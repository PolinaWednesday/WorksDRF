from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tracker.models import Lesson
from tracker.serializers.lesson import LessonSerializer


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
