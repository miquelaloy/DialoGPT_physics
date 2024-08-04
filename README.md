This is my first aproach fine-tuning a LLM model.
This is an easy exercise  where I fine-tune the DialoGPT_small and DialoGPT_medium with a database which have 30k answers and questions about Physics (ArtifactAI/arxiv-physics-instruct-tune-30k) from Hugging Face.

To execute this model is very easy, you only need to pip install the requeriments.txt, open a terminal and execute the main.py archive in that terminal.
When you have executed the archive on your terminal you will be able to interact with the model in the same terminal.

This model is not good generating contexto, so the base program is designed to offer a 5 turn conversation, then the context is deleted and restarted for another 5 turn conversation. When you want to finish to chat with the model you only have to write "stop" in the conversation (the model remembers you the "stop" comand in every question)

Finally, there's two models in this repository, DialoGPT_small and DialoGPT_medium. To choose the model which you want to talk yo only have to change de variable "model_path" on the load_model.py archive. If you want to test the small version use this path: "Dialo_GPT_small/fine-tuned-model". For the medium version use this path in "model_path" variable: "Dialo_GPT_medium/fine-tuned-model".

DialoGPT is under MIT License, so read it closely in ther original repository for further information and details about using their model.

