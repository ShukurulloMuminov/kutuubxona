from django.contrib import admin
from .models import *

class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'guruh', 'kurs', 'kitob_soni')
    list_display_links = ('id', 'ism')
    list_filter = ('guruh', 'kurs')
    list_editable = ('kurs', 'kitob_soni')

    search_help_text = "Ism bo'yicha qidiring!"
    search_fields = ('ism',)



class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 't_sana', 'kitob_soni', 'tirik')
    list_display_links = ('id', 'ism')
    list_editable = ('kitob_soni', 'tirik',)
    inlines = (KitobInline,)

    search_fields = ('ism',)

    list_filter = ( 'tirik',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('talaba', 'olingan_sana', 'qaytargan_sana', 'kutubxonachi', 'kitob')
    search_fields = ('talaba__ism', 'kutubxonachi__ism', 'kitob__nom')
    search_help_text = "Ism bo'yicha qidiring!"
    date_hierarchy = 'qaytargan_sana'


class KitobAdmin(admin.ModelAdmin):
    list_display = ('nom', 'janr', 'sahifa', 'muallif')
    search_fields = ('nom',)


class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'ish_vaqti')
    search_fields = ('ism',)
    list_filter = ('ish_vaqti',)


admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Kitob, KitobAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Record, RecordAdmin)