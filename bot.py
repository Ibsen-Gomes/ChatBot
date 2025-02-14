from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ChatbotPTBR:
    def __init__(self, model_name="microsoft/DialoGPT-medium-portuguese"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def get_response(self, user_input):
        input_ids = self.tokenizer.encode(user_input, return_tensors="pt").to(self.device)

        with torch.no_grad():
            response_ids = self.model.generate(input_ids, max_length=100, num_return_sequences=1)

        response = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)

        return response
