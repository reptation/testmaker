from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=256)
    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=128)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()    
    def __str__(self):
        return self.text


class Test(models.Model):
    date = models.DateField()
    instructor = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)
    helpful_relations = models.CharField(max_length=512)
    questions = models.ManyToManyField(Question)
    choices = models.ManyToManyField(Choice)
    def __str__(self):
        return self.class_name
