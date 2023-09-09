from django.urls import path
from .views import ExcelFileCreateView, ExcelFileListView, ExcelFileColumnsView, DataAnalysisView, \
    DataVisualizationView, ExcelFileDocumentView

urlpatterns = [
    path('upload/', ExcelFileCreateView.as_view(), name='upload-excel-file'),
    path('files/', ExcelFileListView.as_view(), name='excel-file-list'),
    path('columns/<int:pk>/', ExcelFileColumnsView.as_view(), name='get-columns'),
    path('analysis/<int:pk>', DataAnalysisView.as_view(), name='data-analysis'),
    path('visualization/<int:pk>/', DataVisualizationView.as_view(), name='data-visualization'),
    path('doc/<int:pk>/', ExcelFileDocumentView.as_view(), name='open-doc'),


]
