from django import forms
from .models import Event, Story
import jdatetime




class EventCreateForm(forms.ModelForm):
    event_date = forms.CharField(
        label="تاریخ رویداد",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "persian-datepicker",
                "placeholder": "مثلاً: 1404/02/15",
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = Event

        fields = (
            "name",
            "image",
            "description",
            "event_date",
            "start_hour",
            "end_hour",
            "privacy",
        )

        labels = {
            "name": "نام رویداد",
            "image": "تصویر رویداد",
            "description": "توضیحات",
            "start_hour": "ساعت شروع",
            "end_hour": "ساعت پایان",
            "privacy": "نوع دسترسی",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "مثلاً: جلسه تیم طراحی",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "start_hour": forms.TimeInput(
                format="%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
            "end_hour": forms.TimeInput(
                format="%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
            "privacy": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_event_date(self):
        persian_date_str = self.cleaned_data.get('event_date')

        if not persian_date_str:
            raise forms.ValidationError("تاریخ رویداد الزامی است")

        try:
            # Parse Persian date - handle both / and - separators
            persian_date_str = persian_date_str.replace('/', '-')
            j_date = jdatetime.datetime.strptime(persian_date_str, '%Y-%m-%d').date()
            gregorian_date = j_date.togregorian()
            return gregorian_date
        except ValueError:
            raise forms.ValidationError("فرمت تاریخ نامعتبر است. لطفا از فرمت ۱۴۰۴/۰۲/۱۵ استفاده کنید")

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get("start_hour")
        end = cleaned_data.get("end_hour")

        if start and end and start >= end:
            raise forms.ValidationError(
                "ساعت پایان باید بعد از ساعت شروع باشد."
            )

        return cleaned_data


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label="", widget=forms.TextInput(attrs={'class': "form-control form-control-lg",
                                                                                   'placeholder': 'comment',
                                                                                   "rows": 6,
                                                                                   'style': "resize: vertical;"}))


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['image']
