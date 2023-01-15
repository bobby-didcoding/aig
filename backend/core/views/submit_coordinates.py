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
from core.models import Coordinate, Gallery


@login_required
def submit_coordinates(request, id):
    '''
    Used to submit coordinates
    '''
    user = request.user
    if request.method == "POST":
        try:
            gallery_obj = Gallery.objects.get(pk = id)
        except (Gallery.DoesNotExist, ValidationError):
            data = {'result': "Error", 'message': "We couldn't find the Gallery object.", 'redirect': False}

        
        #Used to work through all coordinates sent via ajax
        post = request.POST.dict()
        post.pop('csrfmiddlewaretoken')
        for key, value in post.items():
            coordinate_kwargs = {
                'user': user,
                'gallery': Gallery.objects.get(pk = id),
            }
            coordinates_list = value.split(",")
            for code in coordinates_list:
                split_code = code.split(":")
                key = split_code[0]
                value=split_code[1]
                coordinate_kwargs[key] = value
            Coordinate.objects.create(**coordinate_kwargs)
        
        data = {'result': "Success", 'message': "We have successfully saved your selected coordinates.", 'redirect': '/my-coordinates/'}
        return JsonResponse(data)
    data = {'result': "Error", 'message': "Something went wrong", 'redirect': False}
    return JsonResponse(data)

