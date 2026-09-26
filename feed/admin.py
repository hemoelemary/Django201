from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    #here you can filter what you want to access
    pass

admin.site.register(Post,PostAdmin)