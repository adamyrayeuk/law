from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from .models import Account
from .utils import validate_password

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'npm', 'fullname', 'password', 'date_joined', 'last_login', 'is_staff')
        read_only_fields = ('date_joined', 'last_login', 'is_staff')
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data
        """
        validated_data['password'] = make_password(validated_data.get('password'))
        return Account.objects.create(**validated_data)

    def validate(self, data):
        """
        Validate the given password and return the data back if valid, if not then raise validation error
        """
        password_str = data['password']
        password_is_valid = validate_password(password_str)
        if not password_is_valid:
            raise serializers.ValidationError("Password does not meet requirements")
        return data