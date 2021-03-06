from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserSettings(request):
    user = request.user
    data = request.data

    serializer = UserSerializer(user, many=False, partial=True, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(status=status.HTTP_200_OK)
