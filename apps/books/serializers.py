from rest_framework import serializers, pagination
from .models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ('created', 'updated')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ('created', 'updated')
    # allow indicate how to return each value
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'year': instance.year,
            'title': instance.title,
            'author': instance.author.full_name,
            'editorial': instance.editorial.name,
            'is_available': instance.is_available,
            # here we can use a conditional 'if' to validate data, like
            # 'image': instance.image if instance.image != '' else ''
        }