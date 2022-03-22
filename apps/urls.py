from django.urls import path, include

urlpatterns = [
    path('account/', include('apps.accounts.urls')),
    path('oauth/', include('apps.oauth.urls')),
<<<<<<< HEAD
    path('course/', include('apps.courses.urls')),
=======
>>>>>>> a961fa4083eca7b33c333dc742602349a1399467
]