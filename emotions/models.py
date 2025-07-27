from django.db import models
from .models_user import CustomUser

class EmotionRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    imagen = models.TextField(blank=True, null=True)  # Para guardar la imagen base64

    def __str__(self):
        return f"{self.user.username} - {self.emotion}"