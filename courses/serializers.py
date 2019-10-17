from rest_framework import serializers
from django.db.models import Avg, Sum, Max, Min

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
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
    # reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True, )

    average_rating = serializers.SerializerMethodField()
    sum_total = serializers.SerializerMethodField()
    max_rating = serializers.SerializerMethodField()
    min_rating = serializers.SerializerMethodField()
    min_plus_max = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews',
            'average_rating',
            'sum_total',
            'max_rating',
            'min_rating',
            'min_plus_max'

        )
        model = models.Course

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0

        return round(average * 2) / 2

    def get_sum_total(self, obj):
        sum = obj.reviews.aggregate(Sum('rating')).get('rating__sum')

        if sum is None:
            return 0

        return round(sum)

    def get_max_rating(self, obj):
        max = obj.reviews.aggregate(Max('rating')).get('rating__max')

        if max is None:
            return 0

        return round(max)

    def get_min_rating(self, obj):
        min = obj.reviews.aggregate(Min('rating')).get('rating__min')

        if min is None:
            return 0

        return round(min)


    def get_min_plus_max(self, obj):

        total = self.get_max_rating(obj) + self.get_min_rating(obj)

        return total
