from django.urls import path
from .views import *

app_name = 'Dating'
urlpatterns = [
    path('index/',intex,name='index'),
    path('',GenderselectView.as_view(),name='selectgender'),
    path('gridview/',Gridview.as_view(),name='gridview'),
    path('location/',Locationview.as_view(),name='location'),
    path('education/',Educationview.as_view(),name='education'),
    path('pro/',Desiginationview.as_view(),name='pro'),
    path('matches/',Matchesview.as_view(),name='matches'),
    path('discover/',Discoverview.as_view(),name='discover'),
    path('viewed/',Profileview.as_view(),name='viewed'),
    path('errorview/',Errorview.as_view(),name='errorview'),
    path('notificationview/',Notificationview.as_view(),name='notificationview'),
    path('upgradeview/',Upgradeview.as_view(),name='upgradeview'),



    # path('login/',LoginView.as_view(),name='login'),
    # path('locationgridview/',LocationGridview.as_view(),name='locationgridview'),
    # path('educationgridview/',EducationGridview.as_view(),name='educationgridview'),
    # path('gallery/',GalleryView.as_view(),name='gallery'),
    # path('gallery/delete/<int:pk>/', MediaDeleteView.as_view(), name='media_delete'),
    # path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('send_request/<int:user_id>/', SendrequestView.as_view(), name='send_request'),
    # path('send_html/', SendhtmlView.as_view(), name='send_html'),
    # path('send_html/send_remove/<int:user_id>/', RemovelistView.as_view(), name='send_remove'),
    # path('accept_requests/', Accepthtmlview.as_view(), name='accept_requests'),
    # path('accept_requests/accept_request/<int:request_id>/', AcceptRequestView.as_view(), name='accept_request'),
    # path('accept_requests/reject_request/<int:request_id>/', RejectRequestView.as_view(), name='reject_request'),
    # path('friends_list/', FriendsListView.as_view(), name='friends_list'),
    # path('short_list/<int:request_id>/', ShortlistView.as_view(), name='short_list'),
    # path('short_html/', ShorthtmlView.as_view(), name='short_html'),
    # path('not_interest/<int:request_id>/', NotinterestedView.as_view(), name='not_interest'),
    # path('send_message/<int:id>/', SendMessageView.as_view(), name='send_message'),  
  
  
]