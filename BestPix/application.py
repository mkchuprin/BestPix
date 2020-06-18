import os
from flask import Flask, render_template, send_from_directory
from PIL import Image
from pprint import pprint
from pyheif import read_heif
from sqlite3 import connect
from shutil import rmtree

from .config import PHOTOS_PATH, NUMBER_OF_PHOTOS

app = Flask(__name__)

def get_best_photos_from_database():
    """Connect to the photos database and get the highest rated photos

    Returns:
        (list of tuples): tuples are (filename, score)
    """

    db_path = os.path.join(os.path.expanduser('~'), 'bestpix_data', 'database', 'Photos.sqlite')
    cursor  = connect(db_path).cursor()

    query_result = cursor.execute("""

    SELECT zfilename, 
        zoverallaestheticscore 
    FROM   zgenericasset 
    ORDER  BY zoverallaestheticscore DESC 

    """).fetchall()

    return query_result[:NUMBER_OF_PHOTOS]

def create_folder_if_not_exists(folder):

    if os.path.exists(folder):
        rmtree(folder)

    os.mkdir(folder)


def prepare_photos(filenames_and_scores):
    """Move selected photos to the static folder. Convert HEIC photos to JPEC. Change scores to percent. 

    Args:
        filenames_and_scores (list of tuples): tuples are (filename, score)

    Returns:
        (list of tuples): tuples are (filename, score)
    """

    static_folder = os.path.join(os.path.dirname('__file__'), 'static')

    create_folder_if_not_exists(static_folder)

    new_photos = []
    for filename_and_score in filenames_and_scores:
        score_as_percent = f"{round(filename_and_score[1]*100)}%"
        filename         = filename_and_score[0]
        filepath         = os.path.join(os.path.expanduser('~'), 'bestpix_data', 'originals', filename[0], filename) 

        if filename.endswith('heic'):
            heif_file = read_heif(filepath)
            image     = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
            filename  = filename[:-4]+'jpeg'
        
        else:
            image = Image.open(filepath)

        image.save(os.path.join(static_folder, filename))

        new_photos.append((score_as_percent, filename))

    return new_photos


@app.route('/')
def home():

    filenames_and_scores = get_best_photos_from_database()
    prepared_photos      = prepare_photos(filenames_and_scores)

    return render_template('home.html', scores_and_photos = prepared_photos)


def main():

    app.run(debug=False, host="localhost", port=8442) 

