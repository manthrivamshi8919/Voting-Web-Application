from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
class poll(models.Model):
    question = models.CharField(max_length=200)
class vote(models.Model):
    poll = models.ForeignKey(poll, on_delete=models.CASCADE)

class Election(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    


