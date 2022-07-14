from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'small-input bg-white margin-20px-bottom required',
                                                            'error_message': 'required-error text-radical-red',

                                                            }))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'small-input bg-white margin-20px-bottom required',
               'error_message': 'required-error text-radical-red',

               }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'small-input bg-white margin-20px-bottom required',
               'error_message': 'required-error text-radical-red',

               }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'small-input bg-white margin-20px-bottom required'
        self.fields['password1'].widget.attrs['class'] = 'small-input bg-white margin-20px-bottom required'
        self.fields['password2'].widget.attrs['class'] = 'small-input bg-white margin-20px-bottom required'




class ForgetPassForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'small-input bg-white margin-20px-bottom required',
                                                            'error_message': 'required-error text-radical-red',

                                                            }))


class ResetPassForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'small-input bg-white margin-20px-bottom '
                                                                       'required',
                                                              'error_message': 'required-error text-radical-red',

                                                              }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'small-input bg-white margin-20px-bottom required',
                                      'error_message': 'required-error text-radical-red',

                                      }))
