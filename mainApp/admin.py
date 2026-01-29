from django.contrib import admin
from .models import Talaba, Muallif, Kitob, Kutubxonachi, Record


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'guruh', 'kurs', 'kitob_soni')
    search_fields = ('ism', 'guruh')
    list_filter = ('kurs',)


@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 't_sana', 'kitob_soni', 'tirik')
    search_fields = ('ism',)
    list_filter = ('jins', 'tirik')


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'janr', 'sahifa', 'muallif')
    search_fields = ('nom',)
    list_filter = ('janr',)


@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'ish_vaqti')
    search_fields = ('ism',)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'talaba',
        'kitob',
        'kutubxonachi',
        'olingan_sana',
        'qaytargan_sana'
    )
    list_filter = ('olingan_sana',)
