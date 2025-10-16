from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View

# это домашняя страница
def home_page(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c3e50; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { text-decoration: none; color: #3498db; padding: 8px 16px; border: 1px solid #3498db; border-radius: 4px; }
            a:hover { background-color: #3498db; color: white; }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на главную страницу!</h1>
        <p>Это сайт</p>
        <ul>
            <li><a href="/about/">О нас</a></li>
            <li><a href="/student/1/">Профиль студента 1</a></li>
            <li><a href="/student/2/">Профиль студента 2</a></li>
            <li><a href="/student/3/">Профиль студента 3</a></li>
            <li><a href="/course/python-basics/">Курс Python Basics</a></li>
            <li><a href="/course/django-advanced/">Курс Django Advanced</a></li>
            <li><a href="/course/web-development/">Курс Web Development</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)
#это страничка "о нас"
def about_page(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>О нас</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c3e50; }
            a { text-decoration: none; color: #3498db; padding: 8px 16px; border: 1px solid #3498db; border-radius: 4px; }
            a:hover { background-color: #3498db; color: white; }
        </style>
    </head>
    <body>
        <h1>О нас</h1>
        <p>Это проект по вебу.</p>
        <p><a href="/">Вернуться на главную</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def student_profile(request, student_id):
    #ЭТО студенты, их надо мучить
    students = {
        1: {"name": "Иван Иванов", "group": "ммзи-01", "course": 2, "email": "ivan@edu.ru", "avatar": "👨‍🎓"},
        2: {"name": "Мария Петрова", "group": "ммзи-02", "course": 3, "email": "maria@edu.ru", "avatar": "👩‍🎓"},
        3: {"name": "Алексей Сидоров", "group": "ммзи-01", "course": 2, "email": "alex@edu.ru", "avatar": "👨‍💻"},
    }
    #это проиль студента
    student = students.get(student_id)
    if student:
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Профиль студента</title>
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    margin: 40px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    min-height: 100vh;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                }}
                .avatar {{
                    font-size: 80px;
                    text-align: center;
                    margin-bottom: 20px;
                }}
                h1 {{ 
                    text-align: center;
                    margin-bottom: 30px;
                    color: #feca57;
                }}
                .info {{ 
                    background: rgba(255, 255, 255, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                }}
                .info p {{
                    margin: 10px 0;
                    font-size: 1.1rem;
                }}
                a {{ 
                    display: inline-block;
                    text-decoration: none; 
                    color: #2c3e50; 
                    padding: 12px 30px; 
                    background: #feca57;
                    border-radius: 25px;
                    font-weight: bold;
                    transition: transform 0.3s ease;
                }}
                a:hover {{ 
                    transform: translateY(-3px);
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="avatar">{student['avatar']}</div>
                <h1>Профиль студента</h1>
                <div class="info">
                    <p><strong>ID:</strong> {student_id}</p>
                    <p><strong>Имя:</strong> {student['name']}</p>
                    <p><strong>Группа:</strong> {student['group']}</p>
                    <p><strong>Курс:</strong> {student['course']}</p>
                    <p><strong>Email:</strong> {student['email']}</p>
                </div>
                <p style="text-align: center;"><a href="/">🏠 Вернуться на главную</a></p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_content)
    else:
        raise Http404("Студент не найден")

# это все странички курсов
class CourseDetailView(View):
    def get(self, request, course_slug):
        courses = {
            "python-basics": {
                "title": "Python Basics",
                "description": "Изучите основы программирования на Python с нуля. От переменных до функций и ООП.",
                "duration": "36 часов",
                "level": "Начальный",
                "instructor": "Дмитрий Петров",
                "price": "Бесплатно",
                "students": "1250",
                "rating": "4.9",
                "icon": "🐍",
                "color": "#3776AB",
                "features": ["Основы синтаксиса", "Работа с данными", "Функции и модули", "ООП", "Проекты"]
            },
            "django-advanced": {
                "title": "Django Advanced",
                "description": "Продвинутые техники Django разработки: REST API, аутентификация, кэширование и оптимизация.",
                "duration": "48 часов",
                "level": "Продвинутый",
                "instructor": "Анна Сидорова",
                "price": "12 900 ₽",
                "students": "890",
                "rating": "4.8",
                "icon": "⚡",
                "color": "#0C4B33",
                "features": ["REST API", "Аутентификация", "Кэширование", "Оптимизация", "Deployment"]
            },
            "web-development": {
                "title": "Full Stack Web Development",
                "description": "Полный курс веб-разработки: от HTML/CSS до Django и React. Стань full-stack разработчиком!",
                "duration": "60 часов",
                "level": "Средний",
                "instructor": "Михаил Козлов",
                "price": "18 500 ₽",
                "students": "2100",
                "rating": "4.7",
                "icon": "🚀",
                "color": "#FF6B6B",
                "features": ["HTML/CSS", "JavaScript", "Django", "React", "Базы данных"]
            },
            "data-science": {
                "title": "Data Science Fundamentals",
                "description": "Основы анализа данных и машинного обучения на Python. Pandas, NumPy, Scikit-learn и визуализация.",
                "duration": "42 часа",
                "level": "Средний",
                "instructor": "Елена Васнецова",
                "price": "15 000 ₽",
                "students": "760",
                "rating": "4.9",
                "icon": "📊",
                "color": "#9B59B6",
                "features": ["Pandas/NumPy", "Визуализация", "ML основы", "Статистика", "Проекты"]
            }
        }
        
        course = courses.get(course_slug)
        if course:
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>{course['title']} - Подробности курса</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
                    
                    * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }}
                    
                    body {{
                        font-family: 'Inter', sans-serif;
                        background: linear-gradient(135deg, {course['color']}22, #ffffff);
                        color: #2c3e50;
                        min-height: 100vh;
                        padding: 20px;
                    }}
                    
                    .container {{
                        max-width: 1000px;
                        margin: 0 auto;
                    }}
                    
                    .header {{
                        text-align: center;
                        margin-bottom: 40px;
                        padding: 40px 0;
                    }}
                    
                    .course-icon {{
                        font-size: 80px;
                        margin-bottom: 20px;
                        animation: bounce 2s infinite;
                    }}
                    
                    @keyframes bounce {{
                        0%, 100% {{ transform: translateY(0); }}
                        50% {{ transform: translateY(-10px); }}
                    }}
                    
                    .course-title {{
                        font-size: 3rem;
                        font-weight: 700;
                        margin-bottom: 10px;
                        background: linear-gradient(45deg, {course['color']}, #2c3e50);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                    }}
                    
                    .course-description {{
                        font-size: 1.3rem;
                        color: #5a6c7d;
                        max-width: 600px;
                        margin: 0 auto 30px;
                        line-height: 1.6;
                    }}
                    
                    .course-grid {{
                        display: grid;
                        grid-template-columns: 2fr 1fr;
                        gap: 30px;
                        margin-bottom: 40px;
                    }}
                    
                    @media (max-width: 768px) {{
                        .course-grid {{
                            grid-template-columns: 1fr;
                        }}
                    }}
                    
                    .info-card {{
                        background: white;
                        padding: 30px;
                        border-radius: 20px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
                        border-left: 5px solid {course['color']};
                    }}
                    
                    .stats-card {{
                        background: linear-gradient(135deg, {course['color']}, {course['color']}dd);
                        color: white;
                        padding: 30px;
                        border-radius: 20px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    }}
                    
                    .section-title {{
                        font-size: 1.5rem;
                        font-weight: 600;
                        margin-bottom: 20px;
                        color: {course['color']};
                    }}
                    
                    .stats-title {{
                        font-size: 1.5rem;
                        font-weight: 600;
                        margin-bottom: 20px;
                        color: white;
                    }}
                    
                    .info-item {{
                        display: flex;
                        align-items: center;
                        margin-bottom: 15px;
                        padding: 10px 0;
                        border-bottom: 1px solid #f0f0f0;
                    }}
                    
                    .info-label {{
                        font-weight: 500;
                        min-width: 120px;
                        color: #5a6c7d;
                    }}
                    
                    .info-value {{
                        font-weight: 600;
                        color: #2c3e50;
                    }}
                    
                    .stats-grid {{
                        display: grid;
                        gap: 15px;
                    }}
                    
                    .stat-item {{
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        padding: 15px;
                        background: rgba(255,255,255,0.1);
                        border-radius: 10px;
                        backdrop-filter: blur(10px);
                    }}
                    
                    .stat-value {{
                        font-size: 1.5rem;
                        font-weight: 700;
                    }}
                    
                    .features-section {{
                        background: white;
                        padding: 40px;
                        border-radius: 20px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
                        margin-bottom: 40px;
                    }}
                    
                    .features-grid {{
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                        gap: 15px;
                        margin-top: 20px;
                    }}
                    
                    .feature-item {{
                        background: {course['color']}11;
                        padding: 15px;
                        border-radius: 10px;
                        text-align: center;
                        border: 1px solid {course['color']}33;
                        transition: transform 0.3s ease;
                    }}
                    
                    .feature-item:hover {{
                        transform: translateY(-5px);
                        background: {course['color']}22;
                    }}
                    
                    .cta-section {{
                        text-align: center;
                        padding: 40px;
                        background: linear-gradient(135deg, {course['color']}, {course['color']}dd);
                        color: white;
                        border-radius: 20px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    }}
                    
                    .price {{
                        font-size: 3rem;
                        font-weight: 700;
                        margin: 20px 0;
                    }}
                    
                    .enroll-button {{
                        display: inline-block;
                        padding: 15px 40px;
                        font-size: 1.2rem;
                        font-weight: 600;
                        background: white;
                        color: {course['color']};
                        text-decoration: none;
                        border-radius: 50px;
                        transition: all 0.3s ease;
                        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
                    }}
                    
                    .enroll-button:hover {{
                        transform: translateY(-3px);
                        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    }}
                    
                    .home-button {{
                        display: inline-block;
                        margin-top: 20px;
                        padding: 12px 30px;
                        background: rgba(255,255,255,0.2);
                        color: white;
                        text-decoration: none;
                        border-radius: 25px;
                        border: 2px solid rgba(255,255,255,0.3);
                        transition: all 0.3s ease;
                    }}
                    
                    .home-button:hover {{
                        background: rgba(255,255,255,0.3);
                    }}
                    
                    .badge {{
                        display: inline-block;
                        padding: 5px 15px;
                        background: {course['color']};
                        color: white;
                        border-radius: 20px;
                        font-size: 0.8rem;
                        font-weight: 600;
                        margin-left: 10px;
                    }}
                    
                    .instructor {{
                        display: flex;
                        align-items: center;
                        margin-top: 20px;
                        padding-top: 20px;
                        border-top: 1px solid #f0f0f0;
                    }}
                    
                    .instructor-avatar {{
                        width: 50px;
                        height: 50px;
                        background: {course['color']};
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        color: white;
                        font-weight: bold;
                        margin-right: 15px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <div class="course-icon">{course['icon']}</div>
                        <h1 class="course-title">{course['title']}</h1>
                        <p class="course-description">{course['description']}</p>
                    </div>
                    
                    <div class="course-grid">
                        <div class="info-card">
                            <h2 class="section-title">📋 Детали курса</h2>
                            <div class="info-item">
                                <span class="info-label">Уровень:</span>
                                <span class="info-value">{course['level']} <span class="badge">{course['icon']}</span></span>
                            </div>
                            <div class="info-item">
                                <span class="info-label">Продолжительность:</span>
                                <span class="info-value">{course['duration']}</span>
                            </div>
                            <div class="info-item">
                                <span class="info-label">Формат:</span>
                                <span class="info-value">Онлайн • Практика • Проекты</span>
                            </div>
                            <div class="info-item">
                                <span class="info-label">Сертификат:</span>
                                <span class="info-value">✅ Выдается после завершения</span>
                            </div>
                            
                            <div class="instructor">
                                <div class="instructor-avatar">
                                    {course['instructor'].split(' ')[0][0]}{course['instructor'].split(' ')[1][0]}
                                </div>
                                <div>
                                    <div style="font-weight: 600;">{course['instructor']}</div>
                                    <div style="color: #5a6c7d; font-size: 0.9rem;">Преподаватель курса</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="stats-card">
                            <h2 class="stats-title">📊 Статистика</h2>
                            <div class="stats-grid">
                                <div class="stat-item">
                                    <span>Студентов:</span>
                                    <span class="stat-value">{course['students']}</span>
                                </div>
                                <div class="stat-item">
                                    <span>Рейтинг:</span>
                                    <span class="stat-value">{course['rating']}/5.0</span>
                                </div>
                                <div class="stat-item">
                                    <span>Уроков:</span>
                                    <span class="stat-value">{course['duration'].split(' ')[0]}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="features-section">
                        <h2 class="section-title">🎯 Что вы узнаете</h2>
                        <div class="features-grid">
            """
            
            # Добавляем фичи курса
            for feature in course['features']:
                html_content += f"""
                            <div class="feature-item">
                                <div style="font-size: 1.5rem; margin-bottom: 8px;">✅</div>
                                <div style="font-weight: 500;">{feature}</div>
                            </div>
                """
            
            html_content += f"""
                        </div>
                    </div>
                    
                    <div class="cta-section">
                        <h2 style="font-size: 2rem; margin-bottom: 10px;">Готовы начать?</h2>
                        <p style="font-size: 1.1rem; opacity: 0.9;">Присоединяйтесь к {course['students']}+ студентам уже сегодня!</p>
                        <div class="price">{course['price']}</div>
                        <a href="#" class="enroll-button">🚀 Записаться на курс</a>
                        <br>
                        <a href="/" class="home-button">← Вернуться на главную</a>
                    </div>
                </div>
                
                <script>
                    // Анимация появления элементов
                    document.addEventListener('DOMContentLoaded', function() {{
                        const elements = document.querySelectorAll('.info-card, .stats-card, .features-section, .cta-section');
                        elements.forEach((element, index) => {{
                            element.style.opacity = '0';
                            element.style.transform = 'translateY(20px)';
                            
                            setTimeout(() => {{
                                element.style.transition = 'all 0.6s ease';
                                element.style.opacity = '1';
                                element.style.transform = 'translateY(0)';
                            }}, index * 200);
                        }});
                    }});
                    
                    // Интерактивность для кнопки записи
                    const enrollButton = document.querySelector('.enroll-button');
                    if (enrollButton) {{
                        enrollButton.addEventListener('click', function(e) {{
                            e.preventDefault();
                            this.innerHTML = '🎉 Вы записаны!';
                            this.style.background = '#27ae60';
                            this.style.color = 'white';
                            
                            // Создаем конфетти-эффект
                            for (let i = 0; i < 50; i++) {{
                                setTimeout(() => {{
                                    const confetti = document.createElement('div');
                                    confetti.innerHTML = '🎉';
                                    confetti.style.position = 'fixed';
                                    confetti.style.left = Math.random() * 100 + 'vw';
                                    confetti.style.top = '-50px';
                                    confetti.style.fontSize = (Math.random() * 20 + 10) + 'px';
                                    confetti.style.zIndex = '1000';
                                    confetti.style.pointerEvents = 'none';
                                    document.body.appendChild(confetti);
                                    
                                    // Анимация падения
                                    confetti.animate([
                                        {{ transform: 'translateY(0) rotate(0deg)', opacity: 1 }},
                                        {{ transform: `translateY(${{window.innerHeight}}px) rotate(${{Math.random() * 360}}deg)`, opacity: 0 }}
                                    ], {{
                                        duration: Math.random() * 3000 + 2000,
                                        easing: 'cubic-bezier(0.1, 0.8, 0.2, 1)'
                                    }}).onfinish = () => confetti.remove();
                                }}, i * 100);
                            }}
                        }});
                    }}
                </script>
            </body>
            </html>
            """
            return HttpResponse(html_content)
        else:
            raise Http404("Курс не найден")




#ну тут все легко, тут функция состоит просто из одного хтмл тела
def custom_404(request, exception):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Страница не найдена</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
            h1 { color: #e74c3c; }
            a { text-decoration: none; color: #3498db; padding: 8px 16px; border: 1px solid #3498db; border-radius: 4px; }
            a:hover { background-color: #3498db; color: white; }
        </style>
    </head>
    <body>
        <h1>404 - Страница не найдена</h1>
        <p>Извините, запрашиваемая страница не существует.</p>
        <p><a href="/">Вернуться на главную</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_content, status=404)