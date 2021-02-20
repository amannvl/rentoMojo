from rest_framework import serializers
from .models import Phonebook

class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonebook
        fields = ['id', 'name', 'phone', 'email']


    # def update(self, instance, validated_data):
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     # instance.save()
    #
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.name = validated_data.get('zip', instance.name)
    #     instance.save()
    #     return instance


