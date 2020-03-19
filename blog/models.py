import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField('названии статьи', max_length = 200)
	text = models.TextField('текст статьи')
	published_date = models.DateTimeField('Дата публикации')

	def publish(self):
		self.published_date = timezone.now() 
		self.save() 

	def __str__(self):
		return self.title
