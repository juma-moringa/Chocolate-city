from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/', views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'), 
    url('newhood/', views.create_new_neighbourhood, name='mynewhood'),
    path('joinhood/<id>', views.join_neighbourhood, name='joinhood'),
    path('leavehood/<id>', views.leave_neighbourhood, name='leavehood'),
    path('single_hood/<id>', views.single_neighbourhood, name='single-hood'),
    url('searched/', views.search_business, name='search'),
    path('<id>/post/', views.create_post, name='post'),
    path('<id>/business/', views.create_business, name='business'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)