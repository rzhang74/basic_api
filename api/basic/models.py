from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdvancedUser(models.Model): 
    uid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, db_column='uid') 
    gender = models.IntegerField(null=True)
    age = models.IntegerField(null=True)

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    
class PostContent(models.Model):
    pid = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="pid")
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    content = models.CharField(max_length=256)
    
class SystemMesg(models.Model):
    mid = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    