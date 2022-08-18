from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/blog/<title>/<filename>
    return f'blog/{instance.title}/{filename}'


class Post(models.Model):

    class PostObjects(models.Manager):
        # Filter the post by status
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        upload_to=user_directory_path, default='default.jpg', blank=True, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(
        max_length=255, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_user')

    # Give the option to publish or draft the post
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postobjects = PostObjects()

    # Ordering the posts by published date
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title
