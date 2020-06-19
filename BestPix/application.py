import os
from flask import Flask, render_template, send_from_directory
from PIL import Image
from pprint import pprint
from pyheif import read_heif
from sqlite3 import connect
from shutil import rmtree

NUMBER_OF_PHOTOS = 10

app = Flask(__name__)

def get_filenames_and_scores():

    filenames_and_scores_filepath = '/opt/bestpix_data/scores.csv'

    with open(filenames_and_scores_filepath, 'r') as f:
        return [[x.split(', ')[0], float(x.split(', ')[1])] for x in f.read().splitlines()]

def create_folder_if_not_exists(folder):

    if os.path.exists(folder):
        rmtree(folder)

    os.mkdir(folder)


def prepare_photos():
    """Move selected photos to the static folder. Convert HEIC photos to JPEC. Change scores to percent. 

    Args:
        filenames_and_scores (list of tuples): tuples are (filename, score)

    Returns:
        (list of tuples): tuples are (filename, score)
    """

    create_folder_if_not_exists('/opt/bestpix/static')

    filenames_and_scores = get_filenames_and_scores()
    new_photos           = []
    for filename_and_score in filenames_and_scores:

        filename         = filename_and_score[0]
        score_as_percent = f"{round(filename_and_score[1]*100)}%"
        filepath         = os.path.join('/opt/bestpix_data/static', filename) 

        if filename.endswith('heic'):
            heif_file = read_heif(filepath)
            image     = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
            filename  = filename[:-4]+'jpeg'
        
        else:
            image = Image.open(filepath)

        image.save(os.path.join('/opt/bestpix/static', filename))

        new_photos.append((score_as_percent, filename))

    return new_photos


@app.route('/')
def home():

    prepared_photos  = prepare_photos()

    return render_template('home.html', scores_and_photos = prepared_photos)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8442) 

