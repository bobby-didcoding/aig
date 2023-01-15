# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import ajax_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Coordinate

@ajax_required
@login_required
def create_json(request, id):
    '''
    Used to managed the creation and downloading of json
    '''
    user = request.user
    if request.method == "POST":
        
        try:
            obj = Coordinate.objects.get(pk = id)
            obj.create_json()
            data = {'json_url': obj.file.url}
        except (Coordinate.DoesNotExist, ValidationError):
            data = {'result': "Error", 'message': "We could not find the given Coordinate object", 'redirect': False}
    
        return JsonResponse(data)
    data = {'result': "Error", 'message': "Something went wrong", 'redirect': False}
    return JsonResponse(data)

