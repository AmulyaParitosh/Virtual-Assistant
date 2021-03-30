import json

information = json.loads(open('assistant/configurations/themes.json').read())

Theme = "Nobita"

for theme in information["Themes"]:

    if theme["name"] == Theme:

        name = theme["name"]        
        voice = theme["voice"]
        art = theme["ascii"]
        bg_image = theme["bg_image"]
        label_bg_colour = theme["label_bg_colour"]
        scrolltext_bg_colour = theme["scrolltext_bg_colour"]
        button_colour = theme["button_colour"]
        fg_colour = theme["fg_colour"]
        base_font = theme["base_font"]
        title_font = theme["title_font"]