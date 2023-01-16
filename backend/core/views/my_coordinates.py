# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Coordinate


class MyCoordinatesView(generic.ListView):
    """
    ListView used for our my coordinates page.

    Queryset of :model:`core.Coordinate`.

    **Template:**

    :template:`core/my_coordinates.html`
    """
    model = Coordinate
    template_name = "core/my_coordinates.html"
    paginate_by: int = 10

    def get_queryset(self):
        qs = self.model.objects.active().filter(user = self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f'My Coordinates'
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
