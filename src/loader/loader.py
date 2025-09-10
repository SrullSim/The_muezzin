import datetime
from datetime import datetime, timezone
from config.config import PROJECT_ROOT,DATA_DIR, TIMESTAMP
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
        """ build the dict for sending over """
        try:
            file_path = Path(file)
            metadata = file_path.stat()
            filename = Path(file).name

            c_time = self.timestamp_to_datetime(metadata.st_ctime_ns)
            mod_time = self.convert_to_datetime_type(metadata.st_mtime)


            data_file = {'file_details' : {
                "file_name" : filename,
                "file_path": file,
                "unique_id": self.file_uid_from_metadata(metadata),
                "file_size_in_byts": mod_time,
                "file_create_time": c_time,
                "file_modify_time" : mod_time,
            }}
            return data_file
        except FileNotFoundError:
            print(f"Error: File not found at {file}")
            return {"Error: File not found at" : file}


    def collect_metadata(self) -> list:
        """ get dict of metadata for each file in the directory """
        wav_files = self.read_files_to_list(self.path_to_data_dir)
        data_to_publish = []
        for file in wav_files:

            dict_metadata = self.get_metadata_on_file(file)
            data_to_publish.append(dict_metadata)

        return data_to_publish


    def convert_to_datetime_type(self, st_mtime ):
        """ convert type to datetime """
        mod_time = datetime.fromtimestamp(st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        return mod_time


    def timestamp_to_datetime(self,timestamp):
        """ convert type to datetime """
        return datetime.fromtimestamp(TIMESTAMP, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


    def file_uid_from_metadata(self, metadata):
        """ create unique id """
        mod_time = datetime.fromtimestamp(metadata.st_mtime).strftime("%Y%m%d%H%M%S")
        file_size = metadata.st_size
        return f"{mod_time}_{file_size}"


if __name__ == "__main__":
    pass