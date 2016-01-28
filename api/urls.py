from django.contrib import admin
from django.conf.urls import url, include
from .models import Person
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('facebookID', 'name', 'username', 'gender')

# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^graph/', include('graph.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]