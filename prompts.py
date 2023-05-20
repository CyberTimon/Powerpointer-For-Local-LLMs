def make_prompt(prompt, slide_count, additional_info, model_type):
    if slide_count:
        slide_count = f"It MUST have exactly {slide_count} slides/contents!!"
    else:
        slide_count = "At least 8 slides/contents."
    if additional_info:
        additional_info = f"Also notice this for the presentation:\n{additional_info}"

    if model_type == "vicuna":
        prefix = "USER:"
        suffix = "ASSISTANT:"
    elif model_type == "alpaca":
        prefix = "### Instruction:"
        suffix = "### Response:"
    else:
        prefix = "### Instruction:"
        suffix = "### Response:"
        
    main_prompt = f"""{prefix} Write a presentation text about {prompt}. You only answer with finished presentation.
You must follow these:
-You write the texts no longer than 250 characters!
-You make very short titles!
-You make the presentation easy to understand.
-The presentation has a table of contents which maches the slide/content count.
-The presentation has a summary.
-You are not allowed to insert links/images.
-{slide_count}

{additional_info}

Example! - Stick to this formatting exactly!
```
Title: TITLE OF THE PRESENTATION

Slide: 1
Header: TABLE OF CONTENT
Content: 1. CONTENT OF THIS POWERPOINT
2. CONTENT OF THIS POWERPOINT
3. CONTENT OF THIS POWERPOINT
...

Slide: 2
Header: TITLE OF SLIDE
Content: CONTENT OF THE SLIDE

Slide: 3
Header: TITLE OF SLIDE
Content: CONTENT OF THE SLIDE

...

Slide: X
Headers: SUMMARY
Content: CONTENT OF THE SUMMARY

Slide: END
```
{suffix}
```
Title:"""
    return main_prompt
