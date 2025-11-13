from django.contrib import admin
from .models import Member
# Register your models here.
# remember the admin is a crud method if you want to include members then you shall create it here,see the code bellow
#if you wanna manipulate the design better to utilize admin.py
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
#I see this is riht
admin.site.register(Member, MemberAdmin)