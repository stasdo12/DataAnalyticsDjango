from rest_framework import generics
from .models import ExcelFile
from .serializers import ExcelFileSerializer


class ExcelFileCreateView(generics.CreateAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer


class ExcelFileListView(generics.ListAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer
