from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for displaying and updating the UserProfile model,
    excluding the User field.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'user': 'User',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality'
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                widget_attrs = self.fields[field].widget.attrs
                widget_attrs['class'] = (
                    'border-black rounded-0 profile-form-input'
                )
                self.fields[field].label = False
