
import os
import openai

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
    def __init__(self,) -> None:

        self.model = pipeline(
                "sentiment-analysis",
                model="cardiffnlp/xlm-roberta-base-sentiment-multilingual",
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
                    config["model"],
                    #load_in_4bit=True, # uncomment for quantizing
                    trust_remote_code=True,
                    #device_map='auto',
                )

            except:

                self.base_model = AutoModelForSeq2SeqLM.from_pretrained(
                    config["model"],
                    #load_in_4bit=True, # uncomment for quantizing
                    trust_remote_code=True,
                    #device_map='auto',
                )


            self.pipe = pipeline(
                    "text2text-generation",
                    **self.config,
                )
            
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")
                
    def generate_text(self, name: str, language: str):

        if self.use_openai:

            out = openai.Completion.create(
                        model=self.config["model"],
                        prompt=self.prompter.prompt(language=language, name=name),
                        max_tokens= self.config["max_new_tokens"],
                        temperature= self.config["temperature"],
                        n = self.num_examples,
                        stream = False,
                        logprobs = 1,
                        #stop=[],
            )
            return [i["text"] for i in out["choices"]] 

        else:

            out = self.pipe(
                        self.prompter.prompt(language=language, name=name), 
                        num_return_sequences=self.num_examples, 
                        #return_full_text=False,
                        )
            return [i["generated_text"] for i in out]
        
