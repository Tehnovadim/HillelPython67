from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Trip

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    trips = [
        Trip(name='Экскурсия в Париж', destination='Франция, Париж', price=800.00, description='Незабываемая экскурсия в Париж с посещением Эйфелевой башни, Лувра и круиза по Сене.'),
        Trip(name='Тур по Италии', destination='Италия, Рим', price=1200.00, description='Путешествие по основным городам Италии: Рим, Флоренция, Венеция с гидом и трансферами.'),
        Trip(name='Путешествие в Барселону', destination='Испания, Барселона', price=900.00, description='Незабываемая поездка в Барселону с осмотром достопримечательностей, включая Собор Святого Семейства и Парк Гуэль.'),
        Trip(name='Путевка на Канарские острова', destination='Испания, Тенерифе', price=1300.00, description='Пляжный отдых на Канарских островах с экскурсиями по вулкану Тейде и Лоро Парку.'),
        Trip(name='Автобусный тур по Европе', destination='Германия, Франция, Италия', price=2000.00, description='Тур по основным городам Европы с посещением Берлина, Парижа и Рима за 10 дней.'),
        Trip(name='Тур в Исландию', destination='Исландия, Рейкьявик', price=1800.00, description='Путешествие по Исландии с посещением Голубой лагуны и ледниковых пещер.'),
        Trip(name='Экскурсионный тур в Лондон', destination='Великобритания, Лондон', price=900.00, description='Тур по Лондону с посещением Биг-Бена, Букингемского дворца и круизом по Темзе.'),
        Trip(name='Путешествие в Амстердам', destination='Нидерланды, Амстердам', price=850.00, description='Экскурсии по Амстердаму, посещение музеев и прогулка на лодке по каналам.'),
        Trip(name='Отдых в Хорватии', destination='Хорватия, Сплит', price=1000.00, description='Пляжный отдых в Хорватии с экскурсиями по историческим достопримечательностям.'),
        Trip(name='Гастрономический тур по Франции', destination='Франция, Лион', price=1600.00, description='Путешествие по винодельням и ресторанам Франции с дегустацией вин и сыра.'),
        Trip(name='Путешествие по Швейцарии', destination='Швейцария, Цюрих', price=1400.00, description='Путешествие по живописной Швейцарии с посещением озер и горнолыжных курортов.'),
        Trip(name='Путешествие в Вену', destination='Австрия, Вена', price=950.00, description='Тур по Вене с посещением дворца Шёнбрунн и Венской оперы.'),
        Trip(name='Отдых в Португалии', destination='Португалия, Лиссабон', price=1100.00, description='Отдых в Лиссабоне с экскурсиями по старому городу и поездкой в Синтру.'),
        Trip(name='Тур в Прагу', destination='Чехия, Прага', price=800.00, description='Незабываемый тур по Праге с посещением Карлова моста и Пражского Града.'),
        Trip(name='Экскурсия по Скандинавии', destination='Швеция, Норвегия, Дания', price=2200.00, description='Тур по Скандинавии с посещением Стокгольма, Осло и Копенгагена.')
    ]
    db.session.bulk_save_objects(trips)
    db.session.commit()

@app.route('/')
def index():
    search_query = request.args.get('search')
    if search_query:
        trips = Trip.query.filter(Trip.destination.contains(search_query)).all()
    else:
        trips = Trip.query.all()
    return render_template('index.html', trips=trips)

@app.route('/api/trips', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    return jsonify([trip.to_dict() for trip in trips])

@app.route('/add', methods=['GET', 'POST'])
def add_trip():
    if request.method == 'POST':
        name = request.form['name']
        destination = request.form['destination']
        price = request.form['price']
        description = request.form['description']
        trip = Trip(name=name, destination=destination, price=price, description=description)
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_trip(id):
    trip = Trip.query.get_or_404(id)
    if request.method == 'POST':
        trip.name = request.form['name']
        trip.destination = request.form['destination']
        trip.price = request.form['price']
        trip.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', trip=trip)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_trip(id):
    trip = Trip.query.get_or_404(id)
    db.session.delete(trip)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
