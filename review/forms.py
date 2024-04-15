from django import forms

from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(max_length=100,label="Your Name")
#     review_text=forms.CharField(label="Your Review",max_length=200,widget=forms.Textarea)
#     rating=forms.IntegerField(min_value=1,max_value=5)





class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        #exclude=[]
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating",
        }
        error_messages={
            "user_name":{
                "required":"Your name must not be empty"}
        }