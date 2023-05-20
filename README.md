# PowerPoint Generator using python-pptx and local language models.
This is a PowerPoint generator that uses Python-pptx and local llm's using the oobabooga api to generate beautiful and informative presentations. 
Powerpointer doesn't use MARP. It directly creates the powerpoints so you can easily make changes to them or finish it within powerpoint. It also makes placeholders for images.
You can even select between 7 designs to make the powerpoints more beautiful. 
To see some generated powerpoints, look at my below linked powerpointer which uses gpt 3.5. This is more production ready than this. 

This is a port from my powerpointer which uses the gpt 3.5 openai api: [Powerpointer](https://github.com/CyberTimon/powerpointer)
The goal was to have this running completely local with no costs using for example a LLaMA based model. 

I optimized the prompts to work with the vicuna and alpaca like models. You can select the model type in the powerpointer.py file or can create a new prompt format in the pormpts.py file.

# How it works:
- It asks the user about the informations of the powerpoint
- Then it generates the text for the powerpoint using some "hacky" prompts
- The Python-pptx library converts the generated text using my powerpoint format into a PowerPoint presentation

# How to use this:
To make this work, clone the repository and install the following packages: 
```
pip install python-pptx regex collection
```
After this, start your oobabooga text generation webui instance with an instruct finetuned model and the api extension (--api). 13B models and upwards work the best but you sometimes also receive good output with 7B models.

Finally start the powerpoint generator by running:
```
python3 powerpointer.py
```

# Known issues:
Because of the limitation of "small and sometimes dumb" local models:
- the generator easily hallucinates things
- the generator sometimes ignores the selected slide count
- the generator sometimes forgets to include the additional info

Please report any issues and feel free to make a pull request to fix my code I wrote late at night.

Made by CyberTimon (timon@cybertimon.ch)
