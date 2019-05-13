from django.urls import path

from blog import views


urlpatterns = [
    path('', views.ListBlog.as_view()),
    path('<int:pk>', views.DetailBlog.as_view())
]
