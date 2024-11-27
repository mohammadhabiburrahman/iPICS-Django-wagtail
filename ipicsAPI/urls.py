from django.urls import include, path
from  ipicsAPI import views
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )


schema_view = get_schema_view(
    openapi.Info(
        title="IPICS API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/",
        contact=openapi.Contact(email="contact@test.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('stage/',views.StagesViewSet.as_view()),
    path('stagecategory/',views.StageViewSetNew.as_view()),
    path('category/',views.CategoryViewSet.as_view()),
    path('text/',views.TextualArticleViewSet.as_view()),
    path('prennextarticle/<int:id>',views.TextualArticleViewSet.PrenNextTextualArticleViewMethod),
    path('prennextvideo/<int:id>',views.VideoArticleViewSet.PrenNextVideoArticleViewMethod),
    path('prennextaudio/<int:id>',views.AudioArticleViewSet.PrenNextAudioArticleViewMethod),   
    path('audio/',views.AudioArticleViewSet.as_view()),
    path('video/',views.VideoArticleViewSet.as_view()),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui')

    # path('api/api.json/', schema_view.without_ui(cache_timeout=0),
    #      name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc',
    #                                    cache_timeout=0), name='schema-redoc'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]