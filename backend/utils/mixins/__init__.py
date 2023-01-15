# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from urllib.parse import urlencode

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect



def FormErrors(*args):
	'''
	Handles form error that are passed back to AJAX calls
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message





class AjaxFormMixin(object):
	'''
	Super basic mixin to ajaxify django form - can be over written in view by calling form_valid method
	'''
	
	def form_invalid(self, form):
		response = super(AjaxFormMixin, self).form_invalid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			return JsonResponse(form.errors, status=400)
		return response

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			form.save()
			return JsonResponse({'message':'Success'})
		return response



def RedirectParams(**kwargs):
	'''
	Used to append url parameters when redirecting users
	'''
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response

