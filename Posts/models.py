from django.db import models
from Account.models import User
from django.core.exceptions import ValidationError


   



# Create your models here.



class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    caption = models.TextField()
    images = models.ImageField(upload_to="Posts/User/", null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes")


    
    def __str__(self):
        return self.caption

class Comments(models.Model):
    user = models.ForeignKey(User, related_name="commented_by", on_delete=models.CASCADE)
    text =models.TextField()
    post = models.ForeignKey(BlogPost, related_name='posts', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.user) + " - comment"






