# PowerPoint generator using python-pptx and local large language models.
This is a PowerPoint generator that uses python-pptx and local llm's using the oobabooga text generation webui api to generate beautiful and informative presentations. 
Powerpointer doesn't use MARP. It directly creates the powerpoints so you can easily make changes to them or finish it within powerpoint. It also makes placeholders for images.
You can even select between 7 designs to make the powerpoints more beautiful. 

This is a port from my powerpointer which uses the gpt 3.5 openai api: [Powerpointer](https://github.com/CyberTimon/powerpointer)
The goal was to have this running completely local with no costs using for example a LLaMA based model. You can support this by giving this repo a star!

I optimized the prompts to work with the vicuna and alpaca like models. You can select the model type in the powerpointer.py file or can create a new prompt format in the pormpts.py file.

# How it works:
- It asks the user about the informations of the powerpoint
- Then it generates the text for the powerpoint using some "hacky" prompts and the text generation webui api
- The python-pptx library converts the generated text using my powerpoint format into a PowerPoint presentation

# How to use this:
To make this work, clone the repository and install the following packages: 
```
pip install python-pptx regex collection
```
After this, start your oobabooga text generation webui instance with an instruct finetuned model and the api extension (--extensions api). 13B models and upwards work the best but you sometimes also receive good output with 7B models.

If you run oobabooga on a remote machine or not on a different port/ip, you have to open powerpointer.py and change the HOST or URL variable. When you are there, also make sure that the model_type for the prompt format is set correctly. (Vicuna or Alpaca)

Finally start the powerpoint generator by running:
```
python3 powerpointer.py 
```

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
