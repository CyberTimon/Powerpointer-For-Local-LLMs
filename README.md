# PowerPointer For Local LLMs
Here is a PowerPoint generator that uses python-pptx and local llm's using the Oobabooga Text Generation WebUI api to generate beautiful and informative presentations. 
PowerPointer "For Local LLMs" is a port from my main PowerPointer which uses the GPT 3.5 Turbo OpenAI API: [Powerpointer](https://github.com/CyberTimon/powerpointer) 

The goal was to have this running completely local with no costs using for example a LLaMA based model. 
You can support this by giving this repo a star!


## Features
 - Powerpointer doesn't use MARP. It directly creates the powerpoints so you can easily make changes to them or finish it within PowerPoint
 - It also makes placeholders for images
 - You can select between 7 designs to make the PowerPoints more beautiful
 - Runs locally on your computer so there are no privacy concerns

# How it works:
- It asks the user about the informations of the PowerPoint
- Then it generates the text for the PowerPoint using some optimized prompts and the text generation webui api
- The python-pptx library converts the generated text using my PowerPoint format into a PowerPoint presentation

# How to use this:
To make this work, clone the repository and install the following packages: 
```
pip install python-pptx regex collection
```
After this, start your oobabooga text generation webui instance with an instruct finetuned model and the api extension (--extensions api). 13B models and upwards work the best but you sometimes also receive good output with 7B models. When using 7B models, try instruct tuned Mistral models.

If you run oobabooga on a remote machine or not on a different port/ip, you have to open powerpointer.py and change the HOST or URL variable. **While you are there, also make sure that the model_type ([Prompt Template](#available-prompt-templates) is set correctly.**

Finally start the powerpoint generator by running:
```
python3 powerpointer.py 
```

## Available Prompt Templates
I optimized the prompts to work with instruction tuned models. You can select the prompt format type in the powerpointer.py file. If your desired format is missing, you can create a new prompt format template in the prompts.py file.

Following prompt templates are available out of the box:
 - Alpaca
 - ChatML
 - Vicuna
 - Llama2Chat

Feel free to PR new ones!

## Current best model
As of today (01.07.2024) I recommend to use Nous Hermes Mixtral 8x7b DPO as this yields the best results:
 - [GPT-Q](https://huggingface.co/TheBloke/Nous-Hermes-2-Mixtral-8x7B-DPO-GPTQ)
 - [GGUF](https://huggingface.co/TheBloke/Nous-Hermes-2-Mixtral-8x7B-DPO-GGUF)

Keep in mind that this is quite a big model and requires a good computer to run. If you're looking for a smaller model, I can recommend Hermes Theta 8B:
 - [EXL2](https://huggingface.co/bartowski/Hermes-2-Theta-Llama-3-8B-exl2)
 - [GGUF](https://huggingface.co/bartowski/Hermes-2-Theta-Llama-3-8B-GGUF)

Both model use ChatML as prompt templates.

# Known issues:
Because of the limitation of "small and sometimes dumb" local models:
- the generator easily hallucinates things
- the generator sometimes ignores the selected slide count
- the generator sometimes forgets to include the additional info

Because of my "pro" code:
- it's complicated to add new templates. I'm searching for an easier way

Please report any issues and feel free to make a pull request to fix my code I wrote at night.

Made by CyberTimon (timon@cybertimon.ch)

# Demo screenshots:
Here are some screenshots from the local generated powerpoints:

![alt text](https://raw.githubusercontent.com/CyberTimon/Powerpointer-For-Local-LLMs/main/Examples/AI_sample.png)
![alt text](https://raw.githubusercontent.com/CyberTimon/Powerpointer-For-Local-LLMs/main/Examples/AI_sample2.png)
![alt text](https://raw.githubusercontent.com/CyberTimon/Powerpointer-For-Local-LLMs/main/Examples/Example_run.png)
