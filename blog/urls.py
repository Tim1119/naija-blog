from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('apps.posts.urls', namespace='article')),
    path('comment/', include('apps.comments.urls', namespace='comments')),
    path('profiles/', include('apps.profiles.urls', namespace='profiles')),
    path('accounts/', include('apps.authentication.urls', namespace='authentication')),
    # path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
