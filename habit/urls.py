from django.urls import path

from habit.apps import HabitConfig
from rest_framework.routers import DefaultRouter

from habit.views import (
    HabitViewSet,
    HabitCreateAPIView,
    HabitListAPIView,
    HabitDetailAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HabitPublicListAPIView,
)

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r"habit", HabitViewSet, basename="habit")

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/", HabitListAPIView.as_view(), name="habits"),
    path("habit/<int:pk>/", HabitDetailAPIView.as_view(), name="habit"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("habits/public/", HabitPublicListAPIView.as_view(), name="habits_public"),
] + router.urls
