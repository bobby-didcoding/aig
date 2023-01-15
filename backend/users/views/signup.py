# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import Group
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
from users.forms import SignupForm

User = get_user_model()

class SignUpView(AjaxFormMixin, generic.FormView):
	'''
	Basic view for user sign up with reCAPTURE security
	'''
	template_name = "users/signup.html"
	form_class = SignupForm

	#This form view uses the AJAX mixin but we must add
	#a success_url to user the generic.FormView
	success_url = "/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["page_name"] = f'Sign Up'
		return context

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			obj = form.save(commit=False)
			obj.is_active = True
			obj.save()
			
			#assign "Customer" as default group
			Customer_group, created = Group.objects.get_or_create(name="Customer")
			obj.groups.add(Customer_group)

			login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')
			data = {'result': 'Success', 'message': "Thank you for signing up", 'redirect': '/dashboard/'}
			return JsonResponse(data)
		else:
			data = {'result': "Error", 'message': "There was an error, please try again", 'redirect': False}
			return JsonResponse(data)
		return response

	@method_decorator(login_forbidden)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)



