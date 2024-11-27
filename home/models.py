
from django.db import models
import uuid

from wagtail.admin.edit_handlers import (
    FieldPanel, TabbedInterface, ObjectList)
from wagtail.search import index
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel
from django.core.validators import FileExtensionValidator
from smart_selects.db_fields import (ChainedForeignKey)
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

# import uuid

# def get_uuid_id():
#     return str(uuid.uuid4())

# class style(models.Model):
#     top = models.CharField(max_length=50, null= False, verbose_name= "Top" , default="")
#     left = models.CharField(max_length=50, null= False, verbose_name= "Left", default="")

#     def __str__(self):
#         return str(str(self.id)  + " " + self.top + " " + self.left)


def file_size(value):
    filesize = value.size

    if filesize > 499999834.112:
        raise ValidationError("You cannot upload file more than 500Mb")
    else:
        return value


def validate_file_size(value):
    filesize= value.size

    if filesize > 499999834.112:
        raise ValidationError("The maximum file size that can be uploaded is 500MB")
    else:
        return value        


class Stage(models.Model):
    stageName = models.CharField(
        max_length=50, null=False, verbose_name="Stage Name", unique=True)
    tourKey = models.CharField(
        max_length=200, null=False, verbose_name="Tour Key", default="")
    tourContent = models.CharField(
        max_length=200, null=False, verbose_name="Tour Content", default="")

    def __str__(self):
        return str(self.stageName)

    content_panels = [
        FieldPanel('stageName', classname="full"),
        FieldPanel('tourKey', classname="full"),
        FieldPanel('tourContent', classname="full"),
    ]

    promote_panels = []
    settings_panels = []

    search_fields = [
        index.SearchField('stageName',),
    ]


class Categories(models.Model):
    categoryName = models.CharField(
        max_length=50, verbose_name="Category Name", unique=True)
    stageName = models.ForeignKey(Stage, on_delete=models.SET_NULL,
                                  null=True, related_name="category", verbose_name="Stage Name")
    tourKey = models.CharField(
        max_length=200, null=False, verbose_name="Tour Key", default="")
    tourContent = models.CharField(
        max_length=200, null=False, verbose_name="Tour Content", default="")
    imgSrc = models.CharField(max_length=200, null=True,
                              blank=True, verbose_name="Img Src", default="")
    iconImg = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="icon Img", default="")

    def __str__(self):
        return str(self.categoryName)

    content_panels = [
        FieldPanel('categoryName', classname="full"),
        FieldPanel('stageName', classname="full"),
        FieldPanel('tourKey', classname="full"),
        FieldPanel('tourContent', classname="full"),
        FieldPanel('imgSrc', classname="full"),
        # FieldPanel('style', classname="full"),
    ]
    promote_panels = []
    settings_panels = []

    search_fields = [
        index.SearchField('categoryName'),
        index.SearchField('stageName'),
    ]


class Style(models.Model):
    top = models.CharField(max_length=50, null=False,
                           verbose_name="Top", default="")
    left = models.CharField(max_length=50, null=False,
                            verbose_name="Left", default="")
    categoryName = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True, related_name="style", verbose_name="Category Name")

    def __str__(self):
        return str(str(self.id) + " " + self.top + " " + self.left)


class TextualArticle(models.Model):
    stageName = models.ForeignKey(Stage, on_delete=models.CASCADE,
                                  null=False, blank=False, verbose_name="Stage Name", default=1)
    categoryName = ChainedForeignKey(
        "Categories",
        chained_field="stageName",
        chained_model_field="stageName",
        show_all=False,
        auto_choose=True, null=False, verbose_name="Category Name")
    topicName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Topic Name", default="")
    keyword = models.CharField(
        max_length=50, null=False, blank=False, default="")
    body = RichTextUploadingField(null=False, blank=False, default="")
    medlinePlusUrl = models.URLField(
        max_length=200, verbose_name="Medline Plus URL", null=True, blank=True, default="")
    summary = models.CharField(
        max_length=100, null=False, blank=False, default="", verbose_name="Description")
    comment = models.CharField(max_length=50, null=True, blank=True)
    learnMoreUrl = models.URLField(
        max_length=200, verbose_name="More URL", null=True, blank=True)
    parentTopicName = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Parent Topic Name")
    roleName = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Is Caregiver Article ?")
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.topicName)

    content_panels = [
        FieldPanel('stageName', classname="full"),
        FieldPanel('categoryName', classname="full"),
        FieldPanel('topicName', classname="full"),
        FieldPanel('keyword', classname="full"),
        FieldPanel('summary', classname="full"),
        FieldPanel('body', classname="full"),
        # FieldPanel('medlinePlusUrl', classname="full"),
        # FieldPanel('roleName', classname="full",),
        #    FieldPanel('comment', classname="full"),
        #    FieldPanel('learnMoreUrl', classname="full"),
        # FieldPanel('parentTopicName', classname="full"),

    ]

    search_field = [
        index.SearchField('topicName'),
        index.SearchField('keyword'),
        index.SearchField('parentTopicName'),
        index.SearchField('categoryName'),
        index.SearchField('roleName'),
    ]
    promote_panels = []
    settings_panels = []

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Textual Content")
        ]
    )

# validators=[FileExtensionValidator(allowed_extensions=['mp3','flac','M4A','aac']),file_size])


