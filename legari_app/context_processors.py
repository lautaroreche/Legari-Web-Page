from datetime import datetime
from django.conf import settings


def current_year(request):
    context = {'current_year': datetime.now().year}
    return context


def ga_settings(request):
    return {
        "GA_MEASUREMENT_ID": getattr(settings, "GA_MEASUREMENT_ID", ""),
        "DEBUG": getattr(settings, "DEBUG", False),
    }
