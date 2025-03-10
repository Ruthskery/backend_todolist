from django.urls import path
from .views import user_list, user_detail
from .views import todo_detail, todo_list  # Import the new view


urlpatterns = [
    path("", user_list),  # This should match "api/"
    path("<int:pk>/", user_detail),  # This should match "api/<id>/"
    path("todos/", todo_list),  # For GET and POST
    path("todos/<int:pk>/", todo_detail),  # For PUT and DELETE
]