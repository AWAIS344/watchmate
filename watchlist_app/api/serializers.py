from rest_framework import serializers
from watchlist_app.models import WatchList


class WatchListSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()


    class Meta:
        model=WatchList
        fields="__all__"


    def get_len_name(self,object):
        return len(object.title)
    

    def validate(self,data):
        if data['title'] == data["about"]:
            raise serializers.ValidationError("Title and About Should not be SAME")
        return data
    
    
    def validate_title(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name too Short")
        return value
            
    
