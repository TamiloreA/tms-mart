from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=300)
    password = models.CharField(max_length=400)



    def __str__(self):
        return f"{self.name}  { self.password } "


def image(instance, filename):
    return 'uploads/{}/{}'.format(instance.title, filename)


'''The Post model '''
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(max_length=400)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


