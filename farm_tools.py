# Copyright 2024 Fox Farmer (GitHub: thefoxfarmer, Discord: foxfarmer)

import os
#import hashlib


class LoadFileAsString:

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_file_as_string"
    CATEGORY = "loaders"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"multiline": False}),
            }
        }

    @classmethod
    def IS_CHANGED(cls, file_path):
        st = os.stat(file_path)
        return f"{st.st_ino}.{st.st_dev}.{st.st_size}.{st.st_mtime}.{st.st_ctime}"
        #m = hashlib.sha256()
        #m.update(open(file_path, 'rb').read())
        #return m.digest().hex()

    def __init__(self):
        pass

    def load_file_as_string(self, file_path=''):
        text = open(file_path, 'r', encoding="utf-8").read()
        return (text,)


NODE_CLASS_MAPPINGS = {
    'LoadFileAsString': LoadFileAsString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'LoadFileAsString': 'Load File as String',
}
