from django.db import models

# Create your models here.
class Student(models.Model):
    STATUS_CHOICES=(
    ("준비중","준비"),
    ("파견완료","완료"),
    )
    s_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=STATUS_CHOICES, default="준비중")

    def __str__(self):
        return self.name

class Spec(models.Model):
    tof = models.PositiveIntegerField(default=0)
    gpa = models.FloatField(max_length=50)
    when = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=100)
    univ_name = models.CharField(max_length=100)
    kor_name = models.CharField(max_length=100)
    depart = models.CharField(max_length=100)

    def __str__(self):
        return self.country