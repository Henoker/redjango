from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
import debug_toolbar
print(f"Time zone: {settings.TIME_ZONE}")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", blog.views.index, name="index"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail")
    
] 
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
