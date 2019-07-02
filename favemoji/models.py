from django.db import models


class EmojiInfo(models.Model):
    infoEmoji = models.CharField(max_length=100)
  # info输入串 = models.CharField(max_length=200)
    infoUnicode = models.CharField(max_length=200, default='0')

    def __str__(self):
        return self.infoUnicode
    
  

class FavEmoji(models.Model):
    infoEmoji = models.CharField(max_length=100)
    info输入串 = models.CharField(max_length=200)
    infoUnicode = models.CharField(max_length=200, default='0')
    
    def __str__(self):
        return self.info输入串