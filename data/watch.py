import sys
import os

# Get this file's path so we can find the libs/
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('../projects')))
sys.path.insert(0, root)

import libs.tools as tools
import libs.subjects as subjects
import time

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
        path = os.path.abspath(event.src_path)
        print(path)
        data = tools.readFile(path)
        hash = tools.md5(data)
        if path in self.files:
            if self.files[path] == hash:
                return
        self.files[path] = hash
        compile(path)


def compile(path):
    subs = subjects.Subjects(path)
    subs.writeHtml("subjects.html")


if __name__=="__main__":
    w = Watcher(".", MyHandler())
    w.run()