from django.contrib import admin
from django.http import HttpResponseRedirect

# Register your models here.
from .models import Question, Choice, Test
 



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

    inlines = [ChoiceInline]

    
admin.site.register(Question, QuestionAdmin)


class TestAdmin(admin.ModelAdmin):
    fields = ['class_name', 'instructor', 'date', 'helpful_relations', 'questions']
    actions = ['export_test']

    def export_test(modeladmin, request, queryset):
        return HttpResponseRedirect("/printpdf")


admin.site.register(Test, TestAdmin)
#admin.site.register(Choice)


