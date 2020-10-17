from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.views.generic import CreateView
from django.forms import ModelForm

from .models import User, Listings


class addForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = [
            'title',
            'description',
            'startingbid',
            'image',
            'category'
        
        ]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout()
            self.helper.form_id = 'id-addForm'
            self.helper.form_class = 'addForm'
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
            

'''
title= forms.CharField(
            label= "Insert title for your listing",
            help_text= "Title",
            max_length= 64,
            required=True,
        )
        description = forms.CharField(
            label= "Describe your item",
            help_text= "Item description",
            max_length= 500,
            required=True,
        )
        bid = forms.IntegerField(
            label = "Starting bid",
            initial= 0,
            required=True,
        )
        image = forms.CharField(
            label= "url for your image",
            required=False,
        )
        category = forms.CharField(
            label= "Category",
            required=True,
            max_length=64,

        )
'''