def format_song_filename(song_artist, song_title):
    filename = song_artist + ' - ' + song_title + '.flac'
    # Replace with DIVISION SLASH and not forward slash
    return filename.replace("/", u'\u2215')