from django import forms
from .models import Profile, BlogPost
import re   # keep this

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image')
        widgets = {
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell something about yourself...'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook profile link'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram profile link'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn profile link'}),
        }

    def clean_phone_no(self):
        phone = self.cleaned_data.get('phone_no')
        if phone and not re.fullmatch(r'\d{10}', str(phone)):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone

    def clean_bio(self):
        bio = self.cleaned_data.get('bio', '')
        if any(word in bio.lower() for word in ["http://", "https://", "www."]):
            raise forms.ValidationError("Bio must contain text only, links are not allowed.")
        return bio

    def clean_facebook(self):
        fb = self.cleaned_data.get('facebook')
        if fb and not fb.startswith(("http://", "https://")):
            raise forms.ValidationError("Enter a valid link starting with http:// or https://")
        return fb

    def clean_instagram(self):
        ig = self.cleaned_data.get('instagram')
        if ig and not ig.startswith(("http://", "https://")):
            raise forms.ValidationError("Enter a valid link starting with http:// or https://")
        return ig

    def clean_linkedin(self):
        ln = self.cleaned_data.get('linkedin')
        if ln and not ln.startswith(("http://", "https://")):
            raise forms.ValidationError("Enter a valid link starting with http:// or https://")
        return ln


# ✅ BlogPostForm MUST be OUTSIDE ProfileForm
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug-for-blog'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
        }
