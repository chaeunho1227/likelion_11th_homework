from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
