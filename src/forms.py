from django import forms  
from .models import StudentRegistration 


class StudentForm(forms.ModelForm):  
    """this form class is use to take input from the user
    and store the data after validate and save into database.
    """
    class Meta:  
        model = StudentRegistration  
        fields = ['student_name', 'student_dob', 'student_gender','student_address','student_email','student_phone']
        widgets = { 'student_name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'student_dob': forms.TextInput(attrs={ 'class': 'form-control' }),
            'student_gender': forms.TextInput(attrs={ 'class': 'form-control' }),
            'student_address':forms.TextInput(attrs={ 'class': 'form-control' }),
            'student_email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'student_phone': forms.TextInput(attrs={ 'class': 'form-control' }),
      }