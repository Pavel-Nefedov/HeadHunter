from django.test import TestCase
from candidateapp.models import Candidate


class CandidateModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Candidate.objects.create(first_name='maks', last_name='maks')

    def test_first_name_label(self):
        candidate = Candidate.objects.get(id=1)
        field_label = candidate._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        candidate = Candidate.objects.get(id=1)
        field_label = candidate._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_first_name_max_length(self):
        candidate = Candidate.objects.get(id=1)
        max_length = candidate._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_max_length(self):
        candidate = Candidate.objects.get(id=1)
        max_length = candidate._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_get_absolute_url(self):
        candidate = Candidate.objects.get(id=1)
        self.assertEquals(candidate.get_absolute_url(), '/candidate/user_profile/1')
