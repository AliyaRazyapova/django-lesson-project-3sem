from django.db.models import Prefetch
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.api.serializers import NoteSerializer
from src.web.models import Note, NoteComment


@api_view
def status_view(request):
    return Response({
        "status": "ok", "user_id": request.user.id
    })


class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all().optimize_for_lists().prefetch_related(
        Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
    )
    serializer_class = NoteSerializer
