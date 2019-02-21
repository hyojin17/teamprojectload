from django.contrib import admin
from django.urls import path, include
import home.views
import recommand.views
import beauty.views
import enter.views
import food.views
import vlog.views
import etc.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),
    path('notice/', home.views.notice, name="notice"),
    path('recommand/', recommand.views.recommand, name="recommand"),
    path('recommand/', include('recommand.urls')),
    path('accounts/', include('accounts.urls')),
    path('beauty/', beauty.views.beauty, name='beauty'),
    path('enter/', enter.views.enter, name='enter'),
    path('food/', food.views.food, name='food'),
    path('vlog/', vlog.views.vlog, name='vlog'),
    path('etc/', etc.views.etc, name='etc'),
]
