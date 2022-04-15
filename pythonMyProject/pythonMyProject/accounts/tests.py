from datetime import date
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse

from pythonMyProject.accounts.models import Profile
from pythonMyProject.accounts.views import DetailsProfileView
from pythonMyProject.bikes.models import Bike

UserModel = get_user_model()


# class DetailsProfileViewTests(django_test.TestCase):
#     VALID_USER_CREDENTIALS = {
#         'email': 'ivan@ivan.com',
#         'password': '123456',
#     }
#
#     VALID_PROFILE_DATA = {
#         'first_name': 'Test',
#         'last_name': 'User',
#     }
#
#     def __create_valid_user_profile(self):
#         user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
#         profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)
#
#         return (user, profile)
#
#     def __create_user(self, **credentials):
#         return UserModel.objects.create_user(**credentials)
#
#     # def test_when_opening_not_existing_profile__expect_404(self):
#     #     response = self.client.get(reverse('profile details', kwargs={'pk': 1}))
#     #
#     #     self.assertEqual(404, response.status_code)
#
#     def test__expect_correct_template(self):
#         user, profile = self.__create_valid_user_profile()
#
#         response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk, }))
#
#         self.assertTemplateUsed('account/profile_details.html')
#
#     def test_when_user_is_owner__expect_to_be_true(self):
#         user, profile = self.__create_valid_user_profile()
#
#         self.client.login(**self.VALID_USER_CREDENTIALS)
#
#         response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
#
#         self.assertTrue(response.context['is_owner'])
#
#     def test_when_owner_is_not_owner__expect_to_be_false(self):
#         user, profile = self.__create_valid_user_profile()
#
#         credentials = {
#             'email': 'ivan2@ivan.com',
#             'password': '123456',
#         }
#
#         self.__create_user(**credentials)
#
#         self.client.login(**credentials)
#
#         response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
#
#         self.assertFalse(response.context['is_owner'])
#
#     def test_when_user_has_bikes__should_has_bike(self):
#         user, profile = self.__create_valid_user_profile()
#
#         VALID_BIKE_DATA = {
#             'name': 'Cruz',
#             'type': 'Enduro',
#             'description': 'helo',
#             'image': 'test.jpg',
#             'date_created': date(2022, 1, 3),
#         }
#
#         bikes = Bike.objects.create(**VALID_BIKE_DATA, user=user)
#         bikes.save()
#
#         request = self.client.get(bikes)
#
#         response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk, }))
#
#         self.assertListEqual(
#             [bikes],
#             response.context['bikes'],
#         )
#
#     def test_when_user_has_no_bikes__bikes_should_be_empty(self):
#         user, profile = self.__create_valid_user_profile()
#
#         response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
#
#         self.assertListEqual([], response.context['bikes'])

class DetailsProfileViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(
            email='test@test.com',
            password='1234',
        )

        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='Test2',
            user=self.user,

        )

        self.bike = Bike.objects.create(name='Santa', type='Enduro', description='bike',
                                        image='bike.jpg', date_created=date(2020, 3, 8), user=self.user, )

    def test_when_user_has_a_posted_bike(self):
        self.client.login(email='test@test.com', password='1234', )
        request = self.client.get(reverse('profile details', kwargs={'pk': self.profile.pk}))

        self.assertEqual(request.status_code, 302)

    def test__expect_correct_template(self):
        response = self.client.get(reverse('profile details', kwargs={'pk': self.profile.pk, }))

        self.assertTemplateUsed('account/profile_details.html')

    # def test_bikes_set_in_context(self):
    #     request = self.factory.get('profile/', kwargs={'pk': self.profile.pk})
    #     response = DetailsProfileView.as_view()(request)
    #
    #     self.assertEqual(len(response.context_data['bikes']), 1)





