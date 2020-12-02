from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    is_done = models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
