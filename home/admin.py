from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display =("user","slug","created")
    search_fields = ("slug",)
    list_filter = ("updated",)
    raw_id_fields = ("user",)
    prepopulated_fields = {"slug":("body",)}