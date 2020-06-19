import os
import sqlite3
import shutil


class PhotosInterface:
    def __init__(self):

        self._default_photos_folder    = os.path.join(os.path.expanduser('~'), 'Pictures', 'Photos Library.photoslibrary')
        
        self._default_db_folder        = os.path.join(self._default_photos_folder, 'database')
        self._default_originals_folder = os.path.join(self._default_photos_folder, 'originals')
        self.temp_folder               = os.path.join(os.path.expanduser('~'), 'bestpix_data')

    def delete_temp_folder(self):

        if os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)

    def create_temp_folder(self):
        os.makedirs(self.temp_folder, exist_ok=True)

        return self.temp_folder

    def _copy_database(self):
        
        shutil.copytree(self._default_db_folder, self.temp_folder)

    def _run_query(self):

        temp_db_path = os.path.join(self.temp_folder, 'Photos.sqlite')
        connection   = sqlite3.connect(temp_db_path)


        query = """
        
        SELECT zfilename, 
                zoverallaestheticscore 
            FROM   zgenericasset 
            ORDER  BY zoverallaestheticscore DESC 

        """

        cursor  = connection.cursor()

        try:
            return cursor.execute(query).fetchall()
        except:
            print()
            print()
            print("Error: Couldn't connect to the database. You must import your photos first. Guide here: https://support.apple.com/en-us/HT201302#importmac")
            print()
            print()
            exit()

    def _filter_only_photos(self, filenames_and_scores, number_of_photos):

        only_photos = []

        for x in filenames_and_scores:
            extention = x[0][-4:]

            if extention.lower() in ['heic', 'jpeg']:

                only_photos.append(x)

        return only_photos[:number_of_photos]

    def _save_results(self, filenames_and_scores):

        scores_filepath = os.path.join(self.temp_folder, 'scores.csv')

        with open(scores_filepath, 'w') as f:
            for fn_and_s in filenames_and_scores:
                fn = fn_and_s[0]
                s  = fn_and_s[1]

                f.write(f'{fn}, {s}\n')

    def _save_best_photos_to_static_folder(self, filenames_and_scores):

        tmp_static_folder = os.path.join(self.temp_folder, 'static')

        if not os.path.exists(tmp_static_folder):
            os.makedirs(tmp_static_folder)

        for fn_and_s in filenames_and_scores:
            filename = fn_and_s[0]

            src_path = os.path.join(self._default_originals_folder, filename[0], filename)
            dst_path = os.path.join(self.temp_folder, 'static', filename)

            shutil.copyfile(src_path, dst_path)

    def _cleanup(self):

        filepaths = [os.path.join(self.temp_folder, x) for x in os.listdir(self.temp_folder)]

        allowed_keywords = ['static', 'scores.csv']

        for filepath in filepaths:

            delete_this_fp = True

            for kw in allowed_keywords:
                if kw in filepath:
                    delete_this_fp = False
            
            if delete_this_fp:
                try:
                    os.remove(filepath)
                except:
                    shutil.rmtree(filepath)


    def find_photos(self, number_of_photos = 10):
        """
        Create a csv file containing the filepaths to the best photos and their scores.
        Move the best photos to the [_temp_db_location]/static folder
        """
        self.delete_temp_folder()
        self._copy_database()

        filenames_and_scores = self._run_query()
        filenames_and_scores = self._filter_only_photos(filenames_and_scores, number_of_photos)

        self._save_results(filenames_and_scores)

        self._save_best_photos_to_static_folder(filenames_and_scores)

        self._cleanup()
