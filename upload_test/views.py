from django.shortcuts import render
from .forms import UploadFileForm
from . import filehandler
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):

    return render(request, 'upload_test/index.html')


def results(request):

    return render(request, 'upload_test/results.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['file'] = filehandler.file_handler(request.FILES['file'])
            return HttpResponseRedirect('results')
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})



