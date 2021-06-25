""" import logging
import sys
import time

from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
 """
import parse_xml
import watchdog.events
import watchdog.observers
import time
import sys

  
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.ok'],
                                                             ignore_directories=True, case_sensitive=False)
  
    def on_created(self, event):
        #print("Watchdog received CREATED event - % s." % event.src_path)

        # Event is created, you can process it now
        file = event.src_path
        parse_xml.look_for_esn(file)
        

    def on_deleted(self, event):
        print("Watchdog received DELETED event - % s." % event.src_path)  

  
if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()