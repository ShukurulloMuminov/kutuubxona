"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from mainApp.views import *



urlpatterns = [
    path('', home_page_view),
    path('admin/', admin.site.urls),

    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:kitoblar_id>/', kitoblar_details_view),
    path('kitoblar/<int:kitob_id>/delete/', kitoblar_delete_view),
    path('kitoblar/<int:kitob_id>/delete/confirm', kitoblar_delete_confirm_view),
    path('kitoblar/<int:id>/update/', kitoblar_update_view, name='kitoblar_update'),

    path('mualliflar/', muallif_view, name="mualliflar"),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('mualliflar/<int:muallif_id>/delete/', muallif_delete_view),
    path('mualliflar/<int:muallif_id>/delete/confirm', muallif_delete_confirm_view),
    path('mualliflar/<int:id>/update/', muallif_update_view),

    path('record/', rekordlar_view),
    path('record/<int:rekordlar_id>/', rekordlar_details_view),
    path('record/<int:record_id>/delete/', record_delete_view),
    path('record/<int:record_id>/delete/confirm', record_delete_confirm_view),

    path('kutubxona/', kutubxona_view),
    path('kutubxona/<int:kutubxona_id>/', kutubxona_details_view),
    path('kutubxona/<int:kutubxona_id>/delete/', kutubxona_delete_view),
    path('kutubxona/<int:kutubxona_id>/delete/confirm', kutubxona_delete_confirm_view),

    path('tirik_muallif/', tirik_mualliflar_view),
    path('top3_sahifa/', top3_sahifa_view),
    path('top3_muallif/', top3_muallif_view),
    path('record_sanasi/', rekordlar_sanasi_view),
    path('tiriklar_kitobi/', tiriklar_kitobi_view),
    path('tarixiy/', tarixiy_view),
    path('eng_katta/', eng_katta_view),
    path('10tadan_kam_kitobli/', eng_kop_kitob_view),


]
