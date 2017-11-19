from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import View, DetailView
from BolInput.utils import render_to_pdf
from easy_pdf.views import PDFTemplateResponseMixin
from models import Load
from .forms import LoadForm

# Create your views here.

class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Load
    template_name = 'load_pdf.html'      

def load_list(request):
    loads = Load.objects.all().order_by('date_created')
    return render(request, 'load_list.html', {'loads':loads})

def load_detail(request, pk):
    load = get_object_or_404(Load, pk=pk)
    return render(request, 'load_detail.html', {'load': load})

def load_new(request):
    if request.method == "POST":
        form = LoadForm(request.POST)
        if form.is_valid():
            load = form.save(commit=False)
            load.date_created = timezone.now()
            load.save()
            return redirect('load_detail', pk=load.pk)
    else:
        form = LoadForm()
    return render(request, 'load_edit.html', {'form': form})

def load_edit(request, pk):
    load = get_object_or_404(Load, pk=pk)
    if request.method == "POST":
        form = LoadForm(request.POST, instance=load)
        if form.is_valid():
            load = form.save(commit=False)
            load.date_created = timezone.now()
            load.save()
            return redirect('load_detail', pk=load.pk)
    else:
        form = LoadForm(instance=load)
    return render(request, 'load_edit.html', {'form': form})

def load_remove(request, pk):
    load = get_object_or_404(Load, pk=pk)
    load.delete()
    return redirect('load_list')



class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': Load.load_number, 
            'amount': Load.load_number,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Bill_Of_Lading_%s.pdf" %("1234567")
            content = "inline; filename='%s'" %(filename)
            
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")