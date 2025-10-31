from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from django.contrib import messages
from .forms import FeedbackForm, RegistrationForm
from .forms import FeedbackForm, RegistrationForm, LoginForm  
# Данные для студентов и курсов
STUDENTS_DATA = {
    1: {
        'info': 'Иван Петров',
        'faculty': 'Кибербезопасность',
        'status': 'Активный',
        'year': 3,
        'email': 'ivan@edu.ru',
        'avatar': '👨‍🎓'
    },
    2: {
        'info': 'Мария Сидорова', 
        'faculty': 'Информатика',
        'status': 'Активный',
        'year': 2,
        'email': 'maria@edu.ru',
        'avatar': '👩‍🎓'
    },
    3: {
        'info': 'Алексей Козлов',
        'faculty': 'Программная инженерия', 
        'status': 'Выпускник',
        'year': 5,
        'email': 'alex@edu.ru',
        'avatar': '👨‍💻'
    }
}

COURSES_DATA = {
    'python-basics': {
        'name': 'Основы программирования на Python',
        'duration': 36,
        'description': 'Базовый курс по программированию на языке Python для начинающих.',
        'instructor': 'Доцент Петров И.С.',
        'level': 'Начальный',
        'price': 'Бесплатно',
        'students': '1250',
        'rating': '4.9',
        'icon': '🐍'
    },
    'web-security': {
        'name': 'Веб-безопасность',
        'duration': 48,
        'description': 'Курс по защите веб-приложений от современных угроз.',
        'instructor': 'Профессор Сидоров А.В.',
        'level': 'Продвинутый',
        'price': '12 900 ₽',
        'students': '890',
        'rating': '4.8',
        'icon': '🛡️'
    },
    'network-defense': {
        'name': 'Защита сетей',
        'duration': 42,
        'description': 'Изучение методов и технологий защиты компьютерных сетей.',
        'instructor': 'Доцент Козлова М.П.',
        'level': 'Средний',
        'price': '9 500 ₽',
        'students': '760',
        'rating': '4.7',
        'icon': '🌐'
    }
}

# Function-Based Views
def home_page(request):
    return render(request, 'fefu_lab/home.html', {
        'title': 'Главная страница',
        'heading': 'Добро пожаловать в FEFU Lab!'
    })

def about_page(request):
    return render(request, 'fefu_lab/about.html', {
        'title': 'О нас',
        'heading': 'О нашем проекте'
    })

def student_profile(request, student_id):
    if student_id in STUDENTS_DATA:
        student_data = STUDENTS_DATA[student_id]
        return render(request, 'fefu_lab/student_profile.html', {
            'title': f'Студент {student_data["info"]}',
            'heading': f'Профиль студента',
            'student_id': student_id,
            'student_info': student_data['info'],
            'faculty': student_data['faculty'],
            'status': student_data['status'],
            'year': student_data['year'],
            'email': student_data['email'],
            'avatar': student_data['avatar']
        })
    else:
        raise Http404("Студент с таким ID не найден")

# Class-Based Views
class CourseDetailView(View):
    def get(self, request, course_slug):
        if course_slug in COURSES_DATA:
            course_data = COURSES_DATA[course_slug]
            return render(request, 'fefu_lab/course_detail.html', {
                'title': course_data['name'],
                'heading': course_data['name'],
                'course_slug': course_slug,
                'course': course_data
            })
        else:
            raise Http404("Курс не найден")

# Новые представления для форм
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # В реальном приложении здесь бы сохранялись данные в БД
            return render(request, 'fefu_lab/success.html', {
                'title': 'Успех!',
                'heading': 'Сообщение отправлено!',
                'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.'
            })
    else:
        form = FeedbackForm()
    
    return render(request, 'fefu_lab/feedback.html', {
        'title': 'Обратная связь',
        'heading': 'Форма обратной связи',
        'form': form
    })

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # В реальном приложении здесь бы создавался пользователь
            return render(request, 'fefu_lab/success.html', {
                'title': 'Успех!',
                'heading': 'Регистрация завершена!',
                'message': 'Поздравляем! Вы успешно зарегистрировались в системе.'
            })
    else:
        form = RegistrationForm()
    
    return render(request, 'fefu_lab/register.html', {
        'title': 'Регистрация',
        'heading': 'Регистрация нового пользователя',
        'form': form
    })
# Добавьте эту функцию в views.py
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # В реальном приложении здесь бы проверялись учетные данные в БД
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Простая имитация проверки (в реальном приложении используйте authenticate())
            if username == "demo" and password == "Demo123!":
                return render(request, 'fefu_lab/success.html', {
                    'title': 'Успешный вход!',
                    'heading': 'Добро пожаловать!',
                    'message': f'Рады видеть вас снова, {username}! Вы успешно вошли в систему.'
                })
            else:
                form.add_error(None, "Неверный логин или пароль. Для демо используйте: логин 'demo', пароль 'Demo123!'")
    
    else:
        form = LoginForm()
    
    return render(request, 'fefu_lab/login.html', {
        'title': 'Вход в систему',
        'heading': 'Вход в систему',
        'form': form
    })
# Обработчик для несуществующих страниц
def custom_404(request, exception):
    return render(request, 'fefu_lab/404.html', status=404)