class AudioArticle(models.Model):
    stageName = models.ForeignKey(Stage, on_delete=models.CASCADE,
                                  null=False, blank=False, verbose_name="Stage Name", default=1)
    categoryName = ChainedForeignKey(
        "Categories",
        chained_field="stageName",
        chained_model_field="stageName",
        show_all=False,
        auto_choose=True, null=False, verbose_name="Category Name")
    topicName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Topic Name", default="")
    keyword = models.CharField(
        max_length=50, null=False, blank=False, default="")
    description = models.CharField(
        max_length=100, null=False, blank=False, default="")
    audio = models.FileField(max_length=200, verbose_name="AUDIO (Max file size can be 500MB) & allowed format ('mp3','flac','wav')", null=False, blank=False, default="", validators=[
                             FileExtensionValidator(allowed_extensions=[ 'mp3','flac','wav'])])
#    audio = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['mp3', 'flac' ],max_upload_size=10485760,blank=False, null=False, default="")
#    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp3','webm','mkv','flac'])])
    parentTopicName = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Parent Topic Name")
#    category_name = models.ForeignKey(Categories, on_delete=models.SET_NULL, null= True)
    roleName = models.BooleanField(
        null=False, default=False, verbose_name="Is Caregiver Article ?")
    uid = uid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)
#    handout = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['video/x-msvideo', 'video/mp4', 'audio/mpeg', ],max_upload_size=10485760,blank=True, null=True)

    def __str__(self):
        return str(self.topicName)

    def clean(self):
        if self.audio.size > 499999834.112:
            raise ValidationError("The maximum file size that can be uploaded is 500MB")  

    content_panels = [
        FieldPanel('stageName', classname="full"),
        FieldPanel('categoryName', classname="full"),
        FieldPanel('topicName', classname="full"),
        FieldPanel('keyword', classname="full"),
        FieldPanel('description', classname="full"),
        FieldPanel('audio'),
        FieldPanel('parentTopicName', classname="full"),
        # FieldPanel('roleName', classname="full"),

    ]

    search_field = [
        index.SearchField('topicName'),
        index.SearchField('keyword'),
        index.SearchField('parentTopicName'),
        index.SearchField('categoryName'),
        index.SearchField('roleName'),
    ]
    promote_panels = []
    settings_panels = []

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Audio Content")
        ]
    )

# , validators=[FileExtensionValidator(allowed_extensions=['mp4','MOV','avi','mkv','wmv','avi']),file_size(204800)]


class VideoArticle(models.Model):
    stageName = models.ForeignKey(
        Stage, on_delete=models.CASCADE, null=False, verbose_name="Stage Name", default=1)
    categoryName = ChainedForeignKey(
        "Categories",
        chained_field="stageName",
        chained_model_field="stageName",
        show_all=False,
        auto_choose=True, null=False, verbose_name="Category Name")
    topicName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Topic Name", default="")
    keyword = models.CharField(
        max_length=50, null=False, blank=False, default="")
    description = models.CharField(
        max_length=100, null=False, blank=False, default="")

    video = models.FileField(max_length=200, verbose_name="VIDEO (Max file size can be 500MB) & allowed format ('MOV','mp4','webm','flac')", blank=False, default="", validators= [FileExtensionValidator(allowed_extensions=['MOV','mp4','webm','flac'])])
    # video = ContentTypeRestrictedFileField(
    #     content_types=['application/pdf', 'video/mp4'],
    #     max_upload_size="5242880")
#    video = models.FileField(max_length=200, null= False, blank=False, default="", validators= [FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','flac']), file_size])
#    video = models.FileField(max_length=100, null= True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','flac'])])
    parentTopicName = models.ForeignKey('self', on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name="Parent Topic Name", default="")
#    category_name = models.ForeignKey(Categories, on_delete=models.SET_NULL, null= True)
    roleName = models.BooleanField(
        null=False, default=True, verbose_name="Is Caregiver Article ?")
    uid = uid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.topicName)


    def clean(self):
        if self.video.size > 499999834.112:
            raise ValidationError("The maximum file size that can be uploaded is 500MB")  

    content_panels = [
        FieldPanel('stageName', classname="full"),
        FieldPanel('categoryName', classname="full"),
        FieldPanel('topicName', classname="full"),
        FieldPanel('keyword', classname="full"),
        FieldPanel('description', classname="full"),
        FieldPanel('video', classname="full"),
        FieldPanel('parentTopicName', classname="full"),
        # FieldPanel('roleName', classname="full")

    ]

    search_field = [
        index.SearchField('topicName'),
        index.SearchField('keyword'),
        index.SearchField('parentTopicName'),
        index.SearchField('categoryName'),
        index.SearchField('roleName'),
    ]
    promote_panels = []
    settings_panels = []

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Video Content")
        ]
    )



# class Greeting(models.Model):
#     audio_file = models.FileField(upload_to='greetings/')
#     description = models.CharField(max_length=128, null=True, blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     content_panels = [
#         FieldPanel('description', classname="full"),
#         # FieldPanel('description', classname="full"),
#     ]

# from django.db import models
# from wagtail.documents.models import AbstractDocument
# from wagtail.admin.edit_handlers import FieldPanel
# # Create your models here.
# class LargeDocument(AbstractDocument):

#     admin_form_fields = (
#         'file',
#     )
#     panels = [
#         FieldPanel('file', classname='fn'),
#     ]
