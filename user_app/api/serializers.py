from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError



class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":'password'} ,write_only=True)
    class Meta:
        model= User
        fields=["username",'email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self,):
        email = self.validated_data["email"].lower()
        print(f"🔥 Debug Email: {email}")
        password=self.validated_data["password"]
        passwprd2=self.validated_data["password2"]

        if password!=passwprd2:
            raise serializers.ValidationError({'error':"P1 and P2 must Match"})
        
        if User.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({'error':"User with Email Already Exists!"})
        
        account=User(username=self.validated_data["username"],email=email)
        account.set_password(password)
        account.save()

        return account