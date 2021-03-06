from django.conf.urls import url, include
from rpc4django.views import serve_rpc_request
from . import views
from .models import AOI
from features.views import form_resources

urlpatterns = [
    url(r'^rpc$', serve_rpc_request, name='rpc'),
    url(r'^about/', views.about, name='about'),
    url(r'^help/', views.help, name='help'),
    url(r'^user/', views.index, name='user'),
    url(r'^search/', views.index, name='search'),
    url(r'^portfolio/', views.index, name='portfolio'),
    # TODO fix urls so account and visualize static text can be overwritten
    url(r'^visualize/?$', views.planner, name='planner'),
    # url(r"^visualize/", include("visualize.urls")),
    url(r'^account/', views.account, name='login'),
    url(r'^get_taxlot_json', views.get_taxlot_json, name='get taxlot json'),
    url(r'^geosearch', views.geosearch, name='geosearch'),

    url(r"^features/aoi/form", form_resources,
        kwargs={'model': AOI},
        name="aoi_create_form"),
    url(r"^features/", include("features.urls")),

    url(r'^', views.index, name='index'),
]
