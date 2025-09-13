from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include('User.urls')),
    path('Profile/', include('Profile.urls')),
    path('Post/', include('Post.urls')),
    path('Comment/', include('Comment.urls')),
    path('Notifications/', include('Notification.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
