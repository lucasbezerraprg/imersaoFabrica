from django.urls import path

from .views import create_car, delete_car, list_all_cars, list_one_car, update_car


urlpatterns = [
    path("", list_all_cars, name="list_all_cars"),
    path("create/", create_car, name="create_car"),
    path("get/<int:pk>/", list_one_car, name="list_one_car"),
    path("update/<int:pk>/", update_car, name="update_car"),
    path("delete/<int:pk>/", delete_car, name="delete_car"),
]
