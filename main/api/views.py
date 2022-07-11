import re
from os import stat

from main.api.serializers import CancerRecordSerializer, CommentSerializer
from main.models import CancerRecord, Comment
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tomlkit import comment


class CancerRecordApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CancerRecordSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return CancerRecord.objects.all()


class CommentApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return Comment.objects.filter(record__id=self.kwargs.get("pk")).order_by("time")

    def post(self, request, *args, **kwargs):
        record_id = kwargs["pk"]
        user = request.user
        _comment = request.data.get("comment", None)

        if _comment is None:
            return Response(status=400, data={"error": "comment message is required"})

        try:
            record = CancerRecord.objects.get(id=record_id)
        except:
            return Response(status=400, data={"error": "record does not exist"})

        comment = Comment.objects.create(record=record, user=user, comment=_comment)
        return Response(CommentSerializer(comment).data)


class CommentDetailView(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(user=user)
