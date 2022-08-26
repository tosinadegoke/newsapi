from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active  = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    # CREATE A SERIALIZED DATA FROM A VALIDATED DATA
    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    # UPDATE A SERIALIZED DATA OF OBJECT USING THE INSTANCE ANA VALIDATED DATA 
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)     #get takes two parameter bcos e.g. if there is no author, use the value of the instance
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
            
        instance.save()
        return instance