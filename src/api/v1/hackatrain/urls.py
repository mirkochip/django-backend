from django.conf.urls import url

from api.v1.hackatrain.views import HealthView, SimplePostView, SimpleGetView

urlpatterns = [
    url(r'^health$', HealthView.as_view(), name='health'),
    url(r'^simple_post$', SimplePostView.as_view(), name='simple_post$'),
    url(r'^simple_get$', SimpleGetView.as_view(), name='simple_get$'),
]
