from .logger import logger
from watchdog.events import RegexMatchingEventHandler

log = logger().logger
que = lambda event: 'directory' if event.is_directory else 'file'

class watchman(RegexMatchingEventHandler):

  def on_moved(self, event):
    super(watchman, self).on_moved(event)

    log.debug('moved %s: from %s to %s', que(event), event.src_path, event.dest_path)

  def on_created(self, event):
    super(watchman, self).on_created(event)

    log.debug('created %s: %s', que(event), event.src_path)

  def on_deleted(self, event):
    super(watchman, self).on_deleted(event)

    log.debug('deleted %s: %s', que(event), event.src_path)

  def on_modified(self, event):
    super(watchman, self).on_modified(event)

    log.debug('modified %s: %s', que(event), event.src_path)
