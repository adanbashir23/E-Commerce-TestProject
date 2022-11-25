from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserProfileChangeForm, UserProfileCreationForm

# Register your models here.
UserProfile = get_user_model()


class UserProfileAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name")
    list_display_links = ("email",)

    add_form = UserProfileCreationForm
    add_fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional personal info",
            {
                "fields": (
                    "address",
                    "city",
                    "country",
                    "post_code",
                    "date_of_birth",
                )
            },
        ),
    )

    form = UserProfileChangeForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional personal info",
            {
                "fields": (
                    "address",
                    "city",
                    "country",
                    "post_code",
                    "date_of_birth",
                )
            },
        ),
    )
    model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
