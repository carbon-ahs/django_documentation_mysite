from polls import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("b/<int:question_id>/", views.details_basic, name = "detail_basic"),
    path("<int:question_id>/", views.details, name = "detail"),
    path("<int:question_id>/results/", views.results, name = "results"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
]
