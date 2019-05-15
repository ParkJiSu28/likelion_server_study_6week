from .models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorUpdateOrReadOnly
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = [
        IsAuthorUpdateOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )


