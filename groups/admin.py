from django.contrib import admin
from . import models

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline,]

admin.site.register(models.Group, GroupAdmin)
