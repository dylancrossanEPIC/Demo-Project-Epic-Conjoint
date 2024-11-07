from django import forms

class CreateCourseForm(forms.Form):
    course_title = forms.CharField(max_length=200)
    course_details = forms.CharField(max_length=200)
    course_pub_date = forms.DateField(
        widget=forms.DateInput(attrs={
              'class':'form-control',
              'type': 'date'
            }
        )
    )

class UpdateCourseForm(forms.Form):
    course_title = forms.CharField(max_length=200)
    course_details = forms.CharField(max_length=200)
    course_pub_date = forms.DateField(
        widget=forms.DateInput(attrs={
              'class':'form-control',
              'type': 'date'
            }
        )
    )