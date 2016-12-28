from django.shortcuts import render, get_object_or_404
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from testmaker.models import Question, Test, Choice

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

def q_and_c(request):
    question = get_object_or_404(Question, pk=1)
    #choices = question.choice_set.all()
    #html = "<html><body>The question is %s.</body></html>" % question
    #return HttpResponse(html)
    return render(request, 'testmaker/q_and_c.html', {'question': question})

def t_and_q(request):
    test = get_object_or_404(Test, pk=1)
    questions = Question.objects.filter(test__id=1)
    choices = Choice.objects.filter(question__in=questions)
    return render(request, 'testmaker/t_and_q.html', {'test': test, 'questions': questions, 'choices': choices})   



#http://stackoverflow.com/questions/1377446/render-html-to-pdf-in-django-site
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


#def template_test(request, test_id='2'):
def template_test(request, test_id='2'):
#    print ("function template test\n")
#    print(test_id)
    my_id = test_id[0]
    print my_id
    test = get_object_or_404(Test, id=my_id)
    questions = Question.objects.filter(test__id=my_id)
    choices = Choice.objects.filter(question__in=questions)
    return render_to_pdf('testmaker/t_and_q.html', {'test': test, 'questions': questions, 'choices': choices, 'pagesize': 'A4'})   

#    #Retrieve data or whatever you need
#    return render_to_pdf(
#            'testmaker/template_test.html',
#            {
#                'pagesize':'A4',
##                'mylist': results,
#            }
#        )


