from django import forms 
from .models import AssignCourse

class AssignCourseForm(froms.ModelForm):
    class Meta:
        model = AssignCourse
        fields = ('__all__')
        