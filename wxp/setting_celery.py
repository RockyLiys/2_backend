# -*- coding: utf-8 -*-
#import djcelery
#djcelery.setup_loader()     #加载djcelery
# celery配置
#CELERY_BROKER_URL = 'redis://:lihuipeng@192.168.x.x:6379/3'
#BROKER_URL = 'django://'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'




