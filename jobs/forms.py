from django import forms

TYPES = (
    (None, '--Please choose--'),
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),
    ('contract_work', 'Contract work')
)

DAYS = (
    ('mon', 'MON'),
    ('tue', 'TUE'),
    ('wed', 'WED'),
    ('thu', 'THU'),
    ('fri', 'FRI')
)

class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=TYPES)
    start_date = forms.DateField(help_text='The earliest date you can start working.')
    available_days = forms.MultipleChoiceField(choices=DAYS, help_text='Select all days that you can work.')
    desired_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    certify = forms.BooleanField(label='I certify that the information I have provided is true.', required=True)
