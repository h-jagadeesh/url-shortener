from django.urls import path
from . import views

app_name = "gotolink"
urlpatterns = [
	path("",views.index,name="index"),
	path("success",views.success,name="success"),
	path("<str:s_url>",views.s_link,name="s_link"),
]