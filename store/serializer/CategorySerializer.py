from rest_framework import serializers

from store.models import Category


class CategoryCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # To handle nested object Integrity Error
        # https://medium.com/django-rest-framework/dealing-with-unique-constraints-in-nested-serializers-dade33b831d9
        extra_kwargs = {
            'type': {
                'validators': [],
            }
        }
