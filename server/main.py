from fastapi import FastAPI
from router import eventDriven

def get_server():
    
    server = FastAPI(title = 'eventdriven-api', docs_url='/docs', redoc_url=None,
                     openapi_url = f'/openapi.json')
    
    server.include_router(eventDriven.router_eventdriven)
    
    return server

app = get_server()