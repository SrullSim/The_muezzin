MAPPING ={
    "mapping":{
        "properties":{
            "file_name":{"type": "keyword"},

            "file_path": {"type": "keyword"},

            "unique_id": {"type":"keyword"},

            "file_size_in_byts":{"type": "long"},

            "file_create_time":{"type":"date_nanos"},

            "file_modify_time":{"type": "date", "format": "yyyyMMddHHmmss"},

            "content_file":{"type": "text"},

            # "processed": {"type": "boolean"}

        }
    }
}
