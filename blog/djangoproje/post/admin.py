from django.contrib import admin
from .models import Post # ilk once import ediyoruz
# from post.models import Post    2.yol
# Register your models here.


class PostAdmin(admin.ModelAdmin): # admin panaleinde post kısmından tarıh saat yazacak
    
    list_display = ['title','publishing_date']
    list_display_links = ['publishing_date'] # bu başlıklarada link verdik
    list_filter = ['publishing_date'] # fltreleme ozelligi
    search_fields = ['title','content']
    list_editable = ['title']
    
    class Meta:
        
        model = Post


admin.site.register(Post, PostAdmin) # admin paneline bağlama