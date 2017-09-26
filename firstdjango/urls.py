from django.conf.urls import include, url
from django.contrib import admin

from inventory import views


urlpatterns = [
    url(r'^$', views.index, name='index'), # first parameter regex(match against request), view to call if request matched ,name parameter for template
    url(r'^item/(?P<id>\d+)/',views.item_detail, name='item_detail'),# (?P<id>\d+) is name group which means the digit we pass will called id
    url(r'^admin/', include(admin.site.urls)),
]
