from datetime import timezone

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from pythonMyProject.accounts.models import Profile, AppUser

VALIDATION_ERROR_NAME = "Ensure this value contains only letters or  numbers."


def validate_letters_and_nums(value):
    allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    for el in value:
        if el not in allowed_chars:
            raise ValidationError(VALIDATION_ERROR_NAME)


UserModel = get_user_model()


class Bike(models.Model):
    NAME_MAX_LEN = 30

    ENDURO = 'Enduro'
    XC = 'XC'
    DOWNHILL = 'Downhill'

    TYPES = [(x, x) for x in (ENDURO, XC, DOWNHILL)]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_letters_and_nums,

        )
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    description = models.TextField()

    image = models.ImageField(
        null=True,
        blank=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class SellBike(models.Model):
    NAME_MAX_LEN = 30
    FRAME_MAX_LEN = 30
    FORK_MAX_LEN = 50
    REAR_SHOCK_MAX_LEN = 50
    BRAKES_MAX_LEN = 50
    DRIVETRAIN_MAX_LEN = 30

    ENDURO = 'Enduro'
    XC = 'XC'
    DOWNHILL = 'Downhill'

    TYPES = [(x, x) for x in (ENDURO, XC, DOWNHILL)]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_letters_and_nums,

        )
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    frame = models.CharField(
        max_length=FRAME_MAX_LEN,
        validators=(
            validate_letters_and_nums,
        )
    )

    fork = models.CharField(
        max_length=FORK_MAX_LEN,
        validators=(
            validate_letters_and_nums,
        )
    )

    rear_shock = models.CharField(
        max_length=REAR_SHOCK_MAX_LEN,
        validators=(
            validate_letters_and_nums,
        )
    )

    brakes = models.CharField(
        max_length=BRAKES_MAX_LEN,
        validators=(
            validate_letters_and_nums,
        )
    )

    drivetrain = models.CharField(
        max_length=DRIVETRAIN_MAX_LEN,
        validators=(
            validate_letters_and_nums,
        )
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    price = models.FloatField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    TRANSACTION_ID_MAX_LEN = 100

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )

    complete = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    transaction_id = models.CharField(
        max_length=TRANSACTION_ID_MAX_LEN,
        null=True,
    )

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        SellBike,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    quantity = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def order_id(self):
        return self.order.id

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    ADDRESS_MAX_LEN = 200
    CITY_MAX_LEN = 100
    COUNTRY_MAX_LEN = 100
    ZIPCODE_MAX_LEN = 100

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        null=True,
    )

    city = models.CharField(
        max_length=CITY_MAX_LEN,
        null=True,
    )

    country = models.CharField(
        max_length=COUNTRY_MAX_LEN,
        null=True,
    )

    zipcode = models.CharField(
        max_length=ZIPCODE_MAX_LEN,
        null=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.address
