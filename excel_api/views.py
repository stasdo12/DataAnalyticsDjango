import json

from django.core.files.base import ContentFile
from django.template.base import logger
from rest_framework import generics
from rest_framework.response import Response

from .models import ExcelFile, CSVFile
from .serializers import ExcelFileSerializer
import pandas as pd
import regex as re
from rest_framework import status
import matplotlib.pyplot as plt


class ExcelFileListView(generics.ListAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer


class ExcelFileCreateView(generics.CreateAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def perform_create(self, serializer):
        excel_file = serializer.save()

        try:
            excel_data = pd.read_excel(excel_file.file)
            print(excel_data)
            csv_data = excel_data.to_csv(index=False)

            csv_filename = f"csvfiles/{excel_file.file.name.split('/')[-1].split('.')[0]}.csv"

            csv_file_obj = CSVFile()
            csv_file_obj.file.save(csv_filename, ContentFile(csv_data), save=True)
            print(csv_file_obj)
            excel_file.csv_file = csv_file_obj
            excel_file.save()
            print("ExcelFile object updated")

        except Exception as e:
            logger.error(f"Error creating CSV file: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExcelFileColumnsView(generics.RetrieveAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.csv_file_id:
            csv_file = CSVFile.objects.get(pk=instance.csv_file_id)

            csv_data = pd.read_csv(csv_file.file.path, encoding='cp1251')
            columns = list(csv_data.columns)
            return Response({'columns': columns})
        else:
            return Response({'error': 'No associated CSV file.'}, status=status.HTTP_400_BAD_REQUEST)


class ExcelFileDocumentView(generics.RetrieveAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        function = request.query_params.get('function')
        column_name = request.query_params.get('column_name')

        if instance.csv_file_id:
            csv_file = CSVFile.objects.get(pk=instance.csv_file_id)

            try:
                csv_data = pd.read_csv(csv_file.file.path, encoding='cp1251')
                first_15_records = csv_data.head(15)
                json_data = first_15_records.to_json(orient='records', force_ascii=False)

                if column_name is not None and column_name != "":
                    if function == 'avg':
                        average = csv_data[column_name].mean()
                        return Response({'Average': average})
                    elif function == 'sum':
                        total_sum = csv_data[column_name].sum()
                        return Response({'Sum': total_sum})
                    elif function == 'min':
                        min_value = csv_data[column_name].min()
                        return Response({'Min': min_value})
                    elif function == 'max':
                        max_value = csv_data[column_name].max()
                        return Response({'Max': max_value})
                    elif function == 'mult':
                        multiply_value = csv_data[column_name].prod()
                        return Response({"Multiply": multiply_value})
                    else:
                        return Response({'error': 'Invalid function. Supported functions: average, sum, min, max'},
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'document': json.loads(json_data)})
            except UnicodeDecodeError:
                return Response({'error': 'File decoding error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'No associated CSV file.'}, status=status.HTTP_400_BAD_REQUEST)


class DataAnalysisView(generics.RetrieveAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        csv_data = pd.read_csv(instance.csv_file)

        operation = request.query_params.get('operation')
        if operation == 'regex_search':
            column_name = request.query_params.get('column_name')
            pattern = request.query_params.get('pattern')

            if column_name and pattern:
                try:
                    matched_data = csv_data[csv_data[column_name].str.contains(pattern, flags=re.IGNORECASE, na=False)]
                    result = matched_data.to_dict(orient='records')
                except KeyError:
                    return Response({'error': 'Invalid column name'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Column name and pattern are required.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid operation.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': result})


class DataVisualizationView(generics.RetrieveAPIView):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        csv_data = pd.read_csv(instance.csv_file)

        plt.hist(csv_data['data_column'])
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram')

        image_filename = f"{instance.csv_file.name.split('/')[-1].split('.')[0]}_histogram.png"
        plt.savefig(f'media/{image_filename}')

        return Response({'image_url': f'/media/{image_filename}'})
