from django.shortcuts import render
from rest_framework import viewsets
from .models import Feedback,Contact
from .serializers import Feedback_serializer,Contact_Serializer
# Create your views here.
class FeedbackModelViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = Feedback_serializer
class ContactModelViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Contact_Serializer