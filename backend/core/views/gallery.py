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


class GalleryView(generic.ListView):
    """
    ListView used for our gallery page.

    Queryset of :model:`core.Gallery`.

    **Template:**

    :template:`core/gallery.html`
    """
    model = Gallery
    template_name = "core/gallery.html"
    paginate_by: int = 10

    def get_queryset(self):
        qs = self.model.objects.active()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f'Gallery'
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
