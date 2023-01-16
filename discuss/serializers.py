from rest_framework import serializers
from .models import Discuss, Comment


class DiscussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discuss
        fields = ['id', 'title', 'content']


class TopDiscussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discuss
        fields = ['id', 'title', 'content']

    def top(self):
        print(self.data, self.validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'parent', 'discussion_id']

    # discuss = DiscussSerializer()
    # parent = serializers.RelatedField(many=True)
