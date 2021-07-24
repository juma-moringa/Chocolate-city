from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'), 
    url('newhood/', views.create_new_neighbourhood, name='mynewhood'),
    url('^join/(?P<id>\d+)$',views.join_hood, name='joinhood'),
    
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)