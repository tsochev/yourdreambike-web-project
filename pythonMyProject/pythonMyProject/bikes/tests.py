from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory


from pythonMyProject.accounts.models import Profile
from pythonMyProject.bikes.models import Bike, SellBike
from pythonMyProject.bikes.views.generic import DashboardView, PostBikeView, BikesForSale

UserModel = get_user_model()


class DashboardViewTests(TestCase):
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

    def test_when_render_the_correct_template(self):
        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_when_there_are_bikes__expect_bikes(self):
        self.bike = Bike.objects.create(name='Santa', type='Enduro', description='bike',
                                        image='bike.jpg', date_created=date(2020, 3, 8), user=self.user,)

        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(response.context_data['bikes'][0], self.bike)

    def test_when_there_are_not__created_bikes__expect_empty(self):
        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(0, len(response.context_data['bikes']))

    def test_when_there_are_sell_bikes__expect_sell_bikes(self):
        self.sell_bike = SellBike.objects.create(name='Cruz', type='Downhill', frame='CC', fork='Fox', rear_shock='Fox',
                                                 brakes='Sram', drivetrain='Sram', image='cruz.jpg',
                                                 date_created=date(2020, 3, 8), price='5000.0',
                                                 user=self.user,

        )

        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(response.context_data['sell_bikes'][0], self.sell_bike)

    def test_when_there_are_not_sell_bikes__expect_empty(self):
        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(0, len(response.context_data['sell_bikes']))

    def test__when_there_are_posted_bike_and_bike_for_sale(self):
        self.sell_bike = SellBike.objects.create(name='Cruz', type='Downhill', frame='CC', fork='Fox',
                                                 rear_shock='Fox', brakes='Sram', drivetrain='Sram',
                                                 image='cruz.jpg', date_created=date(2020, 3, 8),
                                                 price='5000.0', user=self.user,)

        self.bike = Bike.objects.create(name='Santa', type='Enduro', description='bike',
                                        image='bike.jpg', date_created=date(2020, 3, 8), user=self.user,

        )

        request = self.factory.get('dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)

        self.assertEqual(1, len(response.context_data['sell_bikes']))
        self.assertEqual(1, len(response.context_data['bikes']))
        self.assertEqual(response.context_data['sell_bikes'][0], self.sell_bike)
        self.assertEqual(response.context_data['bikes'][0], self.bike)


class PostBikesViewTests(TestCase):
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

    def test_when_render_the_correct_template(self):
        request = self.factory.get('posted_bikes/')
        request.user = self.user
        response = PostBikeView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_when_there_are_bikes__expect_bikes(self):
        self.bike = Bike.objects.create(name='Santa', type='Enduro', description='bike',
                                        image='bike.jpg', date_created=date(2020, 3, 8), user=self.user,)

        request = self.factory.get('posted_bikes/')
        request.user = self.user
        response = PostBikeView.as_view()(request)

        self.assertEqual(response.context_data['bikes'][0], self.bike)
        self.assertEqual(len(response.context_data['bikes']), 1)

    def test_when_there_are_not_bikes__expect_empty(self):
        request = self.factory.get('posted_bikes/')
        request.user = self.user
        response = PostBikeView.as_view()(request)

        self.assertEqual(0, len(response.context_data['bikes']))


class BikesForSaleViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(
            email='test@test.com',
            password='123456',
        )

        self.profile = Profile.objects.create(
            first_name='Ivan',
            last_name='Test2',
            user=self.user,

        )

    def test_when_render_the_correct_template(self):
        request = self.factory.get('bikes_for_sale/')
        request.user = self.user
        response = BikesForSale.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_when_there_are_sell_bikes__expect_bikes(self):
        self.sell_bike = SellBike.objects.create(name='Cruz', type='Downhill', frame='CC',
                                                 fork='Fox', rear_shock='Fox', brakes='Sram', drivetrain='Sram',
                                                 image='cruz.jpg', date_created=date(2020, 3, 8), price='5000.0',
                                                 user=self.user,)

        request = self.factory.get('bikes_for_sale/')
        request.user = self.user
        response = BikesForSale.as_view()(request)

        self.assertEqual(response.context_data['sell_bikes'][0], self.sell_bike)
        self.assertEqual(len(response.context_data['sell_bikes']), 1)

    def test_when_there_are_not_created_sell_bikes__expect_empty(self):
        request = self.factory.get('bikes_for_sale/')
        request.user = self.user
        response = BikesForSale.as_view()(request)

        self.assertEqual(0, len(response.context_data['sell_bikes']))



