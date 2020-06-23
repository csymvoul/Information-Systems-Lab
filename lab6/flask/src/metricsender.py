import json, time, os, requests 
from threading import Thread

exporter_url = os.environ.get("EXPORTER_URL","http://localhost:8081")

class Routine(Thread):
    def __init__(self,handler):
        self.handler = handler 
        super(Routine, self).__init__()
    def run(self):
        print("Routine started ...")
        while True:
            try:
                _data = self.handler()
                requests.post(url=exporter_url,data=json.dumps(_data))
            except Exception as e:
                time.sleep(60)
                print(e)
            time.sleep(5)
