from rest_framework import serializers

class WatchSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    about = serializers.CharField()
    genre = serializers.CharField()
    year = serializers.IntegerField()
    published = serializers.BooleanField()
