from django.db import models


class CSVFile(models.Model):
    file = models.FileField(upload_to='csvfiles/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name


class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now=True)

    csv_file = models.ForeignKey(CSVFile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = "Files"
