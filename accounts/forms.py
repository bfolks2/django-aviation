from django import forms


class CreateMemberForm(forms.Form):
    username = forms.CharField(max_length=32)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Password (Again)',
        widget=forms.PasswordInput()
    )
    # home_airport = forms.IntegerField()  Leave off for now, set after Registering
