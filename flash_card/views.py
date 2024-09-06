from rest_framework.views import APIView
from flash_card.serializers import CreateFlashCard, UpdateFlashCard, ListFlashCard
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from flash_card.models import FlashCard
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class CreateFlashCardView(APIView):
    def post(self, request):
        serializer = CreateFlashCard(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UpdateFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        serializer = UpdateFlashCard(data=request.data, instance=flash_card)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        flash_card.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ListFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        user_all_flash_card = get_list_or_404(FlashCard, user__id=user_id)

        serializer = ListFlashCard(instance=user_all_flash_card, many=True)

        return Response(serializer.data)
