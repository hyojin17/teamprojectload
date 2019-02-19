from django.contrib import admin
from django.urls import path, include
import home.views
import recommand.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),
    path('notice/', home.views.notice, name="notice"),
    path('recommand/', recommand.views.recommand, name="recommand"),
    path('recommand/', include('recommand.urls')),
    path('accounts/', include('accounts.urls')),

]
