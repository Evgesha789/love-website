from flask import Flask, render_template, request, session, redirect, url_for
import os
from datetime import datetime
import threading
from pyngrok import ngrok  # ← ДОБАВЬ ЭТУ СТРОЧКУ

app = Flask(__name__)
app.secret_key = 'наш-секретный-ключ-любви'

# 🔧 ДОБАВЬ ЭТОТ КОД ДО ВСЕХ @app.route
def start_tunnel():
    try:
        # Ждем немного чтобы Flask успел запуститься
        import time
        time.sleep(2)
        
        # Открываем туннель к порту 5000
        public_url = ngrok.connect(5000)
        print("\n" + "🎉" * 50)
        print("🎉 ВАШ САЙТ ДОСТУПЕН ИЗ ИНТЕРНЕТА! 🎉")
        print("🎉" * 50)
        print(f"🌐 ССЫЛКА ДЛЯ ЛЮБИМОГО: {public_url}")
        print("📱 Отправь эту ссылку своему парню в Telegram или WhatsApp!")
        print("💖 Он сможет открыть сайт с любого устройства!")
        print("⚠️  Ссылка работает ~2 часа (бесплатно)")
        print("\n")
        
    except Exception as e:
        print(f"❌ Не удалось создать туннель: {e}")
        print("💡 Совет: Перезапусти приложение через пару минут")

# Запускаем туннель в фоне
tunnel_thread = threading.Thread(target=start_tunnel)
tunnel_thread.daemon = True
tunnel_thread.start()

