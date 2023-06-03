
INFERENCE_CONFIG = {
        "model": "mosaicml/mpt-7b-instruct", # Path to HF model, use "text-davinci-003" with OpenAI
        "tokenizer": "EleutherAI/gpt-neox-20b", # Path to HF tokenizer
        'max_new_tokens': 100,
        'min_new_tokens': 20,
        "num_examples": 20,
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