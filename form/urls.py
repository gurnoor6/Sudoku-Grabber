
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.image_view,name='image upload'),

    # path('display_img',views.display_img,name='display img')
    # path('aftersubmit',views.aftersubmit,name="result")
]

if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)