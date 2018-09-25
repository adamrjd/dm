import logging
from watchdog.events import RegexMatchingEventHandler

que = lambda event: 'directory' if event.is_directory else 'file'

class watchman(RegexMatchingEventHandler):

  def on_moved(self, event):
    super().on_moved(event)

    logging.debug('moved %s: from %s to %s', que(event), event.src_path, event.dest_path)

  def on_created(self, event):
    super().on_created(event)

    logging.debug('created %s: %s', que(event), event.src_path)

  def on_deleted(self, event):
    super().on_deleted(event)

    logging.debug('deleted %s: %s', que(event), event.src_path)

  def on_modified(self, event):
    super().on_modified(event)

    logging.debug('modified %s: %s', que(event), event.src_path)
