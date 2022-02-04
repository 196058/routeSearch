from django import forms
from .models import User, Mecainfo, Paddy, Admin, Field, Inquiry


class UserAddForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput, label='パスワード')
    mail = forms.EmailField(label='電子メール', widget=forms.TextInput(attrs={'class': 'myfieldclass'}))

    class Meta:
        model = User
        fields = ('user_name', 'pass_word', 'mail')
        labels = {
            # 'id': 'ユーザID',
            'user_name': '利用者名',
        }


class LoginForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}), label='パスワード')

    class Meta:
        model = User
        fields = ('user_name', 'pass_word')
        labels = {
            'user_name': 'ユーザ名',
            'pass_word': 'パスワード',
        }


class AdminAddForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput, label='パスワード')
    mail = forms.EmailField(label='電子メール', widget=forms.TextInput(attrs={'class': 'myfieldclass'}))

    class Meta:
        model = Admin
        fields = ('user_name', 'pass_word', 'mail')
        labels = {
            'user_name': '氏名',
        }


class AdminLoginForm(forms.ModelForm):
    pass_word = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'myfieldclass'}), label='パスワード')

    class Meta:
        model = Admin
        fields = ('user_name', 'pass_word')
        labels = {
            'user_name': 'ユーザ名',
            'pass_word': 'パスワード',
        }


class MecaAddForm(forms.ModelForm):
    class Meta:
        model = Mecainfo
        fields = (
            'id', 'name', 'full_length', 'full_width', 'plant'
        )
        labels = {
            'name': '機械名',
            'full_length': '全長[mm]',
            'full_width': '全長(幅)[mm]',
            'plant': '条数[条]',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '機械に名前をつけてください。'}),
            'id': forms.HiddenInput
        }


class PaddyAddForm(forms.ModelForm):
    class Meta:
        model = Paddy
        fields = (
            'paddy_id', 'paddy_name'
        )
        labels = {
            'paddy_name': '田んぼ名'
        }
        widgets = {
            'paddy_name': forms.TextInput(attrs={'placeholder': '田んぼに名前をつけてください。'}),
            'id': forms.HiddenInput
        }


class FieldAddForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = (
            'id', 'location_json_data', 'location_start_end_point_data'
        )
        widgets = {
            'id': forms.HiddenInput
        }


class InquiryAddForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = (
            'inquiry_no', 'inquiry_id', 'title', 'contents'
        )
        labels = {
            'inquiry_id': '対応ID',
            'title': 'タイトル',
            'contents': '内容',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '好きな名前をつけてください。'}),
            'id': forms.HiddenInput
        }