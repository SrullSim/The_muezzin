MAPPING ={
    "mapping":{
        "properties":{
            "file_name":{"type": "text"},

            "file_size_in_byts":{"type": "long"},

            "file_create_time":{"type":"date_nanos"},

            "file_modify_time":{"type": "date", "format": "yyyyMMddHHmmss"},

            "processed": {"type": "boolean"}

        }
    }
}
p ={
"mapping": {
  "properties": {
    "file_name":        { "type": "text" },
    "file_size_in_byts":{ "type": "long" },
    "file_create_time": { "type": "date_nanos" },
    "file_modify_time": { "type": "date", "format": "yyyyMMddHHmmss" },
    "processed":        { "type": "boolean" }
  }
}
}