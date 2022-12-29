from django.db import models

# Create your models here.
class Todo(models.Model):
   # 필드 정dml(필드 타입)
   title = models.CharField(max_length=500)
   description = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   complete = models.BooleanField(default=False)
   important = models.BooleanField(default=False)
   def __str__(self) -> str:
    return self.title
    
