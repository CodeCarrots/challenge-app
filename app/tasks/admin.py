from django.contrib import admin

from .models import UnlockedKey
# Register your models here.

class UnlockedKeyAdmin(admin.ModelAdmin):
    readonly_fields = ('ts',)
    list_display = ('user', 'key', 'ts')


admin.site.register(UnlockedKey, UnlockedKeyAdmin)
