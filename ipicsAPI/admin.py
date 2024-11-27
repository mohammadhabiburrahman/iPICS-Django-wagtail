from django.contrib import admin
# from iPICSApi.models import TestAutoIncrement

# Register your models here.


# from wagtail.images.models import Image
# from wagtail.core.models import Site, Page
# from wagtail.documents.models import Document


from home.models import Categories,Stage, AudioArticle, VideoArticle,TextualArticle 

admin.site.register(Stage)
admin.site.register(Categories)
admin.site.register(AudioArticle)
admin.site.register(VideoArticle)
admin.site.register(TextualArticle)
# admin.site.register(Role)

# admin.site.unregister(Document)
# admin.site.unregister(Site)
# admin.site.unregister(Page)
# admin.site.unregister(Image)

