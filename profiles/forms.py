from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and class, remove auto-generated labels and set autofocus on first field """
        # Careful placing an extra (self)
        super().__init__(*args, **kwargs)
        placeholders = {
            # 'full_name': 'Full Name',
            # 'email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_postcode': 'Post Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, state or locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field !='default_country':
                placeholder = f'{ placeholders[field] }*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # self.fields[field].label = False
