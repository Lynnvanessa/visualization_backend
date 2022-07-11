from django.urls import path

from . import views

urlpatterns = [
    path("records/", views.CancerRecordApiView.as_view(), name="records"),
    path("records/<int:pk>/comment/", views.CommentApiView.as_view()),
    path("comments/<int:pk>/", views.CommentDetailView.as_view()),
]
