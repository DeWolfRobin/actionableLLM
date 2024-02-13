# actionableLLM
## What is this repo?
I wanted to create an LLM integration much like the "Google home" and "Alexa"s of the world. In the past I used Dialogflow to get intents from commands and hit webhooks according to those commands. Now, I want to use LLMs to perform these tasks since they are better equiped for this, can adapt more easily to one-off commands and can be run locally.

## Current model
Currently I just took one of the most popular GPT4 models, being the `TheBloke • airoboros l2 gpt4 1 4 1 13B q2_k gguf`. This 5GB model can be stored in the 10GB VRAM of my 3080. With 50 n_gpu_layers in LM studio, I get fast responses, without too much load on my system. This however, is not yet an ideal setup, so sugestions are certainly welcome.

## PoC
Currently there is only a PoC available. To use this yourself:
1. Open LM Studio
1. Select your model
1. Start the LM Studio server
1. Change the user prompt in `assistant.py`
1. Run `python assistant.py`

## End goal
The end goal of this project would be to have a small server script, that can preprocess commands so that it can be used as a "Google home" or "Alexa" replacement. The model would generate Home Assistant payloads, that would then be sent to the HA server in order to perform the requested actions.