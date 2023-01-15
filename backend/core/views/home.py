# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.utils.decorators import method_decorator

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import login_forbidden


class HomeView(generic.TemplateView):
    """
    TemplateView used for our home page.

    **Template:**

    :template:`core/index.html`
    """
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f'Home'
        return context

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
