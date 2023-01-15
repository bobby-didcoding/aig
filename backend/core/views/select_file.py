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
from core.models import Gallery

@ajax_required
@login_required
def select_file(request):
    '''
    Used to managed user file selections
    '''
    user = request.user
    if request.method == "POST":
        
        files = request.POST.getlist("id[]")

        #create a list of Gallery ID's
        gallery_objects = []
        for file_id in files:
            if file_id != 'on':
                try:
                    obj = Gallery.objects.get(pk = file_id)
                    gallery_objects.append(obj)
                except (Gallery.DoesNotExist, ValidationError):
                    pass
        
        #Validation: check if users has selected more than 4
        if len(gallery_objects) > 4:
            data = {'result': "Error", 'message': "Please select up to 4 files", 'redirect': False}
            return JsonResponse(data)

        #remove current selections
        Gallery.objects.remove_user(user)

        #Add new selection
        for obj in gallery_objects:
            obj.users.add(user)
            obj.save()
        
        data = {'result': "Success", 'message': "", 'redirect': "/my-images/"}
        return JsonResponse(data)
    data = {'result': "Error", 'message': "Something went wrong", 'redirect': False}
    return JsonResponse(data)

