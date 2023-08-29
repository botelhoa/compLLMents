# compLLMents

<!-- ![GitHub all releases](https://img.shields.io/github/downloads/botelhoa/compLLMents/total?style=plastic)
![MIT License](https://img.shields.io/bower/l/compLLMents?style=plastic) -->

## Description

This package enables you to send scheduled, uplifting, multi-modal AI-generated text messages to your friends. (Though they won't remain friends long if your only communicate is automated 😉)

It works by first using an LLM to generate a batch of positive and complimentary messages in the language of your choice. Then, a multilingual sentiment classifier scores all the generated posts and selects the most positive to send either as an SMS or over WhatsApp. Further, after recording a few minutes of audio, a custom text-to-speech model will record the message in your voice. [Here](https://colab.research.google.com/drive/1gfTlCWNFgpHdvLR5g8o-OV_a30Pfps60?usp=sharing) is the accompanying Colab notebook.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

First, ensure that [`poetry`](https://python-poetry.org/docs/#installation) is installed. 

```
poetry install
poe install-pytorch
```

To download files to store locally and save time of future downloads, run:

```
download -m path/on/huggingface
```

### SMS 
First create a free [Twilio](https://www.twilio.com/en-us) account and create a phone number (note: Twilio automatically prepends the message `Sent from your Twilio trial account` to free-tier accounts). Copy your credentials from the dashboard into the `TWILIO_CONFIG` dictionary in `config.py`. An example config will look like:

```
 {
    "account_sid": "a_string",
    "auth_token": "a_token",
    "from_": "+11234567890",
}
```

### WhatsApp
You must log in from your computer for the messages to send.


### Audio
Training a custom test-to-speech (TTS) model requires a corpus of recordings to fine tine on. The [Mozilla Common Voice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjwm4ukBhAuEiwA0zQxkwxZgF6SdsfkM8xrx5o7eayEqRS2CVbM2YnIJDUIb0VGqzSrMnBUphoC67kQAvD_BwE) initiative is a crowdsourced voice dataset. After creating an account, you can record yourself speaking sentences in the language of your choosing. Once finished recording, go to `Profile` >> `Download My Data` and copy the URLs you see into the `MOZILLA_CONFIG` dictionary in `config.py` like below:

```
MOZILLA_CONFIG = {
    "first_url": "",
    "second_url": "",
}
```

## Usage

Texts are sent by running:

```
send -r recipient-name -s sender-name -n +11234567890 -l language -t type -b -sa
```

`send --help` explains the parameter options. Pass your OpenAI API key using `-o` to use their models.

You can send custom messages by chaning the text in the `TEMPLATE` object in `main.py`

You can set custom model configuration in the `INFERENCE_CONFIG` object in `conifg.py` including swapping out models, increasing the output length by chaning `max_new_tokens` or increasing the randomness in reponses by raising `temperature` or `top_p`. The default language generation model is `NousResearch/Nous-Hermes-13b` which is the [best performing open-sourced LLM](https://gpt4all.io/index.html) at the time of creation. The default sentiment analysis model is `cardiffnlp/xlm-roberta-base-sentiment-multilingual` which supports 8 languagees: `arabic`, `english`, `french`, `german`, `hindi`, `italian`, `portuguese`, and, `spanish`. 


To schedule texts to be sent at regular intervals, create a crontab similar to the example in `cron`.


### Examples

Here are some examples messages and their sentiment score. 

| Message | Sentiment Score |
| --- | --- |
| Hey Austin! Just wanted to remind you that you are an amazing friend and such a positive force in my life. Keep being you, because you're pretty darn great. | 0.939329206943512 |
| Hey Austin! Just wanted to let you know that you're an amazing friend and I'm lucky to have you in my life. Keep being your awesome self and never forget how much you're loved and appreciated! 😊 | 0.9417279958724976 |
| Hey Austin! Just wanted to remind you that you are an amazing friend and person. Your kindness and positivity always brings a smile to my face. Keep being you, because you're awesome! :) | **0.946333646774292** |

The final recording is below. This was generated by fine-tuning the text-to-speech model on 200 sentences. The more data it is given, the more life-like it will sound.


[![Demo Doccou alpha](![image](https://github.com/botelhoa/compLLMents/assets/56508008/0a691fa1-668e-430e-805a-c787253dab87))](https://github.com/botelhoa/compLLMents/assets/56508008/4a5c5f1f-6080-4937-97c4-b1f3d458a513)



## Tests

Forthcoming...


## Releases

**0.1.0**
- [x] Self-hosted or OpenAI generated compliments
- [x] SMS and WhatsApp supports
- [x] Sentiment-based message selection
- [x] Message scheduling
- [x] User-friendly Colab notebook

**0.1.1**
- [x] Fixed `ReadME.md`

**0.2.0**
- [x] Custom voice messages
- [x] Birthday and custom message templates



## License

MIT License

Copyright (c) [2023] [Austin Botelho]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

