from django.db import models

# Create your models here.
class UserModel(models.Model):
    #host=
    profileImageBase64 = models.TextField(null=True, blank=True)
    email = models.CharField()
    name = models.CharField(max_length=200)
    realmId = models.CharField()
    registerDate: models.DateTimeField(auto_now_add=True)
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name

class MessageRoomModel(models.Model):
    users = models.TextField()
    roomName = models.CharField(max_length=200)
    lastMessageId = models.CharField(max_length=200,null=True, blank=True)
    lastUpdateDate: models.DateTimeField(auto_now_add=True)
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
            return self.roomName

class MessageModel(models.Model):
    senderId = models.CharField(max_length=200)
    readers = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    createdDate: models.DateTimeField(auto_now_add=True)
    roomId = models.CharField(max_length=200)
    createdAt: models.DateTimeField(auto_now_add=True)
    updatedAt: models.DateTimeField(auto_now=True)

    def __str__(self) :
            return self.message