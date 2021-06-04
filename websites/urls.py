# url.py website

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from . import views
urlpatterns =[
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('faq/',views.faq, name='faq'),
    path('contact/',views.contact, name='contact'),
    path('checkout/',views.checkout, name='checkout'),
    path('blog/',views.blog, name='blog'),
    path('post/',views.post, name='post'),
    path('search/',views.search, name='search'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





