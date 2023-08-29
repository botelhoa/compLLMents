
import click
import os
import emoji
import subprocess

from huggingface_hub import snapshot_download

from compllments.utils.model import Writer, Selector, Speaker
from compllments.utils.texter import Texter
from compllments.config import INFERENCE_CONFIG, MOZILLA_CONFIG
from compllments.utils.create_audio import download_mozilla_data
from compllments.utils.template import TEMPLATES




@click.command()
@click.option("-model", "-m", type=str, required=True, help='Name of model in HuggingFace Hub.')
def download(model):
    save_path = f"{os.getcwd()}/models/{model.replace('/', '_')}"
    snapshot_download(repo_id=model, local_dir=save_path)



@click.command()
@click.option("-recipient", "-r", type=str, required=True, help='Name of person recieving message. e.g. "Jane Doe".')
@click.option("-sender", "-s", type=str, default="", help='Name of person sending message. e.g. "John Doe".')
@click.option("-number", "-n", type=str, required=True, help='Phone number to text with country code e.g. "+11234567890".')
@click.option("-subject", "-su", type=click.Choice(TEMPLATES.keys()), required=True, help='Subject of message.')
@click.option("-language", "-l", type=str, default="english", help='Language in which to generate text.')
@click.option("-select-best", "-b", is_flag=True, help='Whether to use sentiment analysis to pick the best message.')
@click.option("-message-type", "-t", type=click.Choice(["sms", "whatsapp"]), required=True, help='Type of message.')
@click.option("-message-format", "-f", type=click.Choice(["text", "audio"]), required=True, help='Message format.')
@click.option("-openai-key", "-o", type=str, default="", help='Pass your OpenAI API key if you want to use their models.')
def cli(recipient: str, sender: str, subject: str, number: str, language: str, select_best: bool, message_type: str, message_format: str, openai_key: str):

    os.environ["OPENAI_API_KEY"] = openai_key

    # select_best only works with certain langauges
    if select_best == False:
        INFERENCE_CONFIG["num_examples"] == 1

    if message_format != "text":
        assert message_type == "whatsapp", f"{message_format.capitalize()} messages can only be sent over WhatsApp"


    # Instantiate helper objects
    text_generator = Writer(config=INFERENCE_CONFIG, template=TEMPLATES[subject])
    text_sender = Texter(message_type=message_type, content_type=message_format)
    media_message = None
    text_message = None

    # Generate messages
    messages = text_generator.generate_text(name=recipient, language=language)
    del text_generator

    # Select message
    if select_best == True:
        text_selector = Selector(INFERENCE_CONFIG)
        message_dict = text_selector.select(text_generator.generate_text(name=recipient, language=language))
        print(f"The most positive message had a score of {message_dict['score']}")
        text_message = message_dict["text"]
        del text_selector

    else:
        text_message = messages[0]


    # Speak message
    if message_format == "audio":
        if MOZILLA_CONFIG["first_url"] and not os.path.isfile("data/combined_personal_audio.wav"):
            download_mozilla_data(MOZILLA_CONFIG)

        assert "speech_model" in INFERENCE_CONFIG, "Please specify the text-to-speech model you wish to use."
        text_speaker = Speaker(config=INFERENCE_CONFIG, language=language)
        media_message_path = text_speaker.generate_audio(f"{sender}'s artificially generated voice has a message for you...{text_message}")
        subprocess.run(["ftransc", "-f", "ogg", media_message_path]) # TODO: is this necessary? Delete ftransc package

        media_message = media_message_path.split(".")[0] + ".ogg"
        final_text_message = f"{sender} has a voice message for you:"

        del text_speaker

    else:
        final_text_message = f"{sender} has a message for you: {text_message} \n\nThis message was generated by an AI Chatbot" + emoji.emojize(":robot:")


    # Send message
    text_sender.send(
        number=number,
        text_message=final_text_message,
        media_message=media_message,
        )

    print(f"The following message was sent to {recipient}: \n\n{final_text_message}")



