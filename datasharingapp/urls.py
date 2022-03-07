from django.conf.urls.static import static
from django.urls import path

from datasharingapp import views, authority_views, owner_views, recievers_views, enc_views
from datasharingpro import settings

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('authority', views.authority_view, name='authority'),
    path('recievers', views.recievers_view, name='recievers'),
    path('owners', views.owners_view, name='owners'),
    path('login_view', views.login_view, name='login_view'),
    path('owner_register', views.owner_register, name='owner_register'),
    path('receiver_register', views.receiver_register, name='receiver_register'),
    path('logout', views.logout_view, name='logout'),
    path('choice_page', views.choice_page, name='choice_page'),


    path('profile_view_owner', owner_views.profile_view_owner, name='profile_view_owner'),
    path('view_file', owner_views.view_file, name='view_file'),
    path('upload_files', owner_views.upload_files, name='upload_files'),
    path('complaint_view_owners', owner_views.complaint_view, name='complaint_view_owners'),
    path('complaint_register_owners', owner_views.complaint_add, name='complaint_register_owners'),


    path('profile_view_reciever', recievers_views.profile_view_reciever, name='profile_view_reciever'),
    path('view_file_recievers', recievers_views.view_file_reciever, name='view_file_recievers'),
    path('complaint_view_reciever', recievers_views.complaint_view_reciever, name='complaint_view_reciever'),
    path('complaint_add_reciever', recievers_views.complaint_add_reciever, name='complaint_add_reciever'),


    path('view_owner', authority_views.view_owner, name='view_owner'),
    path('view_reciever', authority_views.view_reciever, name='view_reciever'),
    path('view_upload', authority_views.view_upload, name='view_upload'),
    # path('encrypt', enc_views.encrypt, name='encrypt'),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
