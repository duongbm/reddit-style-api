from django.db.models import Count
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from discuss.models import Discuss, Comment
from discuss.serializers import DiscussSerializer, CommentSerializer, TopDiscussSerializer


class DiscussionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = DiscussSerializer
    queryset = Discuss.objects.all()

    @action(detail=True, methods=['GET'], name='Get comments for a given discuss', url_path='comments')
    def comments(self, request, *args, **kwargs):
        discuss_id = kwargs['pk']
        queryset = Discuss.objects.prefetch_related('comment').get(pk=discuss_id)
        serializer = CommentSerializer(queryset.discuss.all(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], name='Top 10 discuss', url_path='top')
    def top_ten(self, request, *args, **kwargs):
        queryset = Discuss.objects.all().annotate(comments=Count('comment')).order_by('comments')[:10]
        serializer = TopDiscussSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
