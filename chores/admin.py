from django.contrib import admin
from chores.models import Chores, Category, History, Score, Rewards, UserPreferences

class ChoreAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class HistoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


class ScoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


class RewardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {}


class UserPreferencesAdmin(admin.ModelAdmin):
    prepopulated_fields = {}



admin.site.register(Chores, ChoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Rewards, RewardsAdmin)
admin.site.register(UserPreferences, UserPreferencesAdmin)
