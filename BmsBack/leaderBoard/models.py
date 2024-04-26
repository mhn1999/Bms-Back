from django.db import models

class LeaderBoardMember(models.Model):
  playerId= models.BigAutoField(primary_key=True)
  phoneNumber= models.CharField(max_length=14)
  numberOfConsumedLives= models.IntegerField()
  playerLastLevel= models.IntegerField()
  playTime = models.FloatField()