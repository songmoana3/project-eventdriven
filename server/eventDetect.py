import time 
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        try:
            print("데 박 뚜 먼 가 이 벤 트 가 생 겼 따 !") 
            with open(event.src_path, 'rb') as files:
                while True:
                    response = requests.post('http://192.168.0.38:5557/event-driven', files = {'file':files})
                    if response.status_code != 200:
                        if str(response.status_code).startswith('5'): # 500대 에러 뜨면 요청 멈추기! 
                            raise Exception('데 박 500 에 러 고 쳐 조')
                        time.sleep(2)                           
                        continue
                    else:
                        print('- save complete - ')
                        break
                    
        except Exception as e:
            print(f'UnExpected Error:{e}')    

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