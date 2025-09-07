import datetime
import struct
from config.config import PROJECT_ROOT,DATA_DIR
from pathlib import Path
import os



class Loader:

    def __init__(self):
        self.path_to_data_dir = DATA_DIR



    def read_files_to_list(self, directory_path) -> list:
        """ group all the files in a directory to a list """
        wav_data_list = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".wav"):
                filepath = os.path.join(directory_path, filename)
                wav_data_list.append(filepath)
        return wav_data_list


    def get_metadata_on_file(self, file) -> object:
        try:
            metadata = os.stat(file)
            # print(metadata.st_size)
            data_file = {file: metadata}
            return data_file
        except FileNotFoundError:
            print(f"Error: File not found at {file}")


    def read_metadata(self):
        wav_files = self.read_files_to_list(self.path_to_data_dir)
        data_to_publish = []
        for file in wav_files:
            dict_metadata = self.get_metadata_on_file(file)
            data_to_publish.append(dict_metadata)

        return data_to_publish





l = Loader()
d =l.read_metadata()
print(d)