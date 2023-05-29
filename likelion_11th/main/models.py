from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False,blank=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
    

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title+" : "+self.content[:20]