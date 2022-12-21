from django.contrib import admin

# Register your models here.

from .models import UserModel
from .models import MessageRoomModel
from .models import MessageModel

adminModels = [UserModel, MessageRoomModel, MessageModel]
admin.site.register(adminModels)