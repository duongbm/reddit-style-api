from django.urls import include, path
from rest_framework import routers
from .views import DiscussionViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'discuss', DiscussionViewSet, basename='discuss')
router.register(r'comment', CommentViewSet, basename='comment')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
