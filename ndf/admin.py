from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "average_score", "total_score", "created_at")
    readonly_fields = ("total_score", "average_score", "created_at")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("answers",)
        return self.readonly_fields
