from django.test import TestCase
from django.urls import reverse
from polls.models import ContactMessage

class ContentViewTest(TestCase):

    def test_of_index_page(self):

        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        

    def test_of_page_of_index(self):

        abc = self.client.get(reverse('polls:index'))

        self.assertTemplateUsed(abc, 'polls/index.html')


    def test_post_valid_form_creates_message_and_redirects(self):
        # Дані, які ніби відправив користувач через форму
        form_data = {
            'name': 'Тестовий Користувач',
            'email': 'test@example.com',
            'subject': 'Тестова тема',
            'message': 'Це автоматичний тест'
        }

        # Симулюємо POST-запит (як відправка форми)
        response = self.client.post(
            reverse('polls:send_contact'),          # ← свій url name
            data=form_data,
            follow=True                  # follow=True — йде за редиректами автоматично
        )

        # Перевіряємо, чи створилося повідомлення в базі
        self.assertEqual(ContactMessage.objects.count(), 1)

        # Перевіряємо редирект (наприклад на головну або success сторінку)
        self.assertRedirects(response, reverse('polls:index'))  # ← заміни на свій success_url

        # Перевіряємо, чи є повідомлення про успіх (якщо виводиш messages)
        self.assertContains(response, "Дякуємо! Ваше повідомлення надіслано.")
