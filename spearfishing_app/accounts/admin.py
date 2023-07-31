from django.contrib import admin

from django.contrib.auth import admin as auth_admin, get_user_model

from spearfishing_app.accounts.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()

admin.site.site_header = "Spearfishing Admin"


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm

    ordering = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'gender', 'email',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender',
                    'profile_image_url',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',

                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )
