from django.test import TestCase
from polls.models import ContactMessage   


class ContactMessageTestCase(TestCase):

    def test_can_create_message(self):
        # Створюємо повідомлення
        message = ContactMessage.objects.create(
            name="Іван Петренко",
            email="ivan@example.com",
            subject="Запитання про товар",
            message="Добрий день! Скільки коштує доставка?"
        )

        # Перевіряємо, чи збереглося
        self.assertEqual(ContactMessage.objects.count(), 1)

        # Перевіряємо основні поля
        self.assertEqual(message.name, "Іван Петренко")
        self.assertEqual(message.email, "ivan@example.com")
        self.assertEqual(message.subject, "Запитання про товар")
        self.assertEqual(message.message, "Добрий день! Скільки коштує доставка?")

        # Перевіряємо, що created_at заповнилося автоматично
        self.assertIsNotNone(message.created_at)

    def test_str_method_works_correctly(self):
        message = ContactMessage.objects.create(
            name="Марта",
            email="marta@test.ua",
            message="Тестове повідомлення"
        )

        # Перевіряємо метод __str__
        self.assertEqual(str(message), "Message from Марта")
        
    # перевірка на те що поля можуть бути пустими 
    def test_subject_can_be_empty(self):
        msg = ContactMessage.objects.create(
            name="Без теми",
            email="no@subject.com",
            message="Тільки повідомлення"
        )
        self.assertEqual(msg.subject, "")
        self.assertEqual(ContactMessage.objects.count(), 1)
