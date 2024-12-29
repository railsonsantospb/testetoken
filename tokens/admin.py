from django.contrib import admin
from .models import CustomToken
from django.utils import timezone

@admin.register(CustomToken)
class CustomTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created', 'expires', 'is_active', 'is_expired')
    list_filter = ('is_active', 'created', 'expires')
    search_fields = ('user__username', 'description')
    readonly_fields = ('key', 'created')
    
    def is_expired(self, obj):
        return obj.expires <= timezone.now()
    is_expired.boolean = True
    is_expired.short_description = 'Expired'

    actions = ['invalidate_tokens']

    def invalidate_tokens(self, request, queryset):
        queryset.update(is_active=False)
    invalidate_tokens.short_description = "Invalidate selected tokens"
