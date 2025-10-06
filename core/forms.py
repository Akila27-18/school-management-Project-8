from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import StudentProfile, ClassRoom, User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'classroom']
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'classroom': forms.Select(attrs={'class': 'form-select'}),
        }

    def save(self, commit=True):
        # create underlying User, then StudentProfile
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password, role=User.STUDENT)
        student = StudentProfile.objects.create(
            user=user,
            roll_number=self.cleaned_data.get('roll_number'),
            classroom=self.cleaned_data.get('classroom')
        )
        return student
