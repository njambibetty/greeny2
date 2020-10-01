from django.urls import path
from . import views
from .views import kiosk_upload,kioskOwner_upload

urlpatterns = [
      path("kiosk/upload/", kiosk_upload, name="kiosk-upload"),
       path("kioskOwner/upload/", kioskOwner_upload, name="kioskOwner-upload"),
]