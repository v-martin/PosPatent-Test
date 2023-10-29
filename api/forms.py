from django import forms


class SearchForm(forms.BaseForm):
    registration_number = forms.IntegerField(null=True)
    registration_date = forms.IntegerField(null=True)
    application_number = forms.IntegerField(null=True)
    application_date = forms.IntegerField(null=True)
    authors = forms.CharField(max_length=255, null=True)
    authors_count = forms.IntegerField(null=True)
    right_holders = forms.CharField(max_length=255, null=True)
    contact_to_third_parties = forms.CharField(max_length=255, null=True)
    program_name = forms.CharField(max_length=255, null=True)
    creation_year = forms.IntegerField(null=True)
    registration_publish_date = forms.IntegerField(null=True)
    registration_publish_number = forms.IntegerField(null=True)
    actual = forms.BooleanField()
    publication_url = forms.URLField(null=True)
