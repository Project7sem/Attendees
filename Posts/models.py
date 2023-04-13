from django.db import models
from Account.models import User
# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    caption = models.TextField()
    images = models.ImageField(upload_to="Posts/User/", height_field=420, width_field=420, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True, blank=True)
    comment = models.ForeignKey('Comments', related_name='comments', on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.caption


class Comments(models.Model):
    user = models.ForeignKey(User, related_name="commented_by", on_delete=models.CASCADE)
    text =models.TextField()
    
    def __str__(self):
        return self.user + "comment"



