import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from main.models import Customer, User
import re
from django.core.exceptions import ValidationError


def contains_only_cyrillic(text):
    pattern = re.compile("[А-Яа-яЁё-]+")
    return bool(pattern.fullmatch(text))


def is_correct_phone_number(phone_number):
    pattern = re.compile(r"^[\d+-]{1,18}$")
    return bool(pattern.match(phone_number))


class AddCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["last_name", "first_name", "fathers_name", "birth_date", "phone"]

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not contains_only_cyrillic(last_name):
            raise ValidationError(
                "Фамилия может содержать только кириллицу и знак дефиса"
            )
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not contains_only_cyrillic(first_name):
            raise ValidationError("Имя может содержать только кириллицу и знак дефиса")
        return first_name

    def clean_fathers_name(self):
        fathers_name = self.cleaned_data["fathers_name"]
        if not contains_only_cyrillic(fathers_name):
            raise ValidationError(
                "Отчество может содержать только кириллицу и знак дефиса"
            )
        return fathers_name

    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        if birth_date.year <= 1920:
            raise ValidationError(
                "Год рождения должен быть больше 1920"
            )
        elif birth_date > datetime.date.today():
            raise ValidationError(
                "Дата рождения должна быть раньше сегодняшнего дня"
            )
        return birth_date

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not is_correct_phone_number(phone):
            raise ValidationError(
                "Номер телефона может содержать только цифры и знаки + и -"
            )
        return phone


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "phone"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not contains_only_cyrillic(first_name):
            raise ValidationError("Имя может содержать только кириллицу и знак дефиса")
        return first_name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not is_correct_phone_number(phone):
            raise ValidationError(
                "Номер телефона может содержать только цифры и знаки + и -"
            )
        return phone


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
