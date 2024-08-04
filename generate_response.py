import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_response(tokenizer, model):
    max_length = 1000
    max_new_tokens = 200

    while True:
        chat_history_ids = None
        print("** New 5 question round **")

        for step in range(5):
            remaining_turns = 5 - step
            print(f"- You have {remaining_turns} remaining questions.")
            
            prompt = input("-- Make a question (or 'stop' to finish the program): ")
            if prompt.lower() == "stop":
                print("- Closing the program...")
                return  # Salir del programa
            
            # Codificar la nueva entrada del usuario y agregar el token de fin de secuencia
            new_user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

            # Preparar el historial de conversación
            if chat_history_ids is None:
                bot_input_ids = new_user_input_ids
                attention_mask = torch.ones(new_user_input_ids.shape, dtype=torch.long).to(model.device)
            else:
                bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
                attention_mask = torch.cat([
                    torch.ones(new_user_input_ids.shape, dtype=torch.long),
                    torch.zeros(chat_history_ids.shape, dtype=torch.long)
                ], dim=-1).to(model.device)

            # Recortar el historial si excede el límite
            if bot_input_ids.shape[1] > max_length:
                bot_input_ids = bot_input_ids[:, -max_length:]
                attention_mask = attention_mask[:, -max_length:]

            # Generar una respuesta
            chat_history_ids = model.generate(
                bot_input_ids,
                max_new_tokens=max_new_tokens,  # Limitar el número de nuevos tokens generados
                pad_token_id=tokenizer.eos_token_id,
                attention_mask=attention_mask
            )

            # Decodificar la respuesta generada
            response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            print("* DialoGPT: {}".format(response))
        
        print("- Round completed. Begening a new round of questions.")
