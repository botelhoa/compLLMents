
INFERENCE_CONFIG = {
        "text_model": "NousResearch/Nous-Hermes-13b",  # HF model name, use "gpt-3.5-turbo" with OpenAI
        "sentiment_model": "cardiffnlp/xlm-roberta-base-sentiment-multilingual", # HF model name
        "speech_model": "tts_models/multilingual/multi-dataset/your_tts", # TTS model name. To see optons run `tts --list_models`
        "tokenizer": "EleutherAI/gpt-neox-20b", # HF tokenizer name
        'max_new_tokens': 250, #100,
        'min_new_tokens': 20,
        "num_examples": 10,
        'do_sample': True,
        'temperature': 0.9,
        'top_p': 0.5,
        'typical_p': 0.5,
        'repetition_penalty': 1,
        'top_k': 40,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        #'truncation_length': 2048,
    }


TWILIO_CONFIG = {
    "account_sid": "",
    "auth_token": "",
    "from_": "", 
}


MOZILLA_CONFIG = {
    "first_url": "",
    "second_url": "",
    }