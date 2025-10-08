from django.db import models

class Task(models.Model):
	task_name = models.CharField(max_length = 50)
	task_description = models.CharField(max_length = 200)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.task_name