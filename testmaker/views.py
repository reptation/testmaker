from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from .models import Question, Test, Choice


#for testing
import datetime

# Create your views here.

def print_pdf(request):
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    p = canvas.Canvas(buffer)
    now = datetime.datetime.now()    
    p.drawString(100, 100, "hello testmaker, it is %s." % now)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


