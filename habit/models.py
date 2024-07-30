from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )
    place = models.CharField(max_length=100, verbose_name="место выполнения")
    time = models.TimeField(verbose_name="время выполнения")
    action = models.CharField(max_length=200, verbose_name="действие")
    is_pleasant_habit = models.BooleanField(
        verbose_name="приятная привычка", **NULLABLE
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="связанная привычка", **NULLABLE
    )
    periodicity = models.PositiveSmallIntegerField(
        verbose_name="интервал между привычками в днях"
    )
    reward = models.CharField(max_length=200, verbose_name="вознаграждение", **NULLABLE)
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name="время на выполнение в секундах"
    )
    is_public = models.BooleanField(verbose_name="публичность")

    def __str__(self):
        return f"{self.user} – {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
