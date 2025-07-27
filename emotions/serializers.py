from rest_framework import serializers
from .models import EmotionRecord

class EmotionRecordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = EmotionRecord
        fields = ['id', 'emotion', 'timestamp', 'user', 'username', 'imagen']
        read_only_fields = ['user', 'timestamp']  # ⬅️ QUITA 'emotion'
