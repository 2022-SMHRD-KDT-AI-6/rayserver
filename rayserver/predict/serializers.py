from rest_framework import  serializers
from .models import Post, Test

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Test
        fields = ('exam_img', 'exam_result', 'mem_id')

