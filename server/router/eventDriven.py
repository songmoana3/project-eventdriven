import logging
from typing import List
from fastapi import APIRouter, HTTPException, UploadFile


from crud import eventDrivenCRUD

router_eventdriven = APIRouter(
    prefix = '/event-driven',
    tags = ['J&J test server']
)

@router_eventdriven.post('')
def get_log(
    file : List[UploadFile] = None,
):
    try:
        for content in file:
            eventDrivenCRUD.save_file(content)
            
    except HTTPException as e:
        raise e
    
    except Exception as e:
        logging.error(f'Unexpected Exception: {e}')
        raise HTTPException(status_code = 500, detail = 'Internal Server Error' ) from e