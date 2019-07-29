from django.db import models
from django.urls import reverse # reverse kutuphanesi eklendi

# Create your models here.

class Post (models.Model):  # djangoda modeller class türünde tanımlanır max alan zorunlu
    title = models.CharField(max_length=120, verbose_name="Baslik")# baslik tanimlamak 
    content = models.TextField( verbose_name="Icerik")# metin kontrolü
    publishing_date = models.DateTimeField( verbose_name="Yayimlanma Tarihi",auto_now_add = True)# tarih kontrolü

    image = models.FileField(null = True, blank =True)
    
    
    def __str__(self): # kayit yapilan basliklarin ayni isimle gelmemesi icin
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
       # return "/post/{}".format(self.id) 

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    class Meta:
    	ordering = ['-publishing_date','id'] # post sıralamsını yeniden eskiye yapmak için
       
       


