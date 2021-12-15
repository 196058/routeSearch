from django import forms
from .models import User, Mecainfo, Paddy


class UserAddForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput, label='パスワード')
    mail = forms.EmailField(label='電子メール', widget=forms.TextInput(attrs={'class': 'myfieldclass'}))

    class Meta:
        model = User
        fields = ('id', 'user_name', 'pass_word', 'mail')
        labels = {
            'id': 'ユーザID',
            'user_name': '利用者名',
        }


class LoginForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}), label='パスワード')

    class Meta:
        model = User
        fields = ('id', 'pass_word')
        labels = {
            'id': 'ユーザID',
            'pass_word': 'パスワード',
        }


class MecaAddForm(forms.ModelForm):
    class Meta:
        model = Mecainfo
        fields = (
            'id', 'meca_id', 'name', 'full_length', 'full_width', 'jousu', 'joukan', 'kabuma', 'adjusting',
            'workingspeed'
        )
        labels = {
            'name': '機械名',
            'full_length': '全長[mm]',
            'full_width': '全長(幅)[mm]',
            'jousu': '条数[条]',
            'joukan': '条間[cm]',
            'kabuma': '株間[cm]',
            'adjusting': '一株本数調節量[本]',
            'workingspeed': '作業速度[cm/s]'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '好きな名前をつけてください。'}),
            'id': forms.HiddenInput
        }


class PaddyAddForm(forms.ModelForm):
    class Meta:
        model = Paddy
        fields = (
            'id', 'name'
        )
        labels = {
            'name': '田んぼ名'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '好きな名前をつけてください。'}),
            'id': forms.HiddenInput
        }


# class FieldAddForm(forms.ModelForm):
#     class Meta:
#         model = Field
#         fields = (
#             'id', 'lon', 'lat'
#         )
#         widgets = {
#             'id': forms.HiddenInput
#         }