# Ваша особенная дата ❤️
SECRET_CODE = "02102023"

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Медианомер - Наше место любви</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
                font-family: 'Playfair Display', serif;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 25px;
                padding: 50px 40px;
                text-align: center;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                border: 2px solid #ff6b8b;
                max-width: 600px;
                width: 100%;
                position: relative;
                overflow: hidden;
            }
            
            .container::before {
                content: "❤️";
                position: absolute;
                top: -30px;
                right: -30px;
                font-size: 150px;
                opacity: 0.1;
                transform: rotate(15deg);
            }
            
            .hearts {
                font-size: 40px;
                margin-bottom: 20px;
                animation: float 3s ease-in-out infinite;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3.5em;
                color: #ff6b8b;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }
            
            .subtitle {
                font-size: 1.3em;
                color: #666;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 18px 45px;
                font-size: 1.3em;
                border-radius: 50px;
                cursor: pointer;
                transition: all 0.3s ease;
                font-family: 'Playfair Display', serif;
                font-weight: bold;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
                margin-top: 20px;
            }
            
            .romantic-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
            
            .flower {
                font-size: 30px;
                margin: 0 5px;
                animation: spin 4s linear infinite;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hearts">
                💖✨🌸
            </div>
            
            <h1>Медианомер</h1>
            
            <div class="subtitle">
                Наше особое место любви<br>
                <em>Завтра особенный день...</em>
            </div>
            
            <div style="margin: 30px 0;">
                <span class="flower">🌹</span>
                <span class="flower">🌸</span>
                <span class="flower">💐</span>
            </div>
            
            <p style="color: #888; margin-bottom: 20px; font-style: italic;">
                Нажми на кнопку, чтобы увидеть нашу историю
            </p>
            
            <button class="romantic-btn" onclick="location.href='/secret'">
                💖 Открыть нашу любовь
            </button>
        </div>
    </body>
    </html>
    '''

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    if request.method == 'POST':
        code = request.form['code']
        if code == SECRET_CODE:
            session['allowed'] = True
            return redirect('/love-story')
        else:
            return '''
            <html>
            <head>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
                    
                    body {
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        font-family: 'Playfair Display', serif;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        min-height: 100vh;
                        padding: 20px;
                    }
                    
                    .error-box {
                        background: rgba(255,255,255,0.95);
                        padding: 40px;
                        border-radius: 20px;
                        text-align: center;
                        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                        border: 2px solid #ff6b8b;
                    }
                    
                    h2 {
                        color: #ff6b8b;
                        margin-bottom: 20px;
                    }
                    
                    .romantic-btn {
                        background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                        color: white;
                        border: none;
                        padding: 12px 30px;
                        border-radius: 25px;
                        cursor: pointer;
                        font-family: 'Playfair Display', serif;
                        margin-top: 20px;
                    }
                </style>
            </head>
            <body>
                <div class="error-box">
                    <h2>❌ Неверный код, любимый!</h2>
                    <p>Подсказка: наша дата в формате ДДММГГГГ</p>
                    <p><em>День, когда началась наша сказка...</em></p>
                    <button class="romantic-btn" onclick="location.href='/secret'">
                        Попробовать снова
                    </button>
                </div>
            </body>
            </html>
            '''
    
    return '''
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                font-family: 'Playfair Display', serif;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 20px;
            }
            
            .secret-box {
                background: rgba(255,255,255,0.95);
                padding: 50px 40px;
                border-radius: 25px;
                text-align: center;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                border: 2px solid #ff6b8b;
                max-width: 500px;
                width: 100%;
            }
            
            h2 {
                font-family: 'Dancing Script', cursive;
                font-size: 2.5em;
                color: #ff6b8b;
                margin-bottom: 10px;
            }
            
            .subtitle {
                color: #666;
                margin-bottom: 30px;
                font-style: italic;
            }
            
            input {
                font-size: 18px;
                padding: 15px 20px;
                border: 2px solid #ff6b8b;
                border-radius: 50px;
                margin: 10px;
                text-align: center;
                font-family: 'Playfair Display', serif;
                width: 200px;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                font-weight: bold;
                margin-top: 20px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
            }
            
            .romantic-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="secret-box">
            <h2>🔐 Наш секретный код</h2>
            <div class="subtitle">
                Введи нашу особую дату<br>
                <small>Подсказка: день, когда началась наша любовь</small>
            </div>
            
            <form method="POST">
                <input type="text" name="code" placeholder="ДДММГГГГ" required>
                <br>
                <button class="romantic-btn" type="submit">
                    💝 Открыть историю любви
                </button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/love-story')
def love_story():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
                font-family: 'Playfair Display', serif;
                min-height: 100vh;
                padding: 40px 20px;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            
            .anniversary-header {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                padding: 40px 30px;
                border-radius: 25px;
                text-align: center;
                margin-bottom: 30px;
                box-shadow: 0 15px 35px rgba(255, 107, 139, 0.3);
                position: relative;
                overflow: hidden;
            }
            
            .anniversary-header::before {
                content: "💖✨";
                position: absolute;
                top: 10px;
                left: 10px;
                font-size: 40px;
                opacity: 0.3;
            }
            
            .anniversary-header::after {
                content: "🌸💕";
                position: absolute;
                bottom: 10px;
                right: 10px;
                font-size: 40px;
                opacity: 0.3;
            }
            
            .anniversary-title {
                font-family: 'Dancing Script', cursive;
                font-size: 3em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            
            .anniversary-date {
                font-size: 1.3em;
                margin-bottom: 10px;
                opacity: 0.9;
            }
            
            .anniversary-days {
                font-size: 1.1em;
                opacity: 0.8;
            }
            
            .memory {
                background: rgba(255, 255, 255, 0.95);
                margin: 25px 0;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                border-left: 5px solid #ff6b8b;
                transition: transform 0.3s ease;
            }
            
            .memory:hover {
                transform: translateX(10px);
            }
            
            .memory h3 {
                color: #ff6b8b;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-family: 'Dancing Script', cursive;
            }
            
            .memory p {
                color: #666;
                line-height: 1.6;
                font-size: 1.1em;
            }
            
            .memory-date {
                background: #ff6b8b;
                color: white;
                padding: 5px 15px;
                border-radius: 15px;
                font-size: 0.9em;
                display: inline-block;
                margin-bottom: 10px;
            }
            
            .buttons {
                text-align: center;
                margin-top: 40px;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 0 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
                transition: all 0.3s ease;
            }
            
            .romantic-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
            
            .section-title {
                font-family: 'Dancing Script', cursive;
                font-size: 2.5em;
                color: #ff6b8b;
                text-align: center;
                margin: 40px 0 20px 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }

            .menu-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }

            .menu-item {
                background: rgba(255, 255, 255, 0.9);
                padding: 30px 20px;
                border-radius: 20px;
                text-align: center;
                text-decoration: none;
                color: #ff6b8b;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
                border: 2px solid transparent;
            }

            .menu-item:hover {
                transform: translateY(-5px);
                border-color: #ff6b8b;
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.3);
            }

            .menu-icon {
                font-size: 2.5em;
                margin-bottom: 10px;
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="anniversary-header">
                <div class="anniversary-title">2 ГОДА ЛЮБВИ!</div>
                <div class="anniversary-date">02.10.2023 - 02.10.2025</div>
                <div class="anniversary-days">731 день счастья вместе! 💖</div>
            </div>
            
            <div class="section-title">Наша история любви</div>
            
            <div class="memory">
                <div class="memory-date">02.10.2023</div>
                <h3>Начало нашей сказки</h3>
                <p>День, когда началась наша прекрасная история... Тот самый момент, когда наши сердца поняли, что нашли друг друга.</p>
            </div>
            
            <div class="memory">
                <div class="memory-date">11.10.2023</div>
                <h3>Первый раз в кино втроем</h3>
                <p>А помнишь как втроем ходили впервые в кино? 😂 Такой веселый и неловкий момент, который положил начало нашим совместным приключениям!</p>
            </div>
            
            <div class="memory">
                <div class="memory-date">30.10.2023</div>
                <h3>Зимнее веселье</h3>
                <p>А помнишь как ты меня кинул в сугроб? 😂 Холодный снег, горячий шоколад потом и море смеха - идеальный зимний день!</p>
            </div>

            <div class="memory">
                <div class="memory-date">Наше начало</div>
                <h3>Первое эстетик-фото</h3>
                <p>Тот самый момент, когда мы сделали наше первое красивое фото вместе. Кадр, который захватил магию наших чувств.</p>
            </div>

            <div class="memory">
                <div class="memory-date">Романтический вечер</div>
                <h3>Прогулка на смотровую</h3>
                <p>А нашу прогулку на смотровую? Вид был потрясающий! Город огней под нами, а в сердцах - бесконечное счастье.</p>
            </div>

            <div class="memory">
                <div class="memory-date">Первое путешествие</div>
                <h3>Поездка в Челябинск</h3>
                <p>А первая поездка в Челябинск? Столько эмоций! Дорога, которая сблизила нас еще больше.</p>
            </div>

            <div class="memory">
                <div class="memory-date">Первые цветы</div>
                <h3>Первые цветочки</h3>
                <p>Те самые первые цветы, которые растопили мое сердце. Простой жест, который означал так много...</p>
            </div>

            <div class="memory">
                <div class="memory-date">Июнь 2024</div>
                <h3>Летние деньки</h3>
                <p>Теплые июньские вечера, наполненные любовью... Солнечные дни, которые мы провели вместе, создавая наши воспоминания.</p>
            </div>

            <div class="section-title">Наши особенные моменты</div>

            <div class="menu-grid">
                <a href="/photos" class="menu-item">
                    <span class="menu-icon">📸</span>
                    Наши фото
                </a>
                <a href="/music" class="menu-item">
                    <span class="menu-icon">🎵</span>
                    Наши песни
                </a>
                <a href="/puzzle" class="menu-item">
                    <span class="menu-icon">🧩</span>
                    Пазл любви
                </a>
                <a href="/videos" class="menu-item">
                    <span class="menu-icon">🎥</span>
                    Наши видео
                </a>
                <a href="/letter" class="menu-item">
                    <span class="menu-icon">💌</span>
                    Письмо любви
                </a>
            </div>

            <div class="buttons">
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/photos')
def photos():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <title>Наши фото - Медианомер</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
                font-family: 'Playfair Display', serif;
                padding: 40px 20px;
                min-height: 100vh;
                margin: 0;
            }
            
            .container {
                max-width: 1000px;
                margin: 0 auto;
            }
            
            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3em;
                color: #ff6b8b;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }
            
            .photo-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 25px;
                margin: 30px 0;
            }
            
            .photo-item {
                background: rgba(255, 255, 255, 0.95);
                padding: 20px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            
            .photo-item:hover {
                transform: translateY(-8px);
                border-color: #ff6b8b;
                box-shadow: 0 20px 40px rgba(255, 107, 139, 0.3);
            }
            
            .photo-real {
                width: 100%;
                height: 250px;
                margin: 0 auto 15px;
                border-radius: 15px;
                object-fit: cover;
                border: 3px solid #ff6b8b;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }
            
            .photo-date {
                background: #ff6b8b;
                color: white;
                padding: 8px 15px;
                border-radius: 15px;
                font-size: 0.9em;
                display: inline-block;
                margin-bottom: 12px;
                font-weight: bold;
            }
            
            .photo-title {
                color: #ff6b8b;
                font-weight: bold;
                font-size: 1.3em;
                margin: 12px 0;
                font-family: 'Dancing Script', cursive;
            }
            
            .photo-description {
                color: #666;
                font-size: 1em;
                line-height: 1.5;
                font-style: italic;
                margin: 0;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
                transition: all 0.3s ease;
            }
            
            .romantic-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
            
            .buttons {
                text-align: center;
                margin-top: 40px;
            }
            
            .memory-counter {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
                font-style: italic;
                font-size: 1.1em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📸 Наши незабываемые моменты</h1>
            
            <div class="memory-counter">
                💝 7 особенных воспоминаний, которые греют душу...
            </div>
            
            <div class="photo-grid">
                <!-- Первый поход в кино -->
                <div class="photo-item">
                    <div class="photo-date">11.10.23</div>
                    <img src="/static/photos/kino.jpg" alt="Первый раз в кино" class="photo-real">
                    <div class="photo-title">Первый раз в кино втроем</div>
                    <div class="photo-description">"А помнишь как втроем ходили впервые в кино? 😂"</div>
                </div>
                
                <!-- Сугроб -->
                <div class="photo-item">
                    <div class="photo-date">30.10.23</div>
                    <img src="/static/photos/sugrob.jpg" alt="Зимнее веселье" class="photo-real">
                    <div class="photo-title">Зимнее веселье</div>
                    <div class="photo-description">"А помнишь как ты меня кинул в сугроб? 😂"</div>
                </div>
                
                <!-- Первое эстетик-фото -->
                <div class="photo-item">
                    <div class="photo-date">Наше начало</div>
                    <img src="/static/photos/estetik.jpg" alt="Первое эстетик-фото" class="photo-real">
                    <div class="photo-title">Первое эстетик-фото</div>
                    <div class="photo-description">"Тот самый момент, когда все началось..."</div>
                </div>
                
                <!-- Смотровая -->
                <div class="photo-item">
                    <div class="photo-date">Романтический вечер</div>
                    <img src="/static/photos/smotrovaya.jpg" alt="Прогулка на смотровую" class="photo-real">
                    <div class="photo-title">Прогулка на смотровую</div>
                    <div class="photo-description">"А нашу прогулку на смотровую? Вид был потрясающий!"</div>
                </div>
                
                <!-- Челябинск -->
                <div class="photo-item">
                    <div class="photo-date">Первое путешествие</div>
                    <img src="/static/photos/chelyabinsk.jpg" alt="Поездка в Челябинск" class="photo-real">
                    <div class="photo-title">Поездка в Челябинск</div>
                    <div class="photo-description">"А первая поездка в Челябинск? Столько эмоций!"</div>
                </div>
                
                <!-- Цветочки -->
                <div class="photo-item">
                    <div class="photo-date">Первые цветы</div>
                    <img src="/static/photos/cvetochki.jpg" alt="Первые цветочки" class="photo-real">
                    <div class="photo-title">Первые цветочки</div>
                    <div class="photo-description">"Те самые первые цветы, которые растопили мое сердце"</div>
                </div>
                
                <!-- Июнь -->
                <div class="photo-item">
                    <div class="photo-date">Июнь</div>
                    <img src="/static/photos/iyun.jpg" alt="Летние деньки" class="photo-real">
                    <div class="photo-title">Летние деньки</div>
                    <div class="photo-description">"Теплые июньские вечера, наполненные любовью..."</div>
                </div>
            </div>
            
            <div class="buttons">
                <button class="romantic-btn" onclick="location.href='/love-story'">
                    ← Назад к истории
                </button>
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/music')
def music():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: 'Playfair Display', serif;
                padding: 40px 20px;
                min-height: 100vh;
                color: white;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            
            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3em;
                text-align: center;
                margin-bottom: 40px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .song-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 30px;
                border-radius: 20px;
                margin: 30px 0;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                border: 1px solid rgba(255,255,255,0.2);
            }
            
            .song-title {
                font-size: 1.8em;
                margin-bottom: 10px;
                color: #ff6b8b;
            }
            
            .song-artist {
                font-style: italic;
                margin-bottom: 20px;
                opacity: 0.9;
            }
            
            .song-album {
                color: #ccc;
                font-size: 0.9em;
                margin-bottom: 15px;
            }
            
            .lyrics {
                line-height: 1.8;
                margin: 20px 0;
                font-size: 1.1em;
            }
            
            .audio-player {
                width: 100%;
                margin: 20px 0;
                border-radius: 25px;
                background: #333;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
            }
            
            .buttons {
                text-align: center;
                margin-top: 40px;
            }
            
            .quote {
                text-align: center;
                font-style: italic;
                margin: 30px 0;
                font-size: 1.2em;
                opacity: 0.9;
            }
            
            .success-message {
                background: rgba(76, 175, 80, 0.3);
                color: #a5d6a7;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin: 20px 0;
                border: 1px solid #4CAF50;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎵 Наши песни</h1>
            
            <div class="success-message">
                ✅ Музыка загружена! Наслаждайтесь нашими песнями!
            </div>
            
            <div class="quote">
                "Музыка, которая описывает нашу любовь..."
            </div>
            
            <div class="song-card">
                <div class="song-title">"Фары"</div>
                <div class="song-artist">Пицца</div>
                <div class="song-album">Саундтрек к сериалу</div>
                
                <div style="text-align: center; margin: 20px 0;">
                    <audio controls class="audio-player">
                        <source src="/static/music/fary-pizza.mp3" type="audio/mpeg">
                        Ваш браузер не поддерживает аудио элемент
                    </audio>
                </div>
                
                <div class="lyrics">
                    <p>🎵 Песня о наших путешествиях и дорогах вместе...</p>
                    <p><em>
                    "Фары освещают путь домой,<br>
                    Ты рядом со мной, и мы с тобой...<br>
                    Вместе сквозь ночь, вместе навсегда,<br>
                    Наша любовь - вот она, вот где!"
                    </em></p>
                </div>
            </div>
            
            <div class="song-card">
                <div class="song-title">"Прости"</div>
                <div class="song-artist">Интонация</div>
                <div class="song-album">Молодёжка-2. Новые победы</div>
                
                <div style="text-align: center; margin: 20px 0;">
                    <audio controls class="audio-player">
                        <source src="/static/music/prosti-intonacia.mp3" type="audio/mpeg">
                        Ваш браузер не поддерживает аудио элемент
                    </audio>
                </div>
                
                <div class="lyrics">
                    <p>🎵 Песня о понимании и прощении в отношениях...</p>
                    <p><em>
                    "Прости за все, что было и прошло,<br>
                    Любовь сильнее, чем любое зло...<br>
                    Ты в моем сердце навсегда останешься,<br>
                    И наша связь никогда не прервется."
                    </em></p>
                </div>
            </div>
            
            <div class="buttons">
                <button class="romantic-btn" onclick="location.href='/love-story'">
                    ← Назад к истории
                </button>
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/videos')
def videos():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
                font-family: 'Playfair Display', serif;
                padding: 40px 20px;
                min-height: 100vh;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            
            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3em;
                color: #ff6b8b;
                text-align: center;
                margin-bottom: 30px;
            }
            
            .video-item {
                background: rgba(255, 255, 255, 0.95);
                padding: 25px;
                border-radius: 20px;
                margin: 25px 0;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
                text-align: center;
            }
            
            .video-player {
                width: 100%;
                max-width: 600px;
                height: 340px;
                border-radius: 15px;
                margin: 15px 0;
                border: 3px solid #ff6b8b;
            }
            
            .video-title {
                color: #ff6b8b;
                font-size: 1.4em;
                margin: 15px 0;
                font-family: 'Dancing Script', cursive;
            }
            
            .video-description {
                color: #666;
                font-size: 1em;
                line-height: 1.5;
                font-style: italic;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
            }
            
            .buttons {
                text-align: center;
                margin-top: 40px;
            }
            
            .success-message {
                background: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin: 20px 0;
                color: #4CAF50;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎥 Наши видео</h1>
            
            <div class="success-message">
                ✅ Видео загружены! Смотрите наши особенные моменты!
            </div>
            
            <div class="video-item">
                <div class="video-title">Башня</div>
                <video controls class="video-player">
                    <source src="/static/videos/bashnya.mp4" type="video/mp4">
                    Ваш браузер не поддерживает видео элемент
                </video>
                <div class="video-description">
                    Наше видео у башни - особенный момент...
                </div>
            </div>
            
            <div class="video-item">
                <div class="video-title">Челябинск</div>
                <video controls class="video-player">
                    <source src="/static/videos/chelyabinsk.mp4" type="video/mp4">
                    Ваш браузер не поддерживает видео элемент
                </video>
                <div class="video-description">
                    Воспоминания из нашей поездки в Челябинск...
                </div>
            </div>
            
            <div class="buttons">
                <button class="romantic-btn" onclick="location.href='/love-story'">
                    ← Назад к истории
                </button>
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/puzzle')
def puzzle():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
                font-family: 'Playfair Display', serif;
                padding: 40px 20px;
                min-height: 100vh;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
                text-align: center;
            }
            
            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3em;
                color: #ff6b8b;
                margin-bottom: 20px;
            }
            
            .puzzle-section {
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 20px;
                margin: 30px 0;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            }
            
            .puzzle-title {
                color: #ff6b8b;
                font-size: 1.5em;
                margin-bottom: 20px;
                font-family: 'Dancing Script', cursive;
            }
            
            .puzzle-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 5px;
                max-width: 306px;
                margin: 0 auto 25px;
                border: 3px solid #ff6b8b;
                border-radius: 10px;
                padding: 5px;
                background: white;
                min-height: 306px;
            }
            
            .puzzle-piece {
                width: 100px;
                height: 100px;
                background-size: 300px 200px;
                border-radius: 8px;
                cursor: move;
                transition: all 0.3s ease;
                box-shadow: 0 3px 10px rgba(0,0,0,0.2);
                border: 1px solid #ddd;
                position: relative;
            }
            
            .puzzle-piece.dragging {
                opacity: 0.7;
                transform: scale(1.05);
                z-index: 1000;
            }
            
            .puzzle-slot {
                width: 100px;
                height: 100px;
                border: 2px dashed #ff6b8b;
                border-radius: 8px;
                background: rgba(255, 107, 139, 0.1);
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .puzzle-completed {
                border-color: #4CAF50;
                background: rgba(76, 175, 80, 0.1);
            }
            
            .quote {
                background: rgba(255, 107, 139, 0.1);
                padding: 20px;
                border-radius: 15px;
                margin: 20px 0;
                font-style: italic;
                color: #666;
                line-height: 1.6;
                border-left: 4px solid #ff6b8b;
            }
            
            .quote-text {
                font-size: 1.2em;
                margin-bottom: 10px;
                font-family: 'Dancing Script', cursive;
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
                transition: all 0.3s ease;
            }
            
            .romantic-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
            
            .instructions {
                color: #666;
                margin: 20px 0;
                font-style: italic;
            }
            
            .puzzle-controls {
                margin: 20px 0;
            }
            
            .reset-btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 5px;
            }
            
            .success-message {
                background: rgba(76, 175, 80, 0.2);
                color: #4CAF50;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                border: 1px solid #4CAF50;
            }
            
            .puzzle-piece[data-piece="1"] { background-position: 0 0; }
            .puzzle-piece[data-piece="2"] { background-position: -100px 0; }
            .puzzle-piece[data-piece="3"] { background-position: -200px 0; }
            .puzzle-piece[data-piece="4"] { background-position: 0 -100px; }
            .puzzle-piece[data-piece="5"] { background-position: -100px -100px; }
            .puzzle-piece[data-piece="6"] { background-position: -200px -100px; }
            
            .hidden {
                display: none;
            }
            
            .completed-image {
                width: 300px;
                height: 200px;
                border-radius: 15px;
                border: 3px solid #4CAF50;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                margin: 20px auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧩 Пазлы нашей любви</h1>
            
            <p style="font-size: 1.2em; color: #666; margin-bottom: 30px;">
                Перетаскивай кусочки пазла на правильные места, чтобы собрать нашу фотографию!
            </p>
            
            <!-- Первый пазл -->
            <div class="puzzle-section">
                <div class="puzzle-title">Пазл №1: Наше утро</div>
                
                <div class="instructions">
                    Перетащи кусочки пазла на серые области, чтобы собрать фотографию
                </div>
                
                <div class="puzzle-controls">
                    <button class="reset-btn" onclick="resetPuzzle(1)">🔄 Перемешать пазл 1</button>
                </div>
                
                <!-- Собранное изображение (изначально скрыто) -->
                <img src="/static/photos/puzzle1.jpg" alt="Наше утро" class="completed-image hidden" id="completedImage1">
                
                <!-- Контейнер для сборки пазла -->
                <div class="puzzle-container" id="puzzleContainer1">
                    <div class="puzzle-slot" data-slot="1" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="2" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="3" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="4" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="5" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="6" ondrop="drop(event, 1)" ondragover="allowDrop(event)"></div>
                </div>
                
                <!-- Контейнер с кусочками пазла -->
                <div class="puzzle-container" id="piecesContainer1" style="border: none; background: transparent; margin-top: 20px;">
                    <div class="puzzle-piece" data-piece="1" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                    <div class="puzzle-piece" data-piece="2" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                    <div class="puzzle-piece" data-piece="3" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                    <div class="puzzle-piece" data-piece="4" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                    <div class="puzzle-piece" data-piece="5" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                    <div class="puzzle-piece" data-piece="6" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle1.jpg');"></div>
                </div>
                
                <!-- Цитата для первого пазла -->
                <div class="quote" id="quote1">
                    <div class="quote-text">💝 «Любовь это… понимать, что утро не было бы таким прекрасным без него»</div>
                    <div style="color: #ff6b8b; font-weight: bold;">- Наше утро вместе</div>
                </div>
            </div>
            
            <!-- Второй пазл -->
            <div class="puzzle-section">
                <div class="puzzle-title">Пазл №2: Наша встреча</div>
                
                <div class="instructions">
                    Перетащи кусочки пазла на серые области, чтобы собрать фотографию
                </div>
                
                <div class="puzzle-controls">
                    <button class="reset-btn" onclick="resetPuzzle(2)">🔄 Перемешать пазл 2</button>
                </div>
                
                <!-- Собранное изображение (изначально скрыто) -->
                <img src="/static/photos/puzzle2.jpg" alt="Наша встреча" class="completed-image hidden" id="completedImage2">
                
                <!-- Контейнер для сборки пазла -->
                <div class="puzzle-container" id="puzzleContainer2">
                    <div class="puzzle-slot" data-slot="1" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="2" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="3" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="4" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="5" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                    <div class="puzzle-slot" data-slot="6" ondrop="drop(event, 2)" ondragover="allowDrop(event)"></div>
                </div>
                
                <!-- Контейнер с кусочками пазла -->
                <div class="puzzle-container" id="piecesContainer2" style="border: none; background: transparent; margin-top: 20px;">
                    <div class="puzzle-piece" data-piece="1" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                    <div class="puzzle-piece" data-piece="2" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                    <div class="puzzle-piece" data-piece="3" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                    <div class="puzzle-piece" data-piece="4" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                    <div class="puzzle-piece" data-piece="5" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                    <div class="puzzle-piece" data-piece="6" draggable="true" ondragstart="drag(event)" style="background-image: url('/static/photos/puzzle2.jpg');"></div>
                </div>
                
                <!-- Цитата для второго пазла -->
                <div class="quote" id="quote2">
                    <div class="quote-text">💖 «Любовь это когда жизнь становится богаче от знакомства с тобой»</div>
                    <div style="color: #ff6b8b; font-weight: bold;">- С момента нашей встречи</div>
                </div>
            </div>
            
            <div>
                <button class="romantic-btn" onclick="location.href='/love-story'">
                    ← Назад к истории
                </button>
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>

        <script>
            let completedPuzzles = new Set();
            
            function allowDrop(ev) {
                ev.preventDefault();
            }
            
            function drag(ev) {
                ev.dataTransfer.setData("text", ev.target.getAttribute("data-piece"));
                ev.target.classList.add("dragging");
            }
            
            function drop(ev, puzzleNumber) {
                ev.preventDefault();
                const pieceId = ev.dataTransfer.getData("text");
                const piece = document.querySelector(`#piecesContainer${puzzleNumber} [data-piece="${pieceId}"]`) || 
                              document.querySelector(`[data-piece="${pieceId}"]`);
                const slot = ev.target;
                
                if (slot.classList.contains("puzzle-slot")) {
                    const slotNumber = slot.getAttribute("data-slot");
                    const isCorrect = pieceId === slotNumber;
                    
                    if (isCorrect) {
                        // Очищаем слот перед добавлением нового элемента
                        while (slot.firstChild) {
                            slot.removeChild(slot.firstChild);
                        }
                        
                        // Создаем копию элемента для слота
                        const pieceCopy = piece.cloneNode(true);
                        pieceCopy.style.backgroundPosition = piece.style.backgroundPosition;
                        pieceCopy.style.backgroundImage = piece.style.backgroundImage;
                        pieceCopy.style.width = '100px';
                        pieceCopy.style.height = '100px';
                        pieceCopy.style.margin = '0';
                        pieceCopy.style.position = 'static';
                        pieceCopy.draggable = false;
                        pieceCopy.classList.remove('dragging');
                        
                        slot.appendChild(pieceCopy);
                        slot.classList.add("puzzle-completed");
                        
                        // Скрываем оригинальный элемент
                        piece.style.display = 'none';
                        
                        // Проверяем, собран ли весь пазл
                        checkPuzzleCompletion(puzzleNumber);
                    } else {
                        piece.classList.remove("dragging");
                        showTemporaryMessage("Попробуй другое место! 💕", false);
                    }
                }
            }
            
            function checkPuzzleCompletion(puzzleNumber) {
                const container = document.getElementById(`puzzleContainer${puzzleNumber}`);
                const slots = container.querySelectorAll(".puzzle-slot");
                
                let allCorrect = true;
                slots.forEach(slot => {
                    if (slot.children.length === 0 || !slot.classList.contains("puzzle-completed")) {
                        allCorrect = false;
                    }
                });
                
                if (allCorrect && !completedPuzzles.has(puzzleNumber)) {
                    completedPuzzles.add(puzzleNumber);
                    showTemporaryMessage("🎉 Поздравляю! Пазл собран! 💖", true);
                    
                    // Показываем собранное изображение
                    const completedImage = document.getElementById(`completedImage${puzzleNumber}`);
                    completedImage.classList.remove("hidden");
                    
                    // Скрываем контейнеры с пазлами
                    container.style.display = 'none';
                    document.getElementById(`piecesContainer${puzzleNumber}`).style.display = 'none';
                    
                    // Показываем цитату
                    const quote = document.getElementById(`quote${puzzleNumber}`);
                    quote.style.display = 'block';
                    
                    // Обновляем инструкции
                    const instructions = document.querySelector(`#puzzleContainer${puzzleNumber}`).closest('.puzzle-section').querySelector('.instructions');
                    instructions.textContent = "🎊 Пазл собран! Вот наша прекрасная фотография и особенные слова!";
                }
            }
            
            function resetPuzzle(puzzleNumber) {
                const piecesContainer = document.getElementById(`piecesContainer${puzzleNumber}`);
                const puzzleContainer = document.getElementById(`puzzleContainer${puzzleNumber}`);
                const quote = document.getElementById(`quote${puzzleNumber}`);
                const completedImage = document.getElementById(`completedImage${puzzleNumber}`);
                const instructions = puzzleContainer.closest('.puzzle-section').querySelector('.instructions');
                
                // Показываем контейнеры с пазлами
                puzzleContainer.style.display = 'grid';
                piecesContainer.style.display = 'grid';
                
                // Скрываем собранное изображение
                completedImage.classList.add("hidden");
                
                // Сбрасываем стили слотов
                const slots = puzzleContainer.querySelectorAll(".puzzle-slot");
                slots.forEach(slot => {
                    slot.classList.remove("puzzle-completed");
                    while (slot.firstChild) {
                        slot.removeChild(slot.firstChild);
                    }
                });
                
                // Показываем все кусочки
                const pieces = piecesContainer.querySelectorAll(".puzzle-piece");
                pieces.forEach(piece => {
                    piece.style.display = 'flex';
                });
                
                // Скрываем цитату
                quote.style.display = 'none';
                
                // Восстанавливаем инструкции
                instructions.textContent = "Перетащи кусочки пазла на серые области, чтобы собрать фотографию";
                
                // Убираем из завершенных
                completedPuzzles.delete(puzzleNumber);
                
                showTemporaryMessage("Пазл перемешан! Собери его снова! 🧩", true);
            }
            
            function showTemporaryMessage(message, isSuccess) {
                const tempMsg = document.createElement("div");
                tempMsg.textContent = message;
                tempMsg.style.cssText = `
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: ${isSuccess ? 'rgba(76, 175, 80, 0.9)' : 'rgba(255, 107, 139, 0.9)'};
                    color: white;
                    padding: 20px 30px;
                    border-radius: 15px;
                    font-weight: bold;
                    z-index: 10000;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                    animation: fadeInOut 2s ease;
                `;
                
                document.body.appendChild(tempMsg);
                
                setTimeout(() => {
                    if (tempMsg.parentNode) {
                        document.body.removeChild(tempMsg);
                    }
                }, 2000);
            }
            
            // Инициализация при загрузке
            document.addEventListener("DOMContentLoaded", function() {
                // Скрываем все цитаты изначально
                document.getElementById('quote1').style.display = 'none';
                document.getElementById('quote2').style.display = 'none';
            });
            
            // Добавляем стили для анимации
            const style = document.createElement('style');
            style.textContent = `
                @keyframes fadeInOut {
                    0% { opacity: 0; transform: translate(-50%, -40%); }
                    20% { opacity: 1; transform: translate(-50%, -50%); }
                    80% { opacity: 1; transform: translate(-50%, -50%); }
                    100% { opacity: 0; transform: translate(-50%, -60%); }
                }
            `;
            document.head.appendChild(style);
        </script>
    </body>
    </html>
    '''

@app.route('/letter')
def letter():
    if not session.get('allowed'):
        return redirect('/secret')
    
    return '''
    <html>
    <head>
        <title>Письмо любви - Медианомер</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
                font-family: 'Playfair Display', serif;
                min-height: 100vh;
                padding: 40px 20px;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .love-letter {
                background: rgba(255, 255, 255, 0.95);
                max-width: 800px;
                padding: 60px 50px;
                border-radius: 25px;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
                border: 3px solid #ff6b8b;
                position: relative;
                overflow: hidden;
            }
            
            .love-letter::before {
                content: "💌";
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 80px;
                opacity: 0.1;
                transform: rotate(15deg);
            }
            
            .letter-header {
                text-align: center;
                margin-bottom: 40px;
                border-bottom: 2px solid #ff6b8b;
                padding-bottom: 20px;
            }
            
            .letter-title {
                font-family: 'Dancing Script', cursive;
                font-size: 3.5em;
                color: #ff6b8b;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }
            
            .letter-date {
                font-size: 1.3em;
                color: #666;
                font-style: italic;
            }
            
            .letter-content {
                font-size: 1.2em;
                line-height: 1.8;
                color: #444;
                text-align: justify;
                margin-bottom: 30px;
            }
            
            .letter-paragraph {
                margin-bottom: 25px;
                text-indent: 2em;
            }
            
            .highlight {
                color: #ff6b8b;
                font-weight: bold;
                font-style: italic;
            }
            
            .signature {
                text-align: right;
                margin-top: 40px;
                font-family: 'Dancing Script', cursive;
                font-size: 2em;
                color: #ff6b8b;
            }
            
            .hearts-decoration {
                text-align: center;
                margin: 30px 0;
                font-size: 30px;
                animation: float 3s ease-in-out infinite;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            .romantic-btn {
                background: linear-gradient(135deg, #ff6b8b 0%, #ff8e53 100%);
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 50px;
                cursor: pointer;
                font-family: 'Playfair Display', serif;
                margin: 10px;
                box-shadow: 0 10px 20px rgba(255, 107, 139, 0.3);
                transition: all 0.3s ease;
            }
            
            .romantic-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(255, 107, 139, 0.4);
            }
            
            .buttons {
                text-align: center;
                margin-top: 40px;
            }
            
            .memory-counter {
                text-align: center;
                background: rgba(255, 107, 139, 0.1);
                padding: 15px;
                border-radius: 15px;
                margin: 20px 0;
                color: #666;
                font-style: italic;
            }
        </style>
    </head>
    <body>
        <div class="love-letter">
            <div class="letter-header">
                <div class="letter-title">Моему самому любимому</div>
                <div class="letter-date">2 года нашей любви • 02.10.2023 - 02.10.2025</div>
            </div>
            
            <div class="hearts-decoration">
                💖 🥰 💕 🤗 ✨
            </div>
            
            <div class="letter-content">
                <p class="letter-paragraph">
                    Мой дорогой, любимый! Сегодня исполняется <span class="highlight">2 года</span> 
                    с того дня, когда началась наша сказка. За эти <span class="highlight">731 день</span> 
                    ты подарил мне столько счастья, что его хватило бы на целую вечность.
                </p>
                
                <p class="letter-paragraph">
                    Помнишь наши первые встречи? Тот смешной поход в кино втроем и зимнюю прогулку, 
                    когда ты кинул меня в сугроб? Эти моменты навсегда в моем сердце.
                </p>
                
                <p class="letter-paragraph">
                    Ты научил меня ценить простые радости. <span class="highlight">С тобой даже обычные дни становятся волшебными.</span> 
                    Ты превращаешь серые будни в яркие приключения.
                </p>
                
                <p class="letter-paragraph">
                    Спасибо тебе за каждую улыбку, за каждое "люблю", за терпение и веру в меня. 
                    Ты - мой лучший друг, партнер и самая большая любовь.
                </p>
                
                <p class="letter-paragraph">
                    Я обещаю всегда быть рядом и делать все, чтобы ты чувствовал себя самым любимым 
                    и счастливым. Мы пройдем через все вместе, рука об руку!
                </p>
            </div>
            
            <div class="memory-counter">
                💝 731 день вместе • 17,544 часа счастья • 1,052,640 минут любви 💝
            </div>
            
            <div class="hearts-decoration">
                🌟 💖 💫 🥰 🌸
            </div>
            
            <div class="signature">
                Твоя навсегда 💖
            </div>
            
            <div class="buttons">
                <button class="romantic-btn" onclick="location.href='/love-story'">
                    ← Назад к истории
                </button>
                <button class="romantic-btn" onclick="location.href='/'">
                    🏠 На главную
                </button>
            </div>
        </div>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(debug=True, port=5000)