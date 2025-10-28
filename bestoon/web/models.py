from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    text = models.CharField(max_length=260, default="Token")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return self.text
class Expense(models.Model):
    text = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}____{self.text}"
class Income(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}____{self.text}"
#class Register(models.Model):
 #   user = models.CharField(User)
  #  password = models.CharField(max_length=48)