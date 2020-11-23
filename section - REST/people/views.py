from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from people.models import Person
from people.forms import PersonForm
from rest_framework import viewsets
from people.serializers import PersonSerializer


class PersonSerializerView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(ListView):
    model = Person
    context_object_name = "people"


class PersonCreateView(CreateView):
    model = Person
    fields = ("name", "email", "job_title", "bio")
    success_url = reverse_lazy("person_list")


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "people/person_update_form.html"
    success_url = reverse_lazy("person_list")

def chord_redirect(request):
    log(request.user, 'Chord redirect')
    return redirect('chord/:aml_chord')


