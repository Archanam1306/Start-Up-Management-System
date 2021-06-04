# url.py website

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from . import views
urlpatterns =[
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('wishlist/',views.wishlist, name='wishlist'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





