from django.contrib import admin
from .models import Game, Move


# Decorator to register model admin class to the
# admin.site.register with the specific model.
@admin.register(Game)
# Model admin class
class GameAdmin(admin.ModelAdmin):
    # Var to display which fields need to be shown in the panel
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)


admin.site.register(Move)
