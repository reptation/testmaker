from reportlab.pdfgen import canvas
from django.http import HttpResponse

def some_view(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mynewtestfile.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100,100, "Hello God's world.")

    p.showPage()
    p.save()
    return response


