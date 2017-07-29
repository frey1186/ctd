from django.contrib import admin
from app01 import models

# Register your models here.



admin.site.register(models.Process)
admin.site.register(models.TechContent)
admin.site.register(models.UserProfile)
admin.site.register(models.TechTemplate)
admin.site.register(models.PartTemplate)
admin.site.register(models.SubmitFile)
