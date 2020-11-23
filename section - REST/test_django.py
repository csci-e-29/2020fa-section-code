from django.test import TestCase
from people.models import Person
from rest_framework import status
from people.serializers import PersonSerializer
from rest_framework.test import APIRequestFactory
from people.views import PersonSerializerView
from django.urls import reverse, resolve
from people.urls import urlpatterns


# Needs to run export DJANGO_SETTINGS_MODULE=project_config.settings

"""
@login_required
def aml_chord(request):
    context = {}
    data = open_chord_data('{}/scripts/chord/data/output/aml_chords.json'.format(path_prefix))
    context['data'] = data
    sample_data = open_chord_data('{}/scripts/chord/data/output/aml_samples.json'.format(path_prefix))
    context['sample_data'] = sample_data
    context['cancer'] = 'AML'
    log(request.user, 'AML Chord Diagram')
    return render(request, 'chord/chord.html', {'context':context})

Designed to give a general idea of what test cases should look like. Obviously needs to be tailored for PSET specifically, but high level this is what 
some test might look like.

Cover a few things:
1. Models - adding / removing data, checking various inputs & outputs
2. Views - tests views have correct response codes and that you can successfully perform CRUD operations
3. Serializers - check serialization / deserizalition successfully
4. URLS - reverse (formats a URL) & resolve (checks URL vs view function)

Make sure you do this for tasks that are dependent on one another as well!
"""


class ModelTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="William", email="bleh@gmail.com")
        Person.objects.create(name="Malika", email="bleh2@gmail.com")

    def test_user_django_case(self):
        """
        Test users being added to the database correctly + simple operations
        """
        person_one = Person.objects.get(name="William")
        self.assertEqual(person_one.email, 'bleh@gmail.com')
        self.assertEqual(2, Person.objects.count())
        self.assertEqual(Person.objects.get(name="William").bio, '')


class ViewsTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="William", email="bleh@gmail.com")
        Person.objects.create(name="Malika", email="bleh2@gmail.com")

    def test_get_views(self):
        """
        Test view urls are correct
        """
        self.assertEqual(self.client.get("/").status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.get("/fake").status_code, status.HTTP_404_NOT_FOUND)

    def test_http(self):
        """
        Test for CRUD operations
        """
        response = self.client.get("/people/people-serializer/person/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'William')

        # Insert similar tests for PUT, DELETE, CREATE, etc

        # what Django REST testing should be like, but the above test work as well
        factory = APIRequestFactory()
        request = factory.get('/people/people-serializer/person/')
        g = PersonSerializerView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data[0]['name'], 'William')


class SerializerTestCase(TestCase):
    def setUp(self):
        self.person_one = Person.objects.create(name="William", email="bleh@gmail.com")
        self.person_two = Person.objects.create(name="Malika", email="bleh2@gmail.com")

    def test_serializer(self):
        """
        Test serialization is correct (and should test deserialization, etc)
        """
        ps = PersonSerializer(self.person_one)
        self.assertEqual(ps.data['name'], "William")


class URLSTestCase(TestCase):

    def test_reverse(self):
        url = reverse('person_edit', kwargs={'pk': 1})
        self.assertEqual(url, '/people/people/1/edit/')

    def test_resolve(self):
        resolver = resolve('/people/swagger/')
        self.assertEqual(resolver.view_name, 'schema-swagger-ui')
        # test class type here as well
        