from django.apps import AppConfig



class UsersConfig(AppConfig):
    name = 'users'
    #https://docs.djangoproject.com/en/2.0/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import users.signals

    #https://docs.djangoproject.com/en/3.1/topics/signals/
    
