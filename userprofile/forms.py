"""User Forms"""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Layout
from allauth.account.forms import LoginForm, SignupForm

class UserProfileCreationForm(UserCreationForm):
    """Signing up form for a user"""

    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        """_summary_"""

        model = get_user_model()
        fields = [
            "full_name",
            "email",
            "password1",
            "password2",
            "address",
            "city",
            "country",
            "post_code",
        ]


class UserProfileChangeForm(UserChangeForm):
    """Updating"""

    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserProfileSignupForm(SignupForm):
    """signup form"""

    full_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=100)
    post_code = forms.CharField(max_length=30)
    avatar = forms.ImageField()

    def save(self, request):
        """Save changes"""
        user = super(UserProfileSignupForm, self).save(request)
        user.username = self.cleaned_data["email"]
        user.full_name = self.cleaned_data["full_name"]
        user.address = self.cleaned_data["address"]
        user.city = self.cleaned_data["city"]
        user.country = self.cleaned_data["country"]
        user.post_code = self.cleaned_data["post_code"]
        user.avatar = self.cleaned_data["avatar"]
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserProfileSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user-signup-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('account_signup')
        self.helper.add_input(
            Submit('submit', 'Register'))
        self.helper.layout = Layout(
            Fieldset('Personal Details',
                     Div(
                         Div('full_name', css_class='col-12 col-sm-6 '
                             'col-md-4'),
                          Div('avatar', css_class='col-12 col-sm-6 '
                             'col-md-4'),
                         css_class='row')
                     ),
            Fieldset('Billing Address',
                     Div(
                         Div('address', css_class='col-12'),
                         Div('city', css_class='col-12 col-sm-4'),
                         Div('country', css_class='col-12 col-sm-4'),
                         Div('post_code', css_class='col-12 col-sm-4'),
                         css_class='row')
                     ),
            Fieldset('Login Details',
                     Div(
                         Div('email', css_class='col-12'),
                         Div('password1', css_class='col-12 col-sm-6'),
                         Div('password2', css_class='col-12 col-sm-6'),
                         css_class='row')
                     )
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "full_name", "address", "city", "country", "post_code", "avatar"]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_id = 'user-profile-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('user_profile')
        self.helper.add_input(
            Submit('submit', 'Update', css_class='btn btn-success'))
        self.helper.layout = Layout(
            Fieldset('Personal Details',
                     Div(
                         Field('full_name', wrapper_class='col-12 col-sm-6 '
                               'col-md-4'),
                         css_class='row')
                     ),
            Fieldset('Address',
                     Div(
                         Field('address', wrapper_class='col-12'),
                         Field('city', wrapper_class='col-12 col-sm-4'),
                         Field('country', wrapper_class='col-12 col-sm-4'),
                         Field('post_code', wrapper_class='col-12 col-sm-4'),
                         css_class='row')
                     )
        )

class UserProfileSigninForm(LoginForm):
    """Create"""
    def __init__(self, *args, **kwargs):
        super(UserProfileSigninForm, self).__init__(*args, **kwargs)

        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_id = 'user-login-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('account_login')
        self.helper.add_input(
            Submit('submit', 'Login'))
        self.helper.layout = Layout(
            Fieldset('Login Details',
                     Div(
                         Field(
                             'login', wrapper_class='col-12 col-sm-9 col-md-6'
                             ' col-lg-4'),
                         css_class='row'),
                     Div(
                         Field(
                             'password', wrapper_class='col-12 col-sm-9 '
                             'col-md-6 col-lg-4'),
                         css_class='row'),
                     )
        )
