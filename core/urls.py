from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers

from tasks.views import UserViewSet, GroupViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"tasks", TaskViewSet)

def health(request):
    return JsonResponse({"status": "ok"})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("health/", health),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', include('django_prometheus.urls')),

    
]

PROMETHEUS_LATENCY_BUCKETS = (
    0.01,   # 10 ms
    0.025,  # 25 ms
    0.05,   # 50 ms
    0.075,  # 75 ms
    0.1,    # 100 ms
    0.25,   # 250 ms
    0.5,    # 500 ms
    0.75,   # 750 ms
    1.0,    # 1 segundo
    2.5,
    5.0,
    7.5,
    10.0,
    25.0,
    50.0,
    75.0,
    float('inf'),
)