from django.db import models
from django.contrib.auth.models import User

class signn(models.Model):
    password=models.TextField(max_length=12)
    email=models.EmailField()
    photo=models.ImageField(blank=True)
    name=models.TextField(blank=True)
    bio=models.TextField(blank=True)
    dob=models.DateField(blank=True,null=True)
    gender=models.CharField(max_length=2,blank=True)
    qualification=models.TextField(blank=True)
    number=models.CharField(max_length=10, null=True, blank=True)
    status=models.CharField(max_length=20,default='No')

class Request_users(models.Model):
    idrequest=models.ForeignKey(signn,related_name='sent_requests',on_delete=models.CASCADE)
    idreciever=models.ForeignKey(signn,related_name='received_requests',on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='No')
    time=models.TimeField(auto_now=True)
    def __str__(self):
        return f"Sender: {self.idrequest.name}, Receiver: {self.idreciever.name}"

    

    



