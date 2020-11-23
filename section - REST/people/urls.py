from people.views import PersonListView, PersonCreateView, PersonUpdateView, PersonSerializerView
from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'person', PersonSerializerView, basename='Person')

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('people-serializer/', include(router.urls)),
    path('people/', PersonListView.as_view(), name='person_list'),
    path('people/add/', PersonCreateView.as_view(), name='person_add'),
    path('people/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
]
