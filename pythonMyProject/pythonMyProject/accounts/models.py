from django.contrib.auth import models as auth_models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from pythonMyProject.accounts.managers import AppUserManager


def validate_only_letters(value):
    if not value.isalpha():
        return ValidationError('The name must contain only letters!')


# Custom User
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 3

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDERS = [(x, x) for x in (MALE, FEMALE, OTHER)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='profile_pic',
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
