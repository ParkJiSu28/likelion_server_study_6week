from .models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .permissions import IsAuthorUpdateOrReadOnly



# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = [
        IsAuthorUpdateOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs
