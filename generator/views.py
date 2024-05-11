from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
from .models import Upload, Certificate, Report
from .forms import UploadForm, CertificateForm, ReportForm
from .certifcate import write_name
from .blockchain import Block, Blockchain
import datetime as date
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('list')
    else:
        form = UploadForm()
    return render(request, 'generator/upload.html', {'form': form})

def list_files(request):
    uploads = Upload.objects.filter(user=request.user)
    return render(request, 'generator/list.html', {'uploads': uploads})

def view_file(request, id):
    upload = Upload.objects.get(id=id)
    return render(request, 'generator/view.html', {'upload': upload})

def delete_file(request, id):
    upload = Upload.objects.get(id=id)
    upload.delete()
    return redirect('list')

def generate_certificate(request, dataid):
    upload = Upload.objects.get(id=dataid)
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.upload = upload
            certificate.save()
            # logical implementation
            blockchain = Blockchain()
            blockchain.add_block(Block(1, date.datetime.now(), "Transaction Data 1", ""))
            write_name(upload.file.path, certificate.name)
            return redirect('list_cert')
    else:
        form = CertificateForm()
    return render(request, 'generator/generate.html', {'form': form, 'upload': upload})


def list_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'generator/list_cert.html', {'certificates': certificates})

def download_certificate(request, id):
    certificate = Certificate.objects.get(id=id)
    filename = certificate.certificate.path
    response = HttpResponse(open(filename, 'rb').read())
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
    return response

def view_certificate(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'generator/view_cert.html', {'certificate': certificate})

def delete_certificate(request, id):
    certificate = Certificate.objects.get(id=id)
    certificate.delete()
    return redirect('list_cert')

def report_changes(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            return redirect('list_reports')
    else:
        form = ReportForm()
    return render(request, 'generator/report.html', {'form': form})

def list_reports(request):
    reports = Report.objects.all()
    return render(request, 'generator/list_reports.html', {'reports': reports})

