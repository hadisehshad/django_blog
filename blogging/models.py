from django.db import models
from account.models import User



# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200, help_text="عنوان")
    content = models.TextField(help_text="محتوا")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", help_text="نویسنده")
    created_at = models.DateTimeField(auto_now_add=True, help_text="تاریخ ایجاد")
    image = models.ImageField(upload_to="posts/", help_text="تصویر")

    def __str__(self):
        return f"{self.title} - {self.author}"


