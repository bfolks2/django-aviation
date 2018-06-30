from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'home_airport')
    search_fields = ['user__username', 'home_airport__name']


admin.site.register(Member, MemberAdmin)
