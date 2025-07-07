from rest_framework import serializers
from apis.cbvapis.models import FamilyMember    

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'
        