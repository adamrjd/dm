# Introduction
`dm` is a demo project for Watchdog and Celery, two Python libraries. Watchdog is an simple directory monitring tool with low-level API implementations on all major operating systems -- it seems to be built for extensibility and flexibility. Celery is a distributed task queue and worker management system, with several message brokers supported ootb. This demo lib opts for RabbitMQ for simplicity's sake.

# Dependencies

··· Python36

# Getting Started

First install what you need...

```
$ brew install rabbitmq
$ pip install -r requirements.txt
```

...then start rabbit, watchdog, and celery

```
$ rabbitmq-server -detatched
$ 
```

# TODO

(in unprioritized order)
1. docker-compose
2. some application interfaces for celery
3. more interesting consumers in celery
4. event producers from database queries
