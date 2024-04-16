from . import views
from django.urls import path
urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.Thank_youView.as_view()),
    path("review",views.Review_list.as_view()),
    path("review/<int:id>",views.Single_Review.as_view(),name="single-user")
]
