from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', include('spearfishing_app.common.urls')),
                  path('accounts/', include('spearfishing_app.accounts.urls')),
                  path('events/', include('spearfishing_app.events.urls')),
                  path('locations/', include('spearfishing_app.locations.urls')),
                  path('photos/', include('spearfishing_app.photos.urls')),
                  path('stories/', include('spearfishing_app.stories.urls')),
                  path('market/', include('spearfishing_app.market.urls')),

                  # Add this for reach the images in projects dir.
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
