from celery import Celery

# instantiate app
app = Celery('dm',
              broker='amqp://guest@localhost',
              backend='amqp://guest@localhost',
              include=['dm.tasks'])

# configuration
app.conf.update(result_expires=3600)

# run celery app
app.start()

# define tasks
@app.task
def watchdogger(event):
  # TODO do something
  return