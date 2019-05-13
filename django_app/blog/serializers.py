from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'body',
        )
        model = Blog


# fields also could be '__all__'
# if it's actuall all
