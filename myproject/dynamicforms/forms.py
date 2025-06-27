from django import forms
from .models import Catagory, InformationForm


class DataForm(forms.ModelForm):
    class Meta:
        model = InformationForm
        fields = [
            'title',
            'message',
            'email',
            'dropdown',
            'checkbox',
            'radio_option',
            'terms',
        ]


    def __init__(self,*args,**kwargs):
        super(DataForm,self).__init__(*args,**kwargs)

        
        catagroies = Catagory.objects.filter(is_active=True)
        cat_choices = [(str(cat.id), cat.name) for cat in catagroies]

        #  Checkbox (multiple choices)

        self.fields['dropdown'] = forms.ChoiceField(
            choices=cat_choices,
            widget=forms.Select(attrs={'style': 'width: 100px;'})
        )
        
        #  Radio (single choice)

        self.fields['radio_option'] = forms.ChoiceField(
            choices=cat_choices,
            widget=forms.RadioSelect
        )
       

         #  Checkbox (multiple choices)

        self.fields['checkbox'] = forms.MultipleChoiceField(
            choices=cat_choices,
            widget=forms.CheckboxSelectMultiple
        )
        
        

        # for Textarea
        
        self.fields['message'] = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Enter your message here'})
    )
