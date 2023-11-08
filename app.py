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

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run()
