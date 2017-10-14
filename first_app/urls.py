from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^relative/',views.relative_url,name='relative_urls'),
    url(r'^users/',views.help,name='users'),
    url(r'^form_page/',views.user_form_view,name='form')
]