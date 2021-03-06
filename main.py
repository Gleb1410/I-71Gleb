from flask import render_template
import connexion

# Создадим экземпляр приложения
app = connexion.App(__name__, specification_dir='./')
# Прочитаем файл swagger.yml для настройки конечных точек
app.add_api('swagger.yml')


# Создадим маршрут URL в нашем приложении для "/"
@app.route('/')
def home():
    """
    Эта функция просто отвечает на URL "localhost:5000/" в браузера

    :return:        подствляет шаблон 'home.html'
    """
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5050, debug=True)