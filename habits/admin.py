from django.contrib import admin
from .models import Habit


class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'place', 'time', 'action', 'nice_habit', 'is_public')
    list_filter = ('user', 'nice_habit', 'is_public')
    search_fields = ('name', 'user__username', 'place', 'action')


admin.site.register(Habit, HabitAdmin)
