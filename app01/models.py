from django.db import models

# from django import forms
# class dtform(forms):
    # forms.Select(choices=)
# Create your models here.
class Classroom(models.Model):
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    iden = [(1,"admin"),(2,"teacher")]
    identify = models.IntegerField(choices=iden)
    cls = models.ForeignKey(to="Classroom",null=True,blank=True)

class Questionnaire(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=1000)
    url = models.CharField(max_length=32)
    cls = models.ForeignKey(to="Classroom")
    joinNum = models.IntegerField(default=0)
class Question(models.Model):
    questionnaire = models.ForeignKey(to="Questionnaire")
    title = models.CharField(max_length=32)
    choice = [(1,"单选"),(2,"多选"),(3,"文本"),(4,"分值")]

    qtype = models.IntegerField(choices=choice)
class QuestionDetial(models.Model):
    question = models.ForeignKey(to="Question")
    title = models.CharField(max_length=32)
    detail =models.CharField(max_length=32)
class Answer(models.Model):
    user= models.ForeignKey(to="UserInfo")
    ques = models.OneToOneField(to="Question")
    content = models.CharField(max_length=1000)
    class Meta:
        unique_together = [("user","ques"),]
