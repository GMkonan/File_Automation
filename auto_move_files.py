from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

folder_to_track = 'E:/Downloads'
folder_destination = 'E:/Downloads'

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_folder_destination = folder_destination
            path_name_file, file_extension = os.path.splitext(src)
            if file_extension == ".jpg" or file_extension == ".png":
                new_folder_destination = 'E:/Imagens'
            elif file_extension == ".pdf":
                new_folder_destination = 'E:/Documentos/PDFS'
            new_destination = new_folder_destination + "/" + filename
            os.rename(src, new_destination)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()