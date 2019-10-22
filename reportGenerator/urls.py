from django.urls import path
from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^api/excel_export$', api.ExcelExport.as_view(), name='ExcelExportAPI'),
    url(r'^api/excel_export/1$', api.ExcelExport.as_view(), name='ExcelExportAPI2'),
]