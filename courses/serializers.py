from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True }
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'

        )
        model = models.Review



class CourseSerializer(serializers.ModelSerializer):
    #reviews = ReviewSerializer(many=True, read_only=True)
    #reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True,)

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews'

        )
        model = models.Course