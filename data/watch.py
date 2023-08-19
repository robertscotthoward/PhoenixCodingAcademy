import os
import time
import sys
#sys.path.append(os.path.abspath('../libs'))
from .lib import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.files = {}

    def on_any_event(self, event):
        path = event.src_path

        if path in self.files:
            if self.files[path] == os.path.getmtime(path):
                return
        self.files[path] = os.path.getmtime(path)

        print(path)

def compile(path):
    print(path)
    data = readFile(path)
    print(md5(data))

if __name__=="__main__":
    w = Watcher(".", MyHandler())
    w.run()