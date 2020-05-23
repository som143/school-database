from django.db import models

# Create your models here.
class school(models.Model):
    classes =  models.CharField( max_length=10)
    strength = models.IntegerField()
    cls_teacher = models.CharField(max_length=20)

    def __str__(self):
        return self.classes
class details(models.Model):
    day = models.CharField(max_length=50)
    present_strngth = models.IntegerField()
    sub = models.CharField(max_length = 10)
    teacher_name = models.CharField(max_length= 30)
    classes =  models.CharField(max_length = 20)
    school_child = models.ForeignKey(school,null = True, blank =True, on_delete=models.CASCADE)
    def __str__(self):
        return self.day
