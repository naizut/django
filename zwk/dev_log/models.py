from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
# class BugRecord(models.Model):
# 	body = models.TextField()
# 	publish = models.DateTimeField(default=timezone.now)

# 	class Meta:
# 		ordering = ("-publish",)

class Tutorial(models.Model):
	title = models.CharField(max_length=200)
	publish = models.DateTimeField(default=timezone.now)
	tag = models.TextField()
	category = models.TextField()
	resume = models.TextField()
	body = RichTextUploadingField()
	language = models.TextField()
	users_like = models.ManyToManyField(User, related_name='codinglikes', blank=True)

	class Meta:
		ordering = ("-publish",)

	def __str__(self):
		return self.title

class devlogComments(models.Model):
	diaries = models.ForeignKey(Tutorial, related_name="comments")
	commentator = models.CharField(max_length=80)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return "Comment by {0} on {1}".format(self.commentator, self.diaries)