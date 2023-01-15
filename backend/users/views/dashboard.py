# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import ajax_required
# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import EditUserForm

User = get_user_model()

@login_required
def dashboard(request):
	"""
    Function based view used for our user dashboard.

    **Template:**

    :template:`users/dashboard.html`
    """
	if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
		form = EditUserForm(request.POST, files = request.FILES, instance = request.user)

		if form.is_valid():
			form.save()
			data = {'result': 'Success', 'message': "Your profile has been updated", 'redirect': False}
			return JsonResponse(data)
		else:
			data = {'result': "Error", 'message': "There was an error, please try again", 'redirect': False}
			return JsonResponse(data)				
	else:
		form = EditUserForm(instance=request.user)
	return render(request, 'users/dashboard.html', context={'form': form, "page_name": "Dashboard"})

