from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer
from deepface import DeepFace
import base64
import numpy as np
import cv2

class EmotionRecordViewSet(viewsets.ModelViewSet):
    serializer_class = EmotionRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return EmotionRecord.objects.all()
        return EmotionRecord.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        base64_img = request.data.get('imagen')

        if not base64_img:
            return Response({"imagen": "No se proporcionó la imagen."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convertir base64 a imagen OpenCV
            header, encoded = base64_img.split(",", 1)
            img_data = base64.b64decode(encoded)
            np_arr = np.frombuffer(img_data, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Analizar emoción
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']

            # Guardar el registro en la base de datos
            serializer = self.get_serializer(data={
                "imagen": base64_img,
                "emotion": emotion
            })
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)

            # Devolver la emoción detectada al frontend
            return Response({
                "message": "Emoción guardada correctamente",
                "emotion": emotion
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("Error al analizar emoción:", e)
            return Response({"error": "Error al analizar la emoción."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
