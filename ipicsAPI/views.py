from json import JSONEncoder
from typing import Generic
from urllib import response
from django.http import Http404
from django.shortcuts import render
from requests import request
from rest_framework import viewsets
from .serializers import AudioArticleSerializer, StagesSerializer, CategorySerializer, TextualArticleSerializer, VideoArticleSerializer, StageSerializerNew
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from home.models import AudioArticle, Categories, Stage, TextualArticle, VideoArticle
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


class StagesViewSet(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StagesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    # swagger_schema = None
    # permission_classes = (IsAuthenticated,)


class CategoryViewSet(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'stageName']


class TextualArticleViewSet(generics.ListAPIView):
    queryset = TextualArticle.objects.all()
    serializer_class = TextualArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'parentTopicName',
                        'categoryName', 'roleName', 'summary', 'uid', ]

    @csrf_exempt
    def PrenNextTextualArticleViewMethod(request, id):
        """
        Return single previous object and next object
        """
        if request.method == 'GET':
            try:
                article = TextualArticle.objects.filter(id=id)
                for i in article:
                    stage_id = i.stageName_id
                    category_id = i.categoryName_id
            except:
                article = None
            try:
                pre_article = TextualArticle.objects.filter(id__lt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('-id')

                serializer = TextualArticleSerializer(pre_article, many=True)
                pre_article = serializer.data[0]
            except:
                pre_article = None

            try:
                next_article = TextualArticle.objects.filter(id__gt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('id')
                serializer = TextualArticleSerializer(next_article, many=True)
                next_article = serializer.data[0]
            except:
                next_article = None

            data_list = []
            data_list.append(pre_article)
            data_list.append(next_article)
            return JsonResponse(data_list, safe=False)


class AudioArticleViewSet(generics.ListAPIView):
    queryset = AudioArticle.objects.all()
    serializer_class = AudioArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'parentTopicName',
                        'categoryName', 'roleName', 'description', 'uid', ]
    
    @csrf_exempt
    def PrenNextAudioArticleViewMethod(request, id):
        """
        Return single previous object and next object
        """
        if request.method == 'GET':
            try:
                article = AudioArticle.objects.filter(id=id)
                for i in article:
                    stage_id = i.stageName_id
                    category_id = i.categoryName_id
            except:
                article = None
            try:
                pre_article = AudioArticle.objects.filter(id__lt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('-id')

                serializer = AudioArticleSerializer(pre_article, many=True)
                pre_article = serializer.data[0]
            except:
                pre_article = None

            try:
                next_article = AudioArticle.objects.filter(id__gt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('id')
                serializer = AudioArticleSerializer(next_article, many=True)
                next_article = serializer.data[0]
            except:
                next_article = None

            data_list = []
            data_list.append(pre_article)
            data_list.append(next_article)
            return JsonResponse(data_list, safe=False)

class VideoArticleViewSet(generics.ListAPIView):
    queryset = VideoArticle.objects.all()
    serializer_class = VideoArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'parentTopicName',
                        'categoryName', 'roleName', 'description', 'uid', ]

    

    @csrf_exempt
    def PrenNextVideoArticleViewMethod(request, id):
        """
        Return single previous object and next object
        """
        if request.method == 'GET':
            try:
                article = VideoArticle.objects.filter(id=id)
                for i in article:
                    stage_id = i.stageName_id
                    category_id = i.categoryName_id
            except:
                article = None
            try:
                pre_article = VideoArticle.objects.filter(id__lt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('-id')

                serializer = VideoArticleSerializer(pre_article, many=True)
                pre_article = serializer.data[0]
            except:
                pre_article = None

            try:
                next_article = VideoArticle.objects.filter(id__gt=id).filter(
                    stageName_id=stage_id).filter(categoryName_id=category_id).order_by('id')
                serializer = VideoArticleSerializer(next_article, many=True)
                next_article = serializer.data[0]
            except:
                next_article = None

            data_list = []
            data_list.append(pre_article)
            data_list.append(next_article)
            return JsonResponse(data_list, safe=False)


class StageViewSetNew(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializerNew
    http_method_names = ["get"]
