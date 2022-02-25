
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# class PostManager(models.Manager):


#     def yea(self,year):

#         return self.filter(publish__year=year)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
        # manager baraye publish hastesh le beshe Post.pulished.all() nvsht
        #objects default ham sarec jashe post.objects.all()
        


    

class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
        
    )

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=10,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10 ,choices=STATUS_CHOICES,default='draft')
    objects=models.Manager()
    published=PublishedManager()
    
    # objects=PostManager()

    def get_absolute_url(self):

        return reverse('blog:postdetail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

    

    class Meta:
        ordering=('-publish',)
    
    def __str__(self):
        return self.title

    
