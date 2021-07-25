from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'), 
    # url('all-hoods/',views.neighbourhoods,name='neighbourhood'),
    url('newhood/', views.create_new_neighbourhood, name='mynewhood'),
    url('singlehood/<hood_id>', views.single_neighbourhood, name='singlehood'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
   
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)