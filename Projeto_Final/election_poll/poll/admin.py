from django.contrib import admin
from .models import Poll, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 2

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    inlines = [OptionInline]
