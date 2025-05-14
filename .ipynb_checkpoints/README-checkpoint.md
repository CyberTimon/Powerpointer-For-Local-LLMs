# PowerPointer For Local LLMs
Here is a PowerPoint generator that uses python-pptx and local LLMs via OpenAI-compatible API endpoints (such as llama.cpp server or other compatible servers) to generate beautiful and informative presentations. 

PowerPointer "For Local LLMs" is a port from my main PowerPointer which uses the GPT 3.5 Turbo OpenAI API: [Powerpointer](https://github.com/CyberTimon/powerpointer) 

The goal was to have this running completely local with no costs using for example a LLaMA based model. 

You can support this by giving this repo a star!

## Updates
14.05.2025: Add support for the OpenAI chat completions API format (as this is widely used)

## Features
 - Powerpointer doesn't use MARP. It directly creates the powerpoints so you can easily make changes to them or finish it within PowerPoint
 - It also makes placeholders for images
 - You can select between 7 designs to make the PowerPoints more beautiful
 - Runs locally on your computer so there are no privacy concerns
 - Configurable API endpoint to work with any OpenAI-compatible API server

# How it works:
- It asks the user about the information for the PowerPoint
- Then it generates the text for the PowerPoint using optimized prompts and an OpenAI-compatible API endpoint
- The python-pptx library converts the generated text using my PowerPoint format into a PowerPoint presentation

# How to use this:
To make this work, clone the repository and install the following packages: 
```
pip install python-pptx regex collection requests
```

After this, start your local LLM server with an OpenAI-compatible API endpoint (such as llama.cpp server, ollama, or any other server that supports the OpenAI chat completions API format).

The API URL and port can be configured in the `powerpointer.py` file at the top:
```python
# Configuration
API_HOST = "127.0.0.1"
API_PORT = 5005
API_URL = f"http://{API_HOST}:{API_PORT}/v1/chat/completions"
```

Finally start the powerpoint generator by running:
```
python3 powerpointer.py 
```

## Compatible Local LLM Servers
You can use any local LLM server that supports the OpenAI chat completions API format, such as:
- llama.cpp server
- ollama
- text-generation-webui with OpenAI-compatible API extensions
- vllm
- LM Studio

Load the model you like. Larger models are less likely to hallucinate (false information).

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