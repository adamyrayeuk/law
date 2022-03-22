from django.urls import path, include

urlpatterns = [
    path('account/', include('apps.accounts.urls')),
    path('oauth/', include('apps.oauth.urls')),
    path('course/', include('apps.courses.urls')),
]