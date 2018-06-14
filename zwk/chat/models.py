from django.db import models

# Create your models here.

class Chat(models.Model):
    chatter = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ('-created', )

    def __str__(self):
        return "Message by {0} on {1}".format(self.chatter, self.body)
