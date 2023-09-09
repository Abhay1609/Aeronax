from rest_framework import serializers
from .models import Feedback,Contact
class Feedback_serializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Feedback

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Contact