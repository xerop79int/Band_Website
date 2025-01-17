from django.urls import path
from app.views import *

urlpatterns = [
    path('login', ManagerSigninView.as_view()),
    path('register', ManagerSignupView.as_view()),
    path('customerrequest', ManagerCustomerRequestView.as_view()),
    path('songslist', ManagerBandSongsListView.as_view()),
    path('customersongslist', ManagerCustomerSongsListView.as_view()),
    path('likedbandsongslist', ManagerLikedBandSongsListView.as_view()),
    path('upload', ManagerUploadSongsListView.as_view()),
    path('sets', ManagerSetsView.as_view()),
    path('songsinset', ManagerSongsInSetView.as_view()),
    path('playlist', ManagerPlaylistView.as_view()),
    path('venue', ManagerVenueView.as_view()),
    path('show', ManagerShowView.as_view()),
    path('scrollshare', ManagerScrollShareView.as_view()),
    path('modifybpm', ManagerModifyBPMView.as_view()),
    path('display', ManagerDisplayView.as_view()),
    path('displaymetronome', ManagerDisplayMetronomeView.as_view()),
    path('backup', ManagerBackupView.as_view()),
    path('restore', ManagerRestoreView.as_view()),
    path('logs', ManagerLogsView.as_view()),
    path('date', ManagerDateView.as_view()),
]