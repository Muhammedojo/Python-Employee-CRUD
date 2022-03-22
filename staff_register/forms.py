from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ('fullname','phone','staff_code','position')
        labels = {
            'fullname' : 'Full Name',
            'staff_code' : 'Staff Code'
        }
    def __init__(self, *args, **kwargs):
        super(StaffForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"