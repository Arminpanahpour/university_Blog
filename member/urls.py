from django.urls import path
from member.views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('reset-password/', auth_view.PasswordResetView.as_view(), name='reset-password'),
    # path('reset-password-sent/', auth_view.PasswordResetDoneView.as_view(), name='reset-password-done'),
    # path('reset-password/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name='reset-password-confirm'),
    # path('reset-password-complete/', auth_view.PasswordResetCompleteView.as_view(), name='reset-password-complete'),

]
