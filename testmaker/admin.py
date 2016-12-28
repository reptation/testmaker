from __future__ import unicode_literals
from django.contrib import admin
from django.http import HttpResponseRedirect
# Register your models here.
from .models import Question, Choice, Test
 
from django.contrib.contenttypes.models import ContentType


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

    inlines = [ChoiceInline]

    
admin.site.register(Question, QuestionAdmin)


class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = ['class_name', 'instructor', 'date', 'helpful_relations', 'questions']
    actions = ['export_test']
    list_display = ('class_name', 'id')

    def export_test(modeladmin, request, queryset):
#        my_id = queryset.get(id)
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/actions/
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        
        print("selected is %s" % selected)
       
        ct = ContentType.objects.get_for_model(queryset.model)
#        return HttpResponseRedirect("templatetest/%s" %(join(selected)))
#        t_id = str(selected)
#        (my_ct, my_id) 
#	my_id = Test.id
#        print my_id
# Some crap needed for python < 3??
        print(selected[0])
#        print ascii(selected)
        pass
#        return HttpResponseRedirect("/templatetest/ct%sids/%s/" % (ct.pk, ",".join(selected)))        
        return HttpResponseRedirect("/templatetest/%s/" % (selected[0]))        
#        return HttpResponseRedirect("/templatetest/%s" % (t_id))
#        return HttpResponseRedirect("/templatetest", my_id)



admin.site.register(Test, TestAdmin)
#admin.site.register(Choice)


