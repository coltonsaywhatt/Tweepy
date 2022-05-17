from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('tweeps/', views.tweeps_index, name='index'),
  path('tweeps/search', views.tweep_search, name='tweep_search'),
  path('tweeps/<int:tweep_id>/', views.tweeps_detail, name='detail'),
  path('tweeps/create/', views.TweepCreate.as_view(), name='tweeps_create'),
  path('tweeps/<int:pk>/update/', views.TweepUpdate.as_view(), name='tweeps_update'),
  path('tweeps/<int:pk>/delete/', views.TweepDelete.as_view(), name='tweeps_delete'),
  path('tags/<slug:tag_slug>/', views.tweeps_by_tag, name='tweeps_by_tag'),
]