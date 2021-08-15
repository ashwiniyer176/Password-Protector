from django.db.models.query import QuerySet
from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from .models import PasswordModel
from accounts.models import CustomUser
# Create your tests here.


def createCustomPassword():
    user = CustomUser()
    user.save()
    return PasswordModel.objects.create(websiteLink="1234", websiteName="google.com", userName="captpicard", passwordSaved="123", user=user)


class PasswordModelTests(TestCase):
    def test_two_identical_objects(self):
        """
        Two objects with all attributes the same
        """
        user = CustomUser(username="Django")
        user.save()
        items = {
            "websiteLink": '1234',
            "websiteName": "google.com",
            "userName": "captpicard",
            "passwordSaved": "123",
            "user": user
        }

        response = self.client.post(
            reverse('manager:newPassword'), items, follow=True)
        response2 = self.client.post(
            reverse('manager:newPassword'), items, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        query = PasswordModel.objects.filter(websiteLink=items['websiteLink'],
                                             userName=items['userName'],
                                             passwordSaved=items["passwordSaved"],
                                             user=items["user"])
        print(query)
        self.assertTrue(len(query) <= 1)
