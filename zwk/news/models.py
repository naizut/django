from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	resume = models.TextField()
	body = RichTextUploadingField()
	publish = models.DateTimeField(default=timezone.now)
	users_like = models.ManyToManyField(User, related_name='news_like', blank=True)

	class Meta:
		ordering = ("-publish",)

	def __str__(self):
		return self.title

class Comment(models.Model):
    article = models.ForeignKey(News, related_name="comments")
    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "Comment by {0} on {1}".format(self.commentator, self.article)


