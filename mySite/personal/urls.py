from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('additional1/', views.additional1, name='additional1'),
    path('additional2/', views.additional2, name='additional2'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index view for listing polls
    path('poll/<int:question_id>/', views.poll_detail, name='poll_detail'),  # Detail view for a specific poll
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),  # Vote view for submitting a vote
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/<int:question_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
    path('register/', views.register, name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/<int:question_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
