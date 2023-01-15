# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth import get_user_model, login
from django.views import generic
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import AjaxFormMixin
from utils.decorators import login_forbidden

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import LoginForm

User = get_user_model()

class LoginView(AjaxFormMixin, generic.FormView):
	'''
	Basic view for user sign in
	'''
	template_name = "users/login.html"
	form_class = LoginForm

	#This form view uses the AJAX mixin but we must add
	#a success_url to user the generic.FormView
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["page_name"] = f'Sign In'
		return context

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			user=form.login(self.request)
			if user is not None and user.is_active:
				login(self.request, user)
				next_url = self.request.GET.get('next')
				if next_url:
					data = {'result': 'Success', 'message': "You are now signed in", 'redirect': next_url}
				else:
					data = {'result': 'Success', 'message': "You are now signed in", 'redirect': '/dashboard/'}
			else:
				data = {'result': "Error", 'message': "User is not active", 'redirect': False}
			return JsonResponse(data)	
		else:
			data = {'result': "Error", 'message': "There was an error, please try again", 'redirect': False}
			return JsonResponse(data)
		return response

	@method_decorator(login_forbidden)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)




