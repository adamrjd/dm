import logging

class logger():

  def __init__(self, name='app', level=logging.DEBUG, file='log'):
    self.name = name
    self.logger = logging.getLogger(name)
    self.logger.setLevel(level)

    fh = logging.FileHandler(file)
    fh.setLevel(level)

    self.logger.addHandler(fh)
