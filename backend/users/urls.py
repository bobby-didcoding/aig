# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from . import views

app_name = "users"

urlpatterns = [
	path('login/',views.LoginView.as_view(),name="login"),
	path('signup/',views.SignUpView.as_view(),name="signup"),
	path('logout/',views.logout_user,name="logout"),
	path('dashboard/',views.dashboard ,name="dashboard")
	
]