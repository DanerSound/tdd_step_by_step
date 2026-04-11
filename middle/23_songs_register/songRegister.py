
def songValidator(song_title, song_text):

    song_title = song_title.replace(" ", "_")
    song_title = song_title.lower() + ".txt"

    with open(song_title, "w") as song_script:
        song_script.write(song_text)

