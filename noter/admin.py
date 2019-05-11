from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ( 'id',
    'user', 'shorttext', 'created', 'edited', 'deleted', 'locked', 'protected')
    list_display_links = ('shorttext',)
    search_fields = ("text", "shorttext")

admin.site.register(Note, NoteAdmin)
