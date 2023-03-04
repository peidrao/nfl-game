from team.models import Conference


def conferences(request):
    conferences = Conference.objects.all()
    return {"conferences": conferences}
