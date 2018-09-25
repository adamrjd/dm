from celery import Celery

class throw():
  def __init__(self):
    # instantiate app
    app = Celery('dm',
                 broker='amqp://guest@localhost',
                 backend='amqp://guest@localhost',
                 include=['dm.tasks'])

    # configuration
    app.conf.update(result_expires=3600)

    # run celery app
    app.start()
