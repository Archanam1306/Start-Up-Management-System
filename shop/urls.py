from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from . import views
urlpatterns =[
    path('<slug:shop>',views.shop, name='shop'),
    path('shoplist/',views.shoplist, name='shoplist'),
    path('shopProducts/',views.shopProducts, name='shopProducts'),
    path('shopProducts/<slug:shop>',views.shopProductsList, name='shopProductsList'),
    path('<slug:shop>/<slug:product>',views.product, name='product'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
