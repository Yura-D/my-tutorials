from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from apps.tutorials.views import TutorialBotView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/tutorial/', csrf_exempt(TutorialBotView.as_view())),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
