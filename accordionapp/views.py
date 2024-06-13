from django.shortcuts import render
from .models import AccordionChart


def index(request):
    charts = AccordionChart.objects.all()
    return render(request, 'accordionapp/index.html', {'charts': charts})
