
from rest_framework import serializers
from .models import CompanyReview

class CompanyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyReview
        fields = '__all__'
