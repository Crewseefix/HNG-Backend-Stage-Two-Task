from .models import Person
from django.http import Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import pdb

class CreateEndpoint(APIView):
    @extend_schema(responses=PersonSerializer)
    def post(self, request):
        if 'country' not in request.data:
            request.data['country'] = 'Nigeria'     
        for key in request.data.keys():
            request.data[key] = request.data[key].lower()
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RUDEndpoint(APIView):
    @extend_schema(responses=PersonSerializer)
    def get(self, request, user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({"detail": "Invalid user_id"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            person = Person.objects.get(id=user_id)
        except (Person.DoesNotExist, ValueError):
            raise Http404("Person not found")
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @extend_schema(responses=PersonSerializer)
    def patch(self, request, user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({"detail": "Invalid user_id"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            person = Person.objects.get(id=user_id)
        except (Person.DoesNotExist, ValueError):
            raise Http404("Person not found")                
        for key in request.data.keys():
            request.data[key] = request.data[key].lower()
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @extend_schema(responses=PersonSerializer)
    def delete(self, request, user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({"detail": "Invalid user_id"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            person = Person.objects.get(id=user_id)
        except (Person.DoesNotExist, ValueError):
            raise Http404("Person not found")
        name = person.name
        person.delete()
        return Response({"detail": f"{name} deleted sucessfully"}, status=status.HTTP_200_OK)
    @extend_schema(responses=PersonSerializer)
    def post(self, request, user_id):
        return redirect('handle_unknown_urls')

class handle_unknown_urls(APIView):
    def dispatch(self, request, *args, **kwargs):
        request.method = 'POST'
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return HttpResponseNotFound("Page not found")
    