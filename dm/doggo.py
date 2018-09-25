import sys
import time
from watchdog.observers import Observer
from .handler import watchman

class catch():

  def __init__(self):
    # path to watch
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # event handler
    observer = Observer()
    observer.schedule(watchman(), path, recursive=True)
    observer.start()

    # loop
    try:
      while True:
        time.sleep(1)
    except KeyboardInterrupt:
      observer.stop()

    # thread
    observer.join()
