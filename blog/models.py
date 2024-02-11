from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from tinymce import models as tm

User = get_user_model()


class Category(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=100, unique=True)
    total_post = models.IntegerField(verbose_name="total posts", default=0)

    class Meta:
        ordering = ("-total_post", "-id")
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category_details", kwargs={"pk": self.pk})


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(posted=True)


class Article(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="article"
    )
    topic = models.CharField(max_length=255, unique=True)
    body = tm.HTMLField()
    posted = models.BooleanField(default=False)
    thumbnail = models.FileField(
        default="media/profile/default.jpg",
        null=True,
        blank=True,
        max_length=500,
    )
    slug = AutoSlugField(
        populate_from="topic",
        blank=True,
        null=True,
        unique=True,
        always_update=True,
        default=None,
        unique_with=["author"],
    )
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    objects = models.Manager()
    articles = ArticleManager()

    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail
        else:
            return "#"

    def save(self, *args, **kwargs):
        if self.created_on is None and self.posted:
            self.created_on = timezone.now()

        if self.created_on:
            self.updated_on = timezone.now()

        if not self.pk and self.category is not None:
            self.category.total_post += 1
            self.category.save()

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ("-id", "updated_on")
        verbose_name_plural = "articles"

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("blog:article_details", kwargs={"slug": self.slug})
