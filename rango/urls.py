from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rango import views

app_name = 'rango'

urlpatterns = [
	path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)