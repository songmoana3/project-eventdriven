import os
from fastapi import HTTPException

def save_file(content):
    try:
        file_name = content.filename
        content = content.file.read()
        media_folder = './media'
        
        if not os.path.isdir(media_folder):
            os.makedirs(media_folder)

        with open(os.path.join(media_folder,file_name), 'wb') as file:
            file.write(content)
    
    except Exception as e:
        print(f"UnExpected error: {e}")
        raise HTTPException(status_code = 501, detail = 'Content Save Error') from e