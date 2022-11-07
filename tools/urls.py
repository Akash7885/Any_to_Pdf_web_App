from django import views
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "fileapp"

urlpatterns = [
    path('TextToPdf/', views.TextToPdf, name='TextToPdf'),
    path('ImgToPdf/', views.ImgToPdf, name='ImgToPdf'),
    path('DocxToPdf/', views.DocxToPdf, name='DocxToPdf'),
    path('PngtoPdf/', views.PngtoPdf, name='PngtoPdf'),
    path('feedback/', views.feedback, name='feedback'),
    path('DownloadPage/', views.DownloadPage, name='DownloadPage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
