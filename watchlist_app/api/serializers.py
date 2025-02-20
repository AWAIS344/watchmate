from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Reviews



class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Reviews
        # fields="__all__"
        exclude=["watchlist"]

class WatchListSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model=WatchList
        fields="__all__"


    def get_len_name(self,object):
        return len(object.title)
    

    def validate(self,data):
        if data['title'] == data["storyline"]:
            raise serializers.ValidationError("Title and About Should not be SAME")
        return data
    
    
    def validate_title(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name too Short")
        return value
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    

    watchlist=WatchListSerializer(many=True,read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="moviedetails" 
    # )
    class Meta:
        model=StreamPlatform
        fields="__all__"
        extra_kwargs = {
            'url': {'view_name': 'platformdetails'}  
        }

    def validate(self,data):
        if data['name'] == data["about"]:
            raise serializers.ValidationError("Title and About Should not be SAME")
        return data
    
  
    
    
