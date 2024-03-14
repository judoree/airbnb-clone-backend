from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


# fields 에는 보이고싶은걸 추가 할수 있다
# exclude 는 안보이게 하고 싶은걸 추가
