from django.db import models
from django.urls import reverse
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
    