
from rest_framework import serializers
from home.models import Stage , Categories , TextualArticle, AudioArticle, VideoArticle, Style

class StagesSerializer(serializers.ModelSerializer):
    # stageName = serializers.CharField(source="stageName")
    class Meta:
        model = Stage
        fields = ['id','stageName']

# class StyleSerializer(serializers.ModelSerializer):
#     # stageName = serializers.CharField(source="stageName")
#     class Meta:
#         model = style
#         fields = ['top' ,'left']       

class CategorySerializer(serializers.ModelSerializer):
    # stageName = serializers.RelatedField(source='Stage', read_only = True)
    # stags = StagesSerializer(many=True, read_only = True)
    # stageName = serializers.CharField(source="stage_name")
    # categoryName = serializers.CharField(source="category_name")
    class Meta:
        model = Categories
        fields =['id','stageName', 'categoryName']

class TextualArticleSerializer(serializers.ModelSerializer):
    # stageName = serializers.CharField(source="stage_name")
    # categoryName = serializers.CharField(source="category_name")
    # topicName = serializers.CharField(source="topic_name")
    # medlinePlusUrl = serializers.CharField(source="medline_plus_url")
    # learnMoreUrl = serializers.CharField(source="learn_more_url")
    # parentTopicName = serializers.CharField(source="parent_topic_name")
    # roleName = serializers.CharField(source="role_name")
    class Meta:
        model = TextualArticle
        fields = ['id','stageName','topicName','keyword','body','medlinePlusUrl','summary','comment','learnMoreUrl','parentTopicName', 'categoryName','roleName','uid',]

class AudioArticleSerializer(serializers.ModelSerializer):
    # stageName = serializers.CharField(source="stage_name")
    # categoryName = serializers.CharField(source="category_name")
    # topicName = serializers.CharField(source="topic_name")
    # parentTopicName = serializers.CharField(source="parent_topic_name")
    # roleName = serializers.CharField(source="role_name")
    class Meta:
        model = AudioArticle
        fields = ['id', 'stageName','topicName','keyword', 'description', 'audio','parentTopicName', 'categoryName', 'roleName','uid',]

class VideoArticleSerializer(serializers.ModelSerializer):
    # stageName = serializers.CharField(source="stage_name")
    # categoryName = serializers.CharField(source="category_name")
    # topicName = serializers.CharField(source="topic_name")
    # parentTopicName = serializers.CharField(source="parent_topic_name")
    # roleName = serializers.CharField(source="role_name")
    class Meta:
        model = VideoArticle
        fields = ['id', 'stageName','topicName','keyword','description','video','parentTopicName', 'categoryName', 'roleName','uid',]

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['top', 'left']

class CategorySerializerNew(serializers.ModelSerializer):
    style = StyleSerializer(many = True , read_only =True)
    # style = serializers.StringRelatedField(source='Style', read_only = True)
    # stags = StagesSerializer(many=True, read_only = True)
    # stageName = serializers.CharField(source="stage_name")
    label = serializers.CharField(source="categoryName")
    class Meta:
        model = Categories
        fields =['id','label' , "tourKey", "tourContent", 'imgSrc', 'style','iconImg']

class StageSerializerNew(serializers.ModelSerializer):
    category = CategorySerializerNew(many=True, read_only = True)
    # style = serializers.StringRelatedField(source='Style', read_only = True)
    # style = StyleSerializer(many = True , read_only =True)
    # id = serializers.RelatedField(source='Categories', read_only = True)
    # cat = CategorySerializer(many=True, read_only = True)

    class Meta:
        model = Stage
        fields = ["id", "stageName", "tourKey", "tourContent", "category",]

