from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    return render(request, "polls/index.html")

def contact_view(request):
    # 1. Перевіряємо, чи користувач НАТИСНУВ кнопку (метод POST)
    if request.method == 'POST':
        # 2. Беремо дані з запиту (те, що прийшло з HTML форми)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # 3. Проста перевірка (валідація)
        if name and email:
            # 4. СТВОРЮЄМО і ЗБЕРІГАЄМО запис в БД
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # 5. Показуємо повідомлення про успіх
            messages.success(request, 'Дякуємо! Ваше повідомлення надіслано.')
            
            # 6. ПЕРЕНАПРАВЛЕННЯ (Redirect)
            # Це критично для твого SPA! Ми кидаємо юзера назад на головну.
            # 'home' - це name= твого головного URL (заміни на свій, якщо інший)
            return redirect('polls:index') 
        else:
            messages.error(request, 'Будь ласка, заповніть Ім\'я та Email.')

    # Якщо це не POST (просто зайшов на сторінку) - нічого не робимо, 
    # або можна додати логіку для відображення форми, якщо вона на окремій сторінці.
    # Але оскільки у тебе SPA, форма вже є в HTML, тому просто редиректимо або рендеримо.
    return redirect('polls:index')
