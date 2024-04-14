from django import forms

class ReviewForm(forms.Form):
    user_name=forms.CharField(max_length=100,label="Your Name-")
    review_text=forms.CharField(label="Your Review-",max_length=200,widget=forms.Textarea)
    rating=forms.IntegerField(min_value=1,max_value=5)