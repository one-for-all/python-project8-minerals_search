import string
from django.test import TestCase
from django.shortcuts import reverse
from .models import Mineral
from .models import initialize
import random


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
    @classmethod
    def setUpClass(cls):
        super(MineralViewTest, cls).setUpClass()
        initialize()

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

    def test_filter_by_letter_view(self):
        letter = random.choice(string.ascii_uppercase)
        resp = self.client.get(reverse('minerals:filter', kwargs={
            'letter': letter
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('minerals/list.html')
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertEqual(mineral.name[0].upper(), letter)

    def test_search_view(self):
        test_string = 'ab'
        resp = self.client.get(reverse('minerals:search'), {'q': test_string})
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertIn(test_string.lower(), mineral.name.lower())

    def test_filter_by_category_view(self):
        categories = [
            'Silicate',
            'Oxide',
            'Sulfate',
            'Sulfide',
            'Carbonate',
            'Halide',
            'Sulfosalt',
            'Phosphate',
            'Borate',
            'Organic',
            'Arsenate',
            'Native',
        ]
        category = random.choice(categories)
        resp = self.client.get(reverse('minerals:filter_by_cate', kwargs={
            'category': category}))
        self.assertEqual(resp.status_code, 200)
        minerals = resp.context['minerals']
        for mineral in minerals:
            self.assertEqual(mineral.category.lower(), category.lower())

    def tearDown(self):
        self.mineral.delete()
