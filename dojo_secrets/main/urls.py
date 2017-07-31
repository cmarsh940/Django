from django.conf.urls import url, include

urlpatterns = [
    url(r'^authentication', include('apps.login_app.urls')),
    url(r'^secrets', include('apps.secrets_app.urls')),
    url(r'^', include('apps.login_app.urls')),

]
