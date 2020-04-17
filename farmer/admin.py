from django.contrib import admin
from .models import Farmer,Merchandiser,Schemes,LatestPost
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Merchandiser)
admin.site.register(Schemes)
admin.site.register(LatestPost)