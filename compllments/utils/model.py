
import os
import openai
import torch
#import re
import pandas as pd

from TTS.api import TTS
#from num2words import num2words


from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
from langchain import PromptTemplate



class Prompter:
    def __init__(self, template: str) -> None:

        self.template = PromptTemplate(
                input_variables=["language", "name"],
                template=template,
            )

    def prompt(self, language: str, name: str):
          return self.template.format(language=language, name=name)

    def parse(self, text):
        return text.strip()


class Selector:
    def __init__(self, config: dict) -> None:

        self.model = pipeline(
                "sentiment-analysis",
                model=config["sentiment_model"],
                )
        

    def run(self, text) -> float:
        return self.model(text)
        

    def select(self, text_list: list) -> dict:

        nicest_text = "You are the best" # Default text in case model does not produce postive message
        nicest_score = 0

        for text in text_list:
            out = self.run(text)[0]
            if out["label"] == "positive" and out["score"] > nicest_score:
                nicest_text = text
                nicest_score = out["score"]

        return {"text": nicest_text, "score": nicest_score}


class Writer:

    def __init__(self, config: dict, template: str) -> None:

        self.prompter = Prompter(template)
        self.config = config
        self.num_examples = self.config.pop("num_examples")
        self.use_openai = True if os.environ["OPENAI_API_KEY"] else False
        
        if not self.use_openai:

            self.tokenizer = AutoTokenizer.from_pretrained(config["tokenizer"])

            try:

                self.base_model = AutoModelForCausalLM.from_pretrained(
                    config["text_model"],
                    load_in_8bit=True,
                    trust_remote_code=True,
                    device_map='auto',
                )

                self.pipe = pipeline(
                        "text-generation",
                        return_full_text=False,
                        **self.config,
                    )

            except:

                self.base_model = AutoModelForSeq2SeqLM.from_pretrained(
                    config["text_model"],
                    load_in_8bit=True,
                    trust_remote_code=True,
                    device_map='auto',
                )

                self.pipe = pipeline(
                        "text2text-generation",
                        return_full_text=False,
                        **self.config,
                    )
            
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")
                
    def generate_text(self, name: str, language: str):

        if self.use_openai:

            messages = [{"role": "user", "content": self.prompter.prompt(language=language, name=name)}]

            out = openai.ChatCompletion.create(
                    model=self.config["text_model"],
                    messages=messages,
                    max_tokens=self.config["max_new_tokens"],
                    temperature=self.config["temperature"],
                    top_p=1,
                    n=self.num_examples,
                    stream=False,
                    presence_penalty=0,
                    frequency_penalty=0,
                )

            return [i["message"]["content"] for i in out["choices"]] 

        else:

            out = self.pipe(
                        self.prompter.prompt(language=language, name=name), 
                        num_return_sequences=self.num_examples, 
                        )
            return [i["generated_text"] for i in out]
        


TEXT_CLEANERS = {
    "en": "english_cleaners",
    "pt": "portuguese_cleaners",
    "fr": "french_cleaners",
    "tr": "basic_turkish_cleaners",
    "zh": "chinese_mandarin_cleaners",
    "de": "basic_german_cleaners,"
}

class Speaker:
    def __init__(self, config: dict, language: str) -> None:
        
        language = language.capitalize()
        tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes')[0]
        
        try:
            self.language_code = tables[tables['ISO language name']==language]["639-1"].values[0]
        except: 
            self.language_code = "en"
        
        self.model = TTS(config["speech_model"], progress_bar=False, gpu=torch.cuda.is_available())
        
        self.text_cleaner = TEXT_CLEANERS.get(self.language_code, "multilingual_cleaners")

    def generate_audio(self, text):
        save_path = "data/message2.wav"
        #text = self._preprocess(text)
        self.model.tts_to_file(
            text, 
            speaker_wav="data/combined_personal_audio.wav", 
            language=self.language_code, 
            file_path=save_path,
            text_cleaner=self.text_cleaner,
            #use_phonemes=True,
            )
        return save_path
    

    # def _preprocess(self, text: str) -> str:
    #     """
    #     TODO: Add preprocessors that expand abbreviations, acronyms, and dates as the TTS model only works on letters. 
    #     Skipping for now as these are unlikely outputs from the text generator given the prompt.
    #     """

    #     for i in re.findall(r'\d+', text):
    #         text.replace(num2words(i, lang =self.language_code, to='ordinal'))

    #     return text


