from django.contrib import admin

# Register your models here.
from .models import Band,Member
# from .form import NameForm
admin.site.register(Band)
admin.site.register(Member)
