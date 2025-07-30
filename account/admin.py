from django.contrib import admin
from .models import Member
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ( 'full_name', 'email')
    search_fields = ( 'full_name', 'email')
    list_filter = ('date_joined',)
    ordering = ("-date_joined",)

    


    