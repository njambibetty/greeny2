from django.urls import path
from . import views
from .views import products_list, product_details,product_upload
#,owner,kiosk,basket
urlpatterns = [
    path('', products_list, name='products-list'),
    path('products/<int:product_id>/',product_details, name='products-details'),
    path("products/upload/", product_upload, name="product-upload"),


    
    # path("products/upload/",owner,name="kiosk_owner"),
    # path("products/upload/", kiosk,name="kiosk"),
    # path("products/upload",basket,name="basket"),
]
