from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.v1.hackatrain.serializers import SimplePostInputSerializer, SimpleGetOutputSerializer
from api.v1.hackatrain.view_models import SimplePostViewModel
from base.exceptions import InvalidInputException


class HealthView(APIView):

    def get(self, request):
        return Response(
            status=status.HTTP_200_OK,
            data=datetime.now()
        )


class SimplePostView(APIView):

    def post(self, request):
        input_serializer = SimplePostInputSerializer(data=request.data)

        if not input_serializer.is_valid():
            raise InvalidInputException(errors=input_serializer.errors)

        SimplePostViewModel().save_developer_info(input_serializer.validated_data)

        return Response(
            status=status.HTTP_201_CREATED,
            data='Entry created.'
        )


class SimpleGetView(APIView):

    def get(self, request):
        output_serializer = SimpleGetOutputSerializer
        developers_info = SimplePostViewModel().get_developers_info()
        return Response(
            status=status.HTTP_200_OK,
            data=output_serializer(developers_info).data
        )
