from celery import shared_task


@shared_task 
def add(x,y): # do not use Django models instances as args. just json data or primitive data types.
    return x + y