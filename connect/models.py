from django.db import models




class OpenUserInfo(models.Model):
    _id = models.IntegerField() 
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    tel_num = models.CharField(max_length = 50)
    about = models.TextField(help_text="Описание")
    time_reg = models.CharField(max_length = 50) 

    def __str__(self):
        return self.first_name




class Bulletion(models.Model):
    _id1 = models.IntegerField() 
    title = models.CharField(max_length = 50, help_text="Название работ")
    price = models.IntegerField(help_text="Цена услуги")
    countru = models.CharField(max_length = 15 , help_text="Страна")
    citi = models.CharField(max_length = 15 , help_text="Город")
    subway_ststion = models.CharField(max_length = 15 , help_text="Город")
    images_url = [models.CharField(max_length=200)]*5
    agent_info = OpenUserInfo 
    description = models.TextField(help_text="Описание")
        
    def __str__(self):
        return self.title




