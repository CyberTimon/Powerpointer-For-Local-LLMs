def make_prompt(prompt, slide_count, additional_info):
    if slide_count:
        slide_count = f"It MUST have exactly {slide_count} slides/contents!!"
    else:
        slide_count = "At least 8 slides/contents."
    if additional_info:
        additional_info = f"Also notice this for the presentation:\n{additional_info}"
        
    main_prompt = f"""Write a presentation text about {prompt}. You only answer with finished presentation.
You must follow these:
-You write the texts no longer than 250 characters!
-You make very short titles!
-You make the presentation easy to understand.
-The presentation has a table of contents which maches the slide/content count.
-The presentation has a summary.
-You are not allowed to insert links/images.
-{slide_count}

{additional_info}

Example! - Stick to this formatting exactly!. Don't wrap it in code blocks or similar. Just start your answer with Title:. Example:

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
"""
    return main_prompt
