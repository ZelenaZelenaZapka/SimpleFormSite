from django.db import models

# Створення моделі( тобто колонок бази )
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
    # Для повідомлення користувача який використав форму 
    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення з контактів"
