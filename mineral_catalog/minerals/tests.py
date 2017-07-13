from django.test import TestCase
from django.shortcuts import reverse
from .models import Mineral


class MineralModelTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='amazing mineral',
            category='sulfide'
        )

    def tearDown(self):
        self.mineral.delete()

    def test_mineral_creation(self):
        self.assertIn(self.mineral, Mineral.objects.all())


class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='amazing mineral',
            category='sulfide'
        )

    def test_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertContains(resp, self.mineral.name.title())

    def test_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk':
                                       self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.name.title())
        self.assertContains(resp, self.mineral.category)

    def test_random_view(self):
        resp = self.client.get(reverse('minerals:random'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def tearDown(self):
        self.mineral.delete()
