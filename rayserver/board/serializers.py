from rest_framework import serializers
from .models import Post1
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "contents")

    def to_representation(self, instance):
        self.fields['post_id'] =  PostRepresentationSerializer(read_only=True)
        return super(CommentSerializer, self).to_representation(instance)


class PostSerializer(serializers.ModelSerializer):
    post = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post1
        fields = ("id", "title", "contents", "post")


class PostRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post1
        fields = ("id", "title", "contents")