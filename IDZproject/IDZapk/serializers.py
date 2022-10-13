from rest_framework import  serializers
from IDZapk.models import  UserRegistration
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
