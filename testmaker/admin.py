from __future__ import unicode_literals
from django.contrib import admin
from django.http import HttpResponseRedirect
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
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        return HttpResponseRedirect("/templatetest/%s/" % (selected[0]))        

admin.site.register(Test, TestAdmin)

