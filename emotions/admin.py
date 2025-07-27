from django.contrib import admin
from .models_user import CustomUser
from .models import EmotionRecord

admin.site.register(CustomUser)
admin.site.register(EmotionRecord)
