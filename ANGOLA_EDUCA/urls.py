from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from core import views 
from core.views import Erro  

# URLs principais com suporte a i18n
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('Educa_Angola/', include('core.urls')), 
    path('bolsa/', include('bolsas.urls')),
    path('gestoreduca/', include('gestoreduca.urls')),
    path('comentarios/', include('comentarios.urls')),
    path('cursos/', include('cursos.urls')),
    path('instituicoes/', include('instituicoes.urls')),
    path('noticias/', include('noticias.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('biblioteca/', include('biblioteca.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
handler404 = 'core.views.Erro'


