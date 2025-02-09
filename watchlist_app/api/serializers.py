from rest_framework import serializers

from watchlist_app.models import Movie
class WatchSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField()
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
