from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habit.models import Habit


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test1@mail.com")
        self.user.set_password("123")
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="дома",
            time="20:00:00",
            action="читать книгу",
            is_pleasant_habit=False,
            related_habit=None,
            periodicity=5,
            reward="покушать блинчики",
            time_to_complete=60,
            is_public=True,
        )

    def test_create_habit(self):
        """Тестирование на создание полезной привычки"""
        data = {
            "user": self.user.id,
            "place": "дома",
            "time": "20:00:00",
            "action": "читать книгу",
            "is_pleasant_habit": False,
            "periodicity": 5,
            "reward": "покушать блинчики",
            "time_to_complete": 60,
            "is_public": True,
        }
        response = self.client.post(reverse("habit:habit_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(action="читать книгу").exists())

    def test_list_habit(self):
        """Тестирование на вывод списка полезных привычек"""
        response = self.client.get(reverse("habit:habits"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": "дома",
                        "time": "20:00:00",
                        "action": "читать книгу",
                        "is_pleasant_habit": False,
                        "periodicity": 5,
                        "reward": "покушать блинчики",
                        "time_to_complete": 60,
                        "is_public": True,
                        "user": self.user.pk,
                        "related_habit": None,
                    }
                ],
            },
        )

    def test_detail_habit(self):
        """Тестирование на вывод одной привычки"""
        response = self.client.get(
            reverse("habit:habit", kwargs={"pk": self.habit.id}),
        )
        print("RESPONSE", response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": "дома",
                "time": "20:00:00",
                "action": "читать книгу",
                "is_pleasant_habit": False,
                "periodicity": 5,
                "reward": "покушать блинчики",
                "time_to_complete": 60,
                "is_public": True,
                "user": self.user.pk,
                "related_habit": None,
            },
        )

    def test_update_habit(self):
        """Тестирование на обновление или изменения привычки"""
        data = {
            "place": "караоке",
            "time": "23:00:00",
            "action": "спеть песню",
            "is_pleasant_habit": True,
            "periodicity": 3,
            "reward": "",
            "time_to_complete": 90,
            "is_public": False,
        }
        response = self.client.patch(
            reverse("habit:habit_update", kwargs={"pk": self.habit.id}), data=data
        )
        print("RESPONSE", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, data["place"])
        self.assertEqual(self.habit.action, data["action"])

    def test_delete_habit(self):
        """Тестирование на удаление привычки"""
        response = self.client.delete(
            reverse("habit:habit_delete", kwargs={"pk": self.habit.id}),
        )
        print("RESPONSE", response.content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
