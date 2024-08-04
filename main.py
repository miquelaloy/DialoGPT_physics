from load_model import load_model
from generate_response import generate_response

def main():
    tokenizer, model = load_model()
    generate_response(tokenizer, model)

if __name__ == "__main__":
    main()
