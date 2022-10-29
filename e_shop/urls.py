from django.contrib import admin
from django.urls import path, include

# для отображения изображений
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main_page.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # добавить изображения

