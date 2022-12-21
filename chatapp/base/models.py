from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.
class UserModel(models.Model):
    #host=
    profileImageBase64 = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=200,default="")
    name = models.CharField(max_length=200,default="")
    realmId = models.CharField(max_length=256,default="")
    registerDate: models.DateTimeField(auto_now_add=True)
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name

class MessageRoomModel(models.Model):
    users = ArrayField(models.CharField(max_length=200,null=True, blank=True,default=""),default=list)
    roomName = models.CharField(max_length=200,default="")
    lastMessageId = models.CharField(max_length=200,null=True, blank=True,default="")
    lastUpdateDate: models.DateTimeField(auto_now_add=True)
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
            return self.roomName

class MessageModel(models.Model):
    senderId = models.CharField(max_length=200,default="")
    readers = ArrayField(models.CharField(max_length=200,null=True, blank=True,default=""),default=list)
    message = models.CharField(max_length=200,default="")
    createdDate: models.DateTimeField(auto_now_add=True)
    roomId = models.CharField(max_length=200,default="")
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
            return self.message