from django.urls import path,  include
from ocr_demo.views import ImageProcessView, NetworkDataListAPIView

urlpatterns = [
    path('ocr-data-store', ImageProcessView.as_view(), name='ocr_data_store'),
    path('ocr-data-list', NetworkDataListAPIView.as_view(), name='ocr_data_store'),

]