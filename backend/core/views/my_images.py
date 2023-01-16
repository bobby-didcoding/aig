# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Gallery


class MyImagesView(generic.ListView):
    """
    ListView used for our my images detail page. Only user selected files will display.
    Note: up to 4 ONLY.

    Queryset of :model:`core.Gallery`.

    **Template:**

    :template:`core/my_images.html`
    """
    model = Gallery
    template_name = "core/my_images.html"
    paginate_by: int = 4

    def get_queryset(self):
        qs = self.model.objects.active().filter(users = self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f'My images'
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
