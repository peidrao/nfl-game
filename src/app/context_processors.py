from app.domain.models.conference import Conference


def conferences(request):
    conferences = Conference.objects.all()
    return {"conferences": conferences}
