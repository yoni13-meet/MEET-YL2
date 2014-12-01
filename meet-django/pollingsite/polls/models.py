from django.db import models

class Question (models.Model):
	question = models.CharField(max_length = 200)

class Answer (models.Model):
	ans = models.CharField(max_length = 50)
	votes = models.IntegerField(default = 0)
	polls = models.ForeignKey(Question)