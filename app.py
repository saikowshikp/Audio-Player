# from flask import Flask, render_template, send_file

# app = Flask(__name__)

# @app.route('/')
# def index(filename):
#     # List music files from the specified directory
#     music_files = [
#         'music\\badboy.mp3'
#         # Add more songs as needed
#     ]
#     filename=filename.replace("/","\\")
#     # Function to play the selected song
#     return send_file(filename)
#     return render_template('index.html', music_files=music_files)

# @app.route('/play/<path:filename>')
# def play(filename):
#     filename=filename.replace("/","\\")
#     # Function to play the selected song
#     return send_file(filename)
    
# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# # List the songs
# songs = [
#     'badboy.mp3',
#     'psychosaiyaan.mp3'
#     # Add more songs as needed
# ]

# @app.route('/')
# def index():
#     return render_template('index.html', songs=songs)

# @app.route('/play/<song>')
# def play(song):
#     return send_from_directory('static/music', song)

# @app.route('/next')
# def play_next():
#     global current_song_index
#     current_song_index = (current_song_index + 1) % len(songs)
#     return songs[current_song_index]

# @app.route('/previous')
# def play_previous():
#     global current_song_index
#     current_song_index = (current_song_index - 1) % len(songs)
#     return songs[current_song_index]

# @app.route('/shuffle')
# def shuffle_songs():
#     import random
#     global current_song_index
#     current_song_index = random.randint(0, len(songs) - 1)
#     return songs[current_song_index]

# if __name__ == '__main__':
#     current_song_index = 0  # Keeps track of the current song's index
#     app.run(debug=True)



# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # List the songs in the 'music' directory
#     songs = [
#         'badboy.mp3',
#         'psychosaiyaan.mp3'
#         # Add more songs as needed
#     ]
#     return render_template('index.html', songs=songs)

# if __name__ == '__main__':
#     app.run(debug=True)


import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define the directory path
    music_directory = 'static/music'

    # List all the .mp3 files in the 'music' directory
    songs = [file for file in os.listdir(music_directory) if file.endswith('.mp3')]

    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
