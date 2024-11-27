from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import ( Stage, Categories, TextualArticle, AudioArticle, VideoArticle, Style)

from wagtail.core import hooks
# from django.template.defaultfilters import truncatewords



@hooks.register('construct_main_menu')
def hide_explorer_items_from_users(request, menu_items):
        # if request.user.groups.filter(name__in=["iPICS-Admin",]):
            menu_items[::] = [
                item for item in menu_items if item.name not in ['reports']
            ]

class StageAdmin(ModelAdmin):
    model = Stage
    menu_label = 'Stage'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder'  # change as required
    list_display = ('stageName',)
    list_filter = ('stageName',)
    search_fields = ('stageName',)


class CategoriesAdmin(ModelAdmin):
    model = Categories
    menu_label = 'Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder'  # change as required
    list_display = ('categoryName', 'stageName')
    list_filter = ('categoryName',)
    search_fields = ('categoryName',)


class TextualArticleAdmin(ModelAdmin):
    model = TextualArticle
    menu_label = 'Textual Article'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full'  # change as required
    list_display = ('topicName', 'categoryName',) # 'medlinePlusUrl','learnMoreUrl','parentTopicName',
    list_filter = ('categoryName',) #  'keyword','parentTopicName', 'topicName',
    search_fields = ('topicName',) # 'keyword','parentTopicName',



class AudioArticleAdmin(ModelAdmin):
    model = AudioArticle
    menu_label = 'Audio Article'  # ditch this to use verbose_name_plural from model
    menu_icon = 'media'  # change as required
    list_display = ('topicName','categoryName',) # 'audio', 'keyword','parentTopicName',
    list_filter = ('categoryName',) # 'audio', 'keyword','parentTopicName',
    search_fields = ('topicName',) # 'audio', 'keyword','parentTopicName',


class VideoArticleAdmin(ModelAdmin):
    model = VideoArticle
    menu_label = 'Video Article'  # ditch this to use verbose_name_plural from model
    menu_icon = 'media'  # change as required
    list_display = ('topicName','categoryName',) # 'video', 'keyword','parentTopicName',
    list_filter = ('categoryName',) # 'video', 'keyword','parentTopicName',
    search_fields = ('topicName',) # 'video', 'keyword','parentTopicName',

class StyleAdmin(ModelAdmin):
    model = Style
    menu_label = 'Style'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder'  # change as required
    list_display = ('top', 'left')


modeladmin_register(StageAdmin)
modeladmin_register(CategoriesAdmin)
modeladmin_register(TextualArticleAdmin)
modeladmin_register(AudioArticleAdmin)
modeladmin_register(VideoArticleAdmin)
modeladmin_register(StyleAdmin)
# modeladmin_register(RoleAdmin)

