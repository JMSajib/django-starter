from django.urls import path
from a_users.views import profile_view, profile_edit_view, profile_settings_view, profile_emailcange, profile_emailverified, delete_profile_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('onboarding/', profile_edit_view, name='profile-onboarding'),
    path('settings/', profile_settings_view, name='profile-settings'),
    path('emailchange/', profile_emailcange, name='profile-emailchange'),
    path('emailverify/', profile_emailverified, name='profile-emailverify'),
    path('delete/', delete_profile_view, name='profile-delete')
]