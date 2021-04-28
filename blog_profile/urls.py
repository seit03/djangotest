from django.urls import path
from blog_profile.views import ProfileView, ProfileDetailView

urlpatterns = [
    path('profiles/', ProfileView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailView.as_view()),

]