from  django import forms
from .models import Upload, Certificate, Report

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ['user']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'