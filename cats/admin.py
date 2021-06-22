from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db.models import Count
from .models import *

@admin.register(Species)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("jmeno_druhu", "pocet_druhu")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            celkove=Count("jmeno_druhu", distinct=True),
        )
        return queryset

    def pocet_druhu(self, obj):
        return obj.celkove

    pocet_druhu.admin_order_field = "celkove"
    pocet_druhu.short_description = "Počet druhů"


@admin.register(Description_of_the_cat)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "vek", "vaha", "popisek", "pocet_kocek")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            celkove=Count("jmeno", distinct=True),
        )
        return queryset

    def pocet_kocek(self, obj):
        return obj.celkove

    pocet_kocek.admin_order_field = "celkove"
    pocet_kocek.short_description = "Počet koček"

@admin.register(Photo)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("nazev_fotky","fotka","popisek_fotky", "filesize")
