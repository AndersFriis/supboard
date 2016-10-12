from rest_framework import serializers
from .models import Sup

class SubSerializer(serializers.Modelserializer)
    class Meta:
        model = Sup
        fields = ('id', 'text', 'created_date',)