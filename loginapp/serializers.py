from rest_framework import serializers
from .models import LoginData
import re

class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginData
        fields = ['id','username', 'mobile_number','email','user_type']

    # Custom validation for mobile number
    def validate_mobile_number(self, value):
        # Regular expression to check if the number is valid (starts with 6-9 and is 10 digits)
        if not re.match(r'^[6-9]\d{9}$', value):
            raise serializers.ValidationError("Invalid mobile number. It must start with 6-9 and be 10 digits long.")
        return value

