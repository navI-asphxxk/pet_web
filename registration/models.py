from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"),
                              unique=True,
                              )
    phone = models.IntegerField(_("phone"),
                              unique=True, default=None
                              )
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        # validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    # обязательно поле для регистрации
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "first_name"]
    # Добавьте другие необходимые поля

