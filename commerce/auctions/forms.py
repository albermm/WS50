from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.views.generic import CreateView
from django.forms import ModelForm

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('title', 'username', 'body',)

        widget = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }



class NewListingForm(forms.ModelForm):
    
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
    startingbid = forms.IntegerField(
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

    def __init__(self, *args, **kwargs):
        super(NewListingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.form_id = 'id-NewListingForm'
        self.helper.form_class = 'NewListingForm'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Listing', css_class='btn btn-primary'))

    class Meta:
        model = Listings
        fields = ['title', 'description', 'startingbid', 'image', 'category']


class NewBidForm(forms.ModelForm):
    
    bid_amount= forms.IntegerField(
        label= "Add your bid",
        help_text= "It must be higher than the exisitng one",
        required=True,
    )

    class Meta:
        model = Bids
        fields = ['amount', 'listing', 'username']

    def __init__(self, *args, **kwargs):
        super(NewBidForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.form_id = 'id-NewBidForm'
        self.helper.form_class = 'NewBidForm'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Bid', css_class='btn btn-primary')) 