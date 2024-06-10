
from django.contrib import admin
from django.urls import path, include
from contact.views import contact, landing, aboutus, students_list, student_info
from track.views import  track_landing
#############
from bookindex.views import books_landing, books_info, books_list
from aboutus.views import aboutus
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', landing, name='landing'),
    path('books_list', books_list, name='books_list'),
    path('books_info', books_info, name='books_info'),
    path('tracks', track_landing, name='track_landing'),
    path('students/', include('contact.urls')),
    path('tracks/', include('track.urls')),
    #####################
    path('contact/', include('contactus.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('bookindex/', include('bookindex.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

