# compLLMents>

## Description

This package enables you to send scheduled, uplifting, AI-generated text messages to yourself and your friends. 

It works by first using am LLM to generate a batch of positive and complimentary messages in the language of choice. Then, a multilingual sentiment classifier scores all the generated posts and selects the most positive to send either as an SMS or over WhatsApp.


DISCLAIMER: If you or someone you know is suffering from mental health difficulties, please seek professional *human* help instead of from chatbots. 
[Here]() is one good resource of many.


Provide a short description explaining the what, why, and how of your project. Use the following questions as a guide:

- What was your motivation?
- Why did you build this project? (Note: the answer is not "Because it was a homework assignment.")
- What problem does it solve?
- What did you learn?

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Installation

First, ensure that [`poetry`](https://python-poetry.org/docs/#installation) is installed. 

```
poetry install
poe install-pytorch
```

To download files to store locally and save time of future downloads, run:
`download -m path/on/huggingface`

To send SMS messages, first create a free [Twilio](https://www.twilio.com/en-us) account (note: Twilio automatically prepends the message `blah` to free-tier accounts). Copy your credentials from the dashboard into the `TWILIO_CONFIG` dictionary in `config.py`. An example config will look like:
```
 {
    "account_sid": "a_string",
    "auth_token": "a_token",
}
```

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

Texts are sent by running:
```
send -r recipient-name -s sender-name -n +11234567890 -l language -b -t sms
```

`send --help` explains the parameter options.

You can send custom messages by chaning the text in the `TEMPLATE` object in `main.py`

You can set custom model configuration in the `INFERENCE_CONFIG` object in `conifg.py` including swapping out models, increasing the output length by chaning `max_new_tokens` or increasing the randomness in reponses by raising `temperature` or `top_p`.


Below are some example text generations
```
```

And here are the sentiment scores for them
```
```

To schedule texts to be sent at regular intervals, 
- crontab setup



## Tests


## Credits

List your collaborators, if any, with links to their GitHub profiles.

If you used any third-party assets that require attribution, list the creators with links to their primary web presence in this section.

If you followed tutorials, include links to those here as well.


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

Roadmap

1.   Locally hosted
2.   Ping API
3.   Multilingual
4.   SMS + WhatsApp support
5.   Select nicest
6.   cron job scheduling
7.   publish to pypi

