from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Comments
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        post = self.request.query_params.get('post')
        if post:
            queryset = queryset.filter(post_id=post)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
