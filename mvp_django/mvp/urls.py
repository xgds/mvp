from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from mvp.api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'object', views.ObjectViewSet)
router.register(r'flight', views.FlightViewSet)
router.register(r'position', views.PositionViewSet)

object_query = views.ObjectQuery.as_view({
    'get': 'list',  
})

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += format_suffix_patterns(
    [
        path('flight/<int:pk>/objects', object_query)
    ]
)
