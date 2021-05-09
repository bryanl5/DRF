from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
