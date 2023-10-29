from django.shortcuts import render
from services.entity_service import get_entity_by_attrs, get_entity_context


def patent_by_attr(request):
    if request.GET:
        params = request.GET.dict()
        patents = get_entity_by_attrs(**params)
        contexts = get_entity_context(patents)
        return render(request, 'home.html', {'entities': contexts})

    return render(request, 'home.html')
