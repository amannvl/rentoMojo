from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import requests
from .serializers import PhonebookSerializer
from .models import Phonebook
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny,])
def get_phonebooks(request):
    user = request.user.id
    phonebooks = Phonebook.objects.all()
    serializer = PhonebookSerializer(phonebooks, many=True)
    return JsonResponse({'phonebooks': serializer.data}, safe=False, status=status.HTTP_200_OK)


#add new contact


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def add_phonebook(request):
    # payload = json.loads(request.body)
    user = request.user
    try:
        # data = Phonebook.objects.get(id=payload["data"])
        phonebook = Phonebook.objects.create(
            name=request.data.get('name', False),
            email=request.data.get('email', False),
            phone=request.data.get('phone', False),
        )
        serializer = PhonebookSerializer(phonebook)
        return JsonResponse({'phonebooks': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#update

@api_view(["PUT"])
@csrf_exempt
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, BasicAuthentication,])
def update_phonebook(request, id):
    user = request.user.id
    # payload = json.loads(request.body)
    payload = request.data
    try:
        book_item = Phonebook.objects.filter(id=id).update(name = request.data.get("name"), email = request.data.get("email"), phone = request.data.get("phone"))
        # returns 1 or 0
        # book_item.update(**payload)
        book = Phonebook.objects.get(id=id)
        serializer = PhonebookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#delete a contact

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication,BasicAuthentication])
def delete_phonebook(request, id):
    user = request.user.id
    try:
        phonebook = Phonebook.objects.get(id=id)
        phonebook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)