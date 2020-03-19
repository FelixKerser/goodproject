import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

class Info(models.Model):
	name = models.CharField('Название заголовка', max_length = 200)
	information = models.TextField('Информация')
	last_upd = models.DateTimeField('Последняя дата обновлении')

	def __str__(self):
		return self.information

	def publish(self):
		return self.last_upd >= (timezone.now() - datetime.timedelta(days= 1))