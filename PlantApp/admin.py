from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from UserApp.models import RUser
from .models import Plant, DiseaseDetection
from DemandeTraitement.models import DemandeTraitement


# Register the CustomUser model using the built-in UserAdmin
admin.site.register(RUser, UserAdmin)

# Register the Plant and DiseaseDetection models
admin.site.register(Plant)
admin.site.register(DiseaseDetection)
admin.site.register(DemandeTraitement)