# compLLMents

## Description

This package enables you to send scheduled, uplifting, AI-generated text messages to yourself and your friends. 

It works by first using am LLM to generate a batch of positive and complimentary messages in the language of choice. Then, a multilingual sentiment classifier scores all the generated posts and selects the most positive to send either as an SMS or over WhatsApp.


DISCLAIMER: If someone you know is suffering from mental health difficulties, please reach out person-to-person or encourage them to seek professional *human* help instead of from chatbots. [Here](https://www.nimh.nih.gov/health/find-help) is one good resource of many.


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

To send SMS messages, first create a free [Twilio](https://www.twilio.com/en-us) account and create a phone number (note: Twilio automatically prepends the message `Sent from your Twilio trial account` to free-tier accounts). Copy your credentials from the dashboard into the `TWILIO_CONFIG` dictionary in `config.py`. An example config will look like:

```
 {
    "account_sid": "a_string",
    "auth_token": "a_token",
    "from_": "+11234567890",
}
```
To send WhatsApp messages, you must log in from your computer.

## Usage

Texts are sent by running:

```
send -r recipient-name -s sender-name -n +11234567890 -l language -b -t type
```

`send --help` explains the parameter options. Pass your OpenAI API key using `-o` to use their models.

You can send custom messages by chaning the text in the `TEMPLATE` object in `main.py`

You can set custom model configuration in the `INFERENCE_CONFIG` object in `conifg.py` including swapping out models, increasing the output length by chaning `max_new_tokens` or increasing the randomness in reponses by raising `temperature` or `top_p`. The default language generation model is `mosaicml/mpt-7b-instruct` which is the [best performing open-sourced LLM](https://gpt4all.io/index.html) at the time of creation. The default sentiment analysis model is `cardiffnlp/xlm-roberta-base-sentiment-multilingual` which supports 8 languagees: `arabic`, `english`, `french`, `german`, `hindi`, `italian`, `portuguese`, and, `spanish`. 


To schedule texts to be sent at regular intervals, create a crontab similar to the example in `cron`.


## Tests

Forethcoming...


## License

MIT License

Copyright (c) [year] [fullname]

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

