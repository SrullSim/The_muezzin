import datetime
import struct
from config.config import PROJECT_ROOT,DATA_DIR
from pathlib import Path
import os
import uuid



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


    def get_metadata_on_file(self, file) -> dict:

        try:
            file_path = Path(file)
            metadata = file_path.stat()
            filename = Path(file).name
            fixed_time_stamp = self.convert_to_datetime_type(metadata.st_mtime)
            data_file = {filename : {
                "file_name" : filename,
                "file_size": metadata.st_size,
                "file_create_time": metadata.st_ctime_ns,
                "file_modify_time" : metadata.st_mtime,
            }}
            return data_file
        except FileNotFoundError:
            print(f"Error: File not found at {file}")
            return {"Error: File not found at" : file}


    def collect_metadata(self):
        """ get dict of metadata for each file in the directory """
        wav_files = self.read_files_to_list(self.path_to_data_dir)
        data_to_publish = []
        for file in wav_files:
            dict_metadata = self.get_metadata_on_file(file)
            dict_metadata["unique_id"] = str(uuid.uuid4())
            data_to_publish.append(dict_metadata)

        return data_to_publish


    def convert_to_datetime_type(self, st_mtime ):
        last_modified_dt = datetime.datetime.fromtimestamp(st_mtime)
        return last_modified_dt



if __name__ == "__main__":
    l = Loader()
    d =l.collect_metadata()
    print(d)