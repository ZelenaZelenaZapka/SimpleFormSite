from django.contrib import admin

from .models import ContactMessage

# За допомогою цього ми створюємо список адмінів 
admin.site.register(ContactMessage)
