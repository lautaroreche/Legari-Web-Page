from datetime import datetime


def current_year():
    context = {'current_year': datetime.now().year}
    return context
