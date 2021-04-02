import json

information = json.loads(open('assistant/configurations/themes.json').read())

Theme = "Nobita"

for theme in information["Themes"]:

    if theme["name"] == Theme:

        name = theme["name"]
        voice = theme["voice"]
        bg_image = theme["bg_image"]
        conn_image = theme["conn_image"]
        disconn_image = theme["disconn_image"]
        label_bg_colour = theme["label_bg_colour"]
        scrolltext_bg_colour = theme["scrolltext_bg_colour"]
        button_colour = theme["button_colour"]
        fg_colour = theme["fg_colour"]
        base_font = theme["base_font"]
        title_font = theme["title_font"]


def get_themes():
    print("\nAvailable Themes are:- ")
    for theme in information["Themes"]:
        print("\t", theme["name"])


if __name__ == "__main__":
    get_themes()
