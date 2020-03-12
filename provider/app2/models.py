from django.db import models

# Create your models here.
class NoteData(models.Model):
    username = models.CharField(max_length=20)
    note = models.TextField(max_length=2000)
    data = models.DateField(auto_now_add=True)
    updatedate = models.DateField(auto_now_add=True)