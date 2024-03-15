from django.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),
]
# 장고 가 제공해주는 url 안에서 변수를 설정 할 수 있음 django 는 그걸view funstion 에 줄거임
