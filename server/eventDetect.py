import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("데 박 뚜 먼 가 이 벤 트 가 생 겼 따 ! %s" % event.src_path) #
        print(event.src_path)
        
        with open(f'{event.src_path}', 'rb') as files:
            try:
                print(type(files))
                upload = {'file':files}
                requests.post('http://192.168.0.38:5557/event-driven', files = upload)
            except Exception as e:
                print(e)
        

def evenvDetection():
    observer = Observer()
    event_handler = ExampleHandler()
    observer.schedule(event_handler, path='./test_folder')
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
    evenvDetection()