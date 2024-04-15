from django.db import models

# Create your models here.
class Review(models.Model):
    user_name=models.CharField(max_length=100)
    review_text=models.TextField(max_length=200)
    rating=models.IntegerField()
    CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Bad', 'Bad'),
    ]
    like = models.CharField(
        choices=CHOICES,default="Good",max_length=20
    )

    
    def __str__(self) -> str:
        return f"{self.user_name} {self.rating}"