
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),      # app 1
    path('', include("accounts.urls")),  # app 2
    path('accounts/', include("django.contrib.auth.urls")),   # working for login.html
]
