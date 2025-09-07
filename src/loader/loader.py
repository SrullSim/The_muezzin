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


    def get_metadata_on_file(self, file) -> dict:

        try:
            file_path = Path(file)
            metadata = file_path.stat()
            filename = Path(file).name
            mod_time = self.convert_to_datetime_type(metadata.st_mtime)

            data_file = {filename : {
                "file_name" : filename,
                "unique_id": self.file_uid_from_metadata(metadata),
                "file_size_in_byts": metadata.st_size,
                "file_create_time": metadata.st_ctime_ns,
                "file_modify_time" : mod_time,
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
            data_to_publish.append(dict_metadata)

        return data_to_publish


    def convert_to_datetime_type(self, st_mtime ):
        mod_time = datetime.datetime.fromtimestamp(st_mtime).strftime("%Y%m%d%H%M%S")
        return mod_time



    def file_uid_from_metadata(self, metadata):
        mod_time = datetime.datetime.fromtimestamp(metadata.st_mtime).strftime("%Y%m%d%H%M%S")
        file_size = metadata.st_size
        return f"{mod_time}_{file_size}"


if __name__ == "__main__":
    l = Loader()
    d =l.collect_metadata()
    print(d)