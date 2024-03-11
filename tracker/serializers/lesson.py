from rest_framework import serializers
from tracker.models import Course, Lesson
from tracker.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_link')]
