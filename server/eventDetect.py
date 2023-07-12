import time 
import logging
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        try:
            with open(event.src_path, 'rb') as files:
                while True:
                    response = requests.post('http://192.168.0.38:5557/event-driven', files = {'file':files})
                    if response.status_code != 200:
                        if str(response.status_code).startswith('5'):  
                            raise Exception('error raised')
                        time.sleep(2)                           
                        continue
                    else:
                        logging.info('- save complete - ')
                        break
                    
        except Exception as e:
            logging.error(f'UnExpected Error:{e}')    

def detect_events():
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, path='./test_folder') # 폴더에 뭐가 생기면 자동으로 on_created 메서드가 호출 됨.
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    finally:
        observer.stop()
        observer.join()


if __name__ == '__main__':
    detect_events()