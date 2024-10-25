from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"

    def validate_goto_url(self, value):
        if not value.startswith("http"):
            raise serializers.ValidationError("Goto url must start with http or https")
        return value
