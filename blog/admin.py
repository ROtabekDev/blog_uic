from django import forms
from django.contrib import admin


from .models import (
    Article, Author, Category,
    Comment, Tag, Profession, Social_network_profile, 
    Social_network_type, Subscriber, Message
)

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'views_count')
    form = ArticleAdminForm 

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profession)
admin.site.register(Social_network_profile)
admin.site.register(Social_network_type)
admin.site.register(Subscriber)
admin.site.register(Message)