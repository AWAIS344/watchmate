from rest_framework import serializers

from watchlist_app.models import Movie

def validate_name(value):
    if len(value)<2:
        raise serializers.ValidationError("Name too Short")
    return value


class WatchSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField(validate=[validate_name])
    about = serializers.CharField()
    genre = serializers.CharField()
    year = serializers.IntegerField()
    published = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.about = validated_data.get('about',instance.about)
        instance.genre = validated_data.get('genre',instance.genre)
        instance.year = validated_data.get('year',instance.year)
        instance.published = validated_data.get('published',instance.published)
        instance.save()
        return instance
    
    def toogle(self,instance):
        instance.published=not instance.published
        instance.save()
        return instance
    
    def validate(self,data):
        if data['title'] == data["about"]:
            raise serializers.ValidationError("Title and About Should not be SAME")
        return data
    
    # def validate_title(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name too Short")
    #     return value
