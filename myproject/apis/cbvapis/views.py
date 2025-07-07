from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FamilyMember  
from .serializers import FamilyMemberSerializer 

# Create your views here.


class FamilyMemberLists(APIView):
    def get(self, request):
        family_members = FamilyMember.objects.all()
        serializer = FamilyMemberSerializer(family_members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FamilyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FamilyMemberDetail(APIView):
    def get(request, pk):
        try:
            family_member = FamilyMember.objects.get(pk=pk)
        except FamilyMember.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FamilyMemberSerializer(family_member)
        return Response(serializer.data)
   

    def put(self, request, pk):
        family_member = FamilyMember.objects.get(pk=pk)
        serializer = FamilyMemberSerializer(family_member, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
    def delete(self, request, pk):
        family_member = FamilyMember.objects.get(pk=pk)
        family_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)