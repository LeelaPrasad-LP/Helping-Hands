from django.urls import path,include
from . import views

urlpatterns = [
    path('student/',views.student,name='loginhome'),
    path('student/profile/',views.profileView,name='profile'),
    path('student/contact/',views.Contactus.as_view(),name='contact'),
    path('student/problems/' ,views.ProblemsView.as_view(),name='problems'),
    path('student/problem/create/',views.ProblemCreate.as_view(),name='create'),
    path('student/problem/<int:pk>/edit/',views.ProblemEdit.as_view(),name='edit'),
    path('student/problem/<int:pk>/upvote', views.upvote, name='upvote'),
    path('student/problem/<int:pk>/detail',views.Problemdetailview.as_view(),name='detail'),


    path('donor/',views.donor,name='donorlogin'),
    path('donor/profile/',views.dprofileView,name='dprofile'),
    path('donor/contact/',views.dContactus.as_view(),name='dcontact'),
    path('donor/problems/',views.dProbView.as_view(),name='dproblems'),
    path('donor/problem/<int:pk>/detail/',views.dProblemdetailview.as_view(),name='ddetail'),

]
