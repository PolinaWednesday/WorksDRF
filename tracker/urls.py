from django.urls import path
from rest_framework import routers
from tracker.views.course import CourseViewSet
from tracker.views.lesson import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('create/', LessonListCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/update/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_retrieve_update_destroy'),
]

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns += router.urls

