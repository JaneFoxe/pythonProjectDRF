from rest_framework import serializers

from habit.models import Habit
from habit.validators import (
    TimeCompleteValidator,
    ChoiceValidator,
    RelatedPleasantValidator,
    PleasantValidator,
    PeriodicityValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    validators = [
        TimeCompleteValidator(field="time_to_complete"),
        ChoiceValidator(field1="related_habit", field2="reward"),
        RelatedPleasantValidator(field1="related_habit", field2="is_pleasant_habit"),
        PleasantValidator(
            field1="is_pleasant_habit", field2="reward", field3="related_habit"
        ),
        PeriodicityValidator(field="periodicity"),
    ]

    class Meta:
        model = Habit
        fields = "__all__"
