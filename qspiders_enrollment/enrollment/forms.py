# enrollment/forms.py
from django import forms
from .models import Student, Course

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'selected_course', 'has_paid_fees']

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)

        # Add specific choices for selected_course
        specific_courses = ['Full Stack Python', 'Full Stack Java', 'Software Testing']
        self.fields['selected_course'].queryset = Course.objects.filter(name__in=specific_courses)

        self.fields['selected_course'].widget.attrs.update({'class': 'select2'})

        # Use a single checkbox for has_paid_fees
        self.fields['has_paid_fees'].widget = forms.CheckboxInput(attrs={'class': 'checkbox-label'})
