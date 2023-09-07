from django.urls import path
from .views import ExcelFileCreateView, ExcelFileListView

urlpatterns = [
    path('upload/', ExcelFileCreateView.as_view(), name='upload-excel-file'),
    path('files/', ExcelFileListView.as_view(), name='excel-file-list'),
]
