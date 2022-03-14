from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer
from .serializers import CommentSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Вы можете менять только свой пост!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Вы можете удалять только свой пост!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied()
        serializer.save(author=self.request.user, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
