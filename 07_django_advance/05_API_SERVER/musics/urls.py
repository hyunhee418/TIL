from django.urls import path
from . import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        # 필수
        title='Music API',
        default_version='vq',
        # 선택
        description='아티스트, 음악, 의견을 제공하는 API 입니다.',
        contact=openapi.Contact('hyunhee18@gmail.com'),
        license=openapi.License('SSAFY API'),

    )
)

app_name = 'musics'

urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),

    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),

    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_id>', views.music_detail, name='music_detail'),
]
