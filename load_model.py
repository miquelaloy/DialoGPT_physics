from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model():
    model_path = "Dialo_GPT_medium/fine-tuned-model"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    return tokenizer, model
