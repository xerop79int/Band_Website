from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(BandLeader)
admin.site.register(BandMember)
admin.site.register(CustomerRequest)
admin.site.register(BandSongsList)
admin.site.register(LikedBandSongsList)
admin.site.register(SongsSet)
admin.site.register(Sets)
admin.site.register(SongsInSet)
admin.site.register(Playlist)
