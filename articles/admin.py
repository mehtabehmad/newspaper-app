from django.contrib import admin

from .models import Article, Comment

# Register your models here.

class CommentInline(admin.TabularInline): 
    #StackedInline -> for displaying each in individual row
    # TabularInline -> for displaying all the comments in one row.
    model = Comment
    extra = 0 # no default extra rows

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)