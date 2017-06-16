from django.contrib import admin
from firstapp.models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(UserProfile)

