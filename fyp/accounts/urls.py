from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('pending-institutions/', views.pending_institutions_view, name='pending_institutions'),
    path('approve-institution/<int:user_id>/', views.approve_institution_view, name='approve_institution'),
    path('revoke-approval/<int:user_id>/', views.revoke_approval_view, name='revoke_approval'),
]
