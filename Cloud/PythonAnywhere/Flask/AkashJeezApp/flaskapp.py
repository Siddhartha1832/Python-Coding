# Import the Flask class from the flask module.
from flask import (Flask, render_template, url_for,
    redirect, flash, request, abort, session)
from flask_qrcode import QRcode
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import (LoginManager, login_user, current_user,
	logout_user, login_required, login_manager, UserMixin)
from PIL import Image
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
	TextAreaField, TextField, IntegerField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileField, FileAllowed
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta
from gsearch.googlesearch import search
from PyLyrics import *
from oxforddictionaries.words import OxfordDictionaries
# SecretKey -> protect form from mofifying cookies & cross site forgery attack.
import secrets, os, requests, json, pyttsx3, copy, fortune_cookie_phrases
import wikiquote, wikipedia, random, string, socket, hashlib, emoji
from forex_python.bitcoin import BtcConverter
from bs4 import BeautifulSoup as soup
from dateutil.parser import parse
from translate import Translator
from quiz import QuizFile

# create the app object
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
qrcode = QRcode(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
original_questions = QuizFile.original_questions
questions = copy.deepcopy(original_questions)
phrases = fortune_cookie_phrases.phrases


# forms.py

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min=7, max=20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired(), Length(min=7, max=20)])
	confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired(), Length(min=7, max=20)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min=7, max=20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

class PostForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()])
	content = TextAreaField('Content', validators = [DataRequired()])
	submit = SubmitField('Post')

class TextToSpeechConversionForm(FlaskForm):
	text = TextField('Enter Sample Text', validators = [DataRequired()])
	submit = SubmitField('Convert!')

class GoogleSearchForm(FlaskForm):
	keyword = TextField('Enter keyword', validators = [DataRequired()])
	submit = SubmitField('Search')

class YoutubeVideoForm(FlaskForm):
	link = TextField('Type YouTube Link', validators = [DataRequired()])
	submit = SubmitField('Play Video')

class SongLyricsForm(FlaskForm):
	artist_name = TextField('Artist Name', validators = [DataRequired()])
	song_name = TextField('Song Name', validators = [DataRequired()])
	submit = SubmitField('Get Song Lyrics')

class OxfordDictionarysForm(FlaskForm):
	word = TextField('Word', validators = [DataRequired()])
	submit = SubmitField('Get Meaning and Opposite!')

class AgeCalculatorsForm(FlaskForm):
	dob = TextField('Enter Date of Birth (dd/mm/yyyy)', validators = [DataRequired()])
	submit = SubmitField('Get Age!')

class GenerateQRCodeFrom(FlaskForm):
	text = TextField('Enter text', validators = [DataRequired()])
	submit = SubmitField('Generate QR Code')

class WeatherReportForm(FlaskForm):
	city = TextField('Enter City Name (Not Country)', validators = [DataRequired()])
	submit = SubmitField('Get Weather Data')

class FlamesGameForm(FlaskForm):
	your_name = TextField('Enter Your Name', validators = [DataRequired()])
	partner_name = TextField('Enter Your Partner Name', validators = [DataRequired()])
	submit = SubmitField('Play GAME!')

class LanguageTranslateForm(FlaskForm):
	word = TextField('Enter Word/Sentence', validators = [DataRequired()])
	submit = SubmitField('Translate!')

class RandomQuotesForm(FlaskForm):
	word = TextField('Enter KeyWord', validators = [DataRequired()])
	submit = SubmitField('Get Quotes!')

class WikipediaSearchForm(FlaskForm):
	word = TextField('Enter Keyword', validators = [DataRequired()])
	submit = SubmitField('Search')

class RechargeCodeGeneratorForm(FlaskForm):
	mobile_num = IntegerField('Enter Mobile Number (without +91)', validators = [DataRequired(), NumberRange(min=10)])
	submit = SubmitField('Generate Code')

class IPAddressSearchForm(FlaskForm):
    name = TextField('Enter IP Address / Domain', validators = [DataRequired()])
    submit = SubmitField('Search')

class IPAddressSearchForm(FlaskForm):
	name = TextField('Enter IP Address / Domain', validators = [DataRequired()])
	submit = SubmitField('Search')

class CryptographyForm(FlaskForm):
	name = TextField('Enter Sample Text', validators = [DataRequired()])
	submit = SubmitField('Encrypt Message!')

class PlayMusicForm(FlaskForm):
	audio_path = TextField('Type Audio URL from Internet', validators = [DataRequired()])
	submit = SubmitField('Load Music')

class LoveCalculatorForm(FlaskForm):
	boy_name = TextField('Enter Boy Name', validators = [DataRequired()])
	girl_name = TextField('Enter Girl Name', validators = [DataRequired()])
	submit = SubmitField('Calculate Love %')

class ZodiacSignForm(FlaskForm):
	dob = TextField('Enter Date of Birth (dd/mm/yyyy)', validators = [DataRequired()])
	submit = SubmitField('Get Astro Sign!!')


# models.py

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(70), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"


# routes.py

@app.route('/')
@app.route('/home')
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts = posts, fortune = random.choice(phrases),
		date = datetime.now().strftime('%d-%m-%Y'))

@app.route('/about')
def about():
    return render_template('about.html', title = 'AboutMe')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("Your account has been created! You are now able to log in.", 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash("Login Unsucessful. Please Check Email and Password..", 'danger')
	return render_template('login.html',title = 'Login', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn


@app.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
	return render_template('account.html', title = 'Account', image_file = image_file, form = form)

@app.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created!', 'success')
		return redirect(url_for('home'))
	return render_template('create_post.html', title = 'NewPost', form = form, legend = 'New Post')

@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title = post.title, post = post)

@app.route('/post/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Your post has been deleted!', 'success')
	return redirect(url_for('home'))

@app.route('/user/<string:username>')
def user_posts(username):
	page = request.args.get('page', 1, type=int)
	user = User.query.filter_by(username=username).first_or_404()
	posts = Post.query.filter_by(author=user)\
			.order_by(Post.date_posted.desc())\
			.paginate(page=page, per_page=5)
	return render_template('user_posts.html', posts = posts, user = user)

@app.route('/users')
def users():
	users = User.query.all()
	users_count = User.query.count()
	return render_template('users.html', title = 'Users', users = users, users_count = users_count)

@app.route('/applications')
def applications():
	return render_template('applications.html', title = 'Apps')

@app.route("/applications/currency_exchange", methods=['GET', 'POST'])
def currency_exchange():
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD").json()
    data = response['rates']
    return render_template('currency_exchange.html', data = data)

@app.route("/applications/cryptocurrency_exchanges", methods=['GET', 'POST'])
def cryptocurrency_exchanges():
	countries = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
	bitc = BtcConverter()
	raw_data = []
	for data in countries:
		raw_data.append([data, bitc.get_latest_price(data)])
	return render_template('cryptocurrency_exchanges.html', raw_data = raw_data)

@app.route("/applications/stock_ticker", methods=['GET', 'POST'])
def stock_ticker():
	company_codes = ['AAPL', 'MSFT', 'FB', 'AMZN', 'SBUX', 'GOOG', 'BABA', 'JNJ', 'JPM', 'XOM', 'BAC', 'WMT', 'WFC', 'INTC', 'VZ', 'ORCL', 'HON']
	start_date = (datetime.now() - timedelta(days=5)).strftime('%d-%m-%Y')
	raw_data = []
	for code in company_codes:
		df = web.DataReader(code, "yahoo", start_date, datetime.now())
		content = [code, df['High'].tail(5)[-1], df['Low'].tail(5)[-1], df['Open'].tail(5)[-1], df['Close'].tail(5)[-1], df['Volume'].tail(5)[-1], df['Adj Close'].tail(5)[-1]]
		raw_data.append(content)
	return render_template('stock_ticker.html', raw_data = raw_data)

@app.route('/applications/text_to_speech', methods = ['GET', 'POST'])
def text_to_speech():
	form = TextToSpeechConversionForm()
	if request.method == 'POST':
		engine = pyttsx3.init()
		engine.say(form.text.data)
		engine.runAndWait()
		return render_template('text_to_speech.html', form = form)
	return render_template('text_to_speech.html', form = form)

@app.route('/applications/google_search', methods = ['GET', 'POST'])
def google_search():
    form = GoogleSearchForm()
    raw_data = []
    if request.method == 'POST':
        keyword = form.keyword.data
        raw_data = [url for url in search(keyword.casefold(), num_results=10)]
        return render_template('google_search.html', form = form, raw_data = raw_data)
    return render_template('google_search.html', form = form)

@app.route('/applications/youtube_video', methods = ['GET', 'POST'])
def youtube_video():
	form = YoutubeVideoForm()
	if request.method == 'POST':
		temp_link = form.link.data
		raw_link = "https://www.youtube.com/embed/{}".format(temp_link.split('/')[3])
		return render_template('youtube_video.html', form = form, raw_link = raw_link)
	return render_template('youtube_video.html', form = form)

@app.route('/applications/song_lyrics', methods = ['GET', 'POST'])
def song_lyrics():
	form = SongLyricsForm()
	if request.method == 'POST':
		artist_name = form.artist_name.data
		song_name = form.song_name.data
		raw_data = PyLyrics.getLyrics(artist_name.casefold(), song_name.casefold())
		raw_data = raw_data.split('\n')
		return render_template('song_lyrics.html', form = form, raw_data = raw_data)
	return render_template('song_lyrics.html', form = form)

@app.route('/applications/oxford_dictionary', methods = ['GET', 'POST'])
def oxford_dictionary():
	form = OxfordDictionarysForm()
	if request.method == 'POST':
		word = form.word.data
		app_id = '86bad9b7'
		app_key = 'b36d710e0a1ea7cbf4080c46e66fa8db'
		od = OxfordDictionaries(app_id, app_key)
		synonyms_data = od.get_synonyms(word.casefold()).json()
		synonyms = synonyms_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
		synonyms = [res['text'] for res in synonyms]
		antonyms_data = od.get_antonyms(word.casefold()).json()
		antonyms = antonyms_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms']
		antonyms = [res['text'] for res in antonyms]
		return render_template('oxford_dictionary.html', form = form, synonyms = synonyms, antonyms = antonyms)
	return render_template('oxford_dictionary.html', form = form)

@app.route('/applications/age_calculator', methods = ['GET', 'POST'])
def age_calculator():
	form = AgeCalculatorsForm()
	if request.method == 'POST':
		dob = form.dob.data
		b_date = datetime.strptime(dob, '%d/%m/%Y')
		age_calc = ((datetime.today() - b_date).days/365)
		return render_template('age_calculator.html', form = form, age_calc = age_calc)
	return render_template('age_calculator.html', form = form)

@app.route('/applications/get_news', methods = ['GET', 'POST'])
def get_news():
	resp = soup(requests.get("https://news.google.com/news/rss").text, "xml")
	raw_data = []
	for news in resp.findAll("item"):
		pubdate = parse(news.pubDate.text)
		content = [news.title.text, news.link.text, pubdate.strftime('%d-%m-%Y %I:%M %p')]
		raw_data.append(content)
	return render_template('get_news.html', raw_data = raw_data)

@app.route('/applications/generate_qrcode', methods = ['GET', 'POST'])
def generate_qrcode():
	form = GenerateQRCodeFrom()
	if request.method == 'POST':
		text = form.text.data
		text = qrcode(text, box_size=12)
		return render_template('generate_qrcode.html', form = form, text = text)
	return render_template('generate_qrcode.html', form = form)

@app.route('/applications/weather_report', methods = ['GET', 'POST'])
def weather_report():
	form = WeatherReportForm()
	if request.method == 'POST':
		api_key = '28a31767a1909138a53410a56233a326'
		city = form.city.data
		raw_data = []
		resp = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
		data = json.loads(resp.text)
		raw_data.append(f" City - {(data['name']).upper()}")
		raw_data.append(f" Coordinates - Latitude {data['coord']['lat']} & Longitude {data['coord']['lon']}")
		raw_data.append(f" Description - {(data['weather'][0]['description']).upper()}")
		raw_data.append(f" Temperature - {data['main']['temp']} F")
		raw_data.append(f" Humidity - {data['main']['humidity']}")
		raw_data.append(f" Wind Speed - {data['wind']['speed']}")
		icon = data['weather'][0]['icon']
		return render_template('weather_report.html', form = form, raw_data = raw_data, icon = icon)
	return render_template('weather_report.html', form = form)

@app.route('/applications/flames_game', methods = ['GET', 'POST'])
def flames_game():
	form = FlamesGameForm()
	if request.method == 'POST':
		your_name = form.your_name.data
		partner_name = form.partner_name.data
		data = ''

		def flames_count(male_name, female_name):
			male_name_list = list(male_name)
			female_name_list = list(female_name)
			for letter in male_name_list[:]:
				if female_name_list.count(letter) > 0:
					female_name_list.remove(letter)
					male_name_list.remove(letter)
			return len(female_name_list) + len(male_name_list)

		def flames_result(count):
			flames_list = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
			while len(flames_list) > 1:
				remove_count = count
				if count > len(flames_list):
					remove_count = count % len(flames_list)
					if remove_count == 0:
						remove_count = len(flames_list)
				flames_list.remove(flames_list[remove_count - 1])
				flames_list = flames_list[remove_count - 1:] + flames_list[:remove_count - 1]
			return flames_list[0]

		def calculate(your_name, partner_name):
			first_name = your_name.lower().replace(' ', '')
			second_name = partner_name.lower().replace(' ', '')
			count = flames_count(first_name, second_name)
			result = flames_result(count)
			return result

		data = calculate(your_name, partner_name)
		return render_template('flames_game.html', form = form, data = data)
	return render_template('flames_game.html', form = form)

@app.route('/applications/language_translate', methods = ['GET', 'POST'])
def language_translate():
	form = LanguageTranslateForm()
	languages = ['Arabic', 'Bengali', 'Bulgarian', 'Chinese', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hawaiian', 'Hindi', 'Indonesian', 'Italian', 'Japanese', 'Kannada', 'Korean', 'Malay', 'Malayalam', 'Persian', 'Portuguese',  'Serbian', 'Slovak', 'Somali', 'Spanish', 'Swedish', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Vietnamese']
	if request.method == 'POST':
		word = form.word.data
		raw_data = []
		for language in languages:
			translator = Translator(from_lang = "english" ,to_lang = language)
			content = [language, translator.translate(word)]
			raw_data.append(content)
		return render_template('language_translate.html', form = form, raw_data = raw_data)
	return render_template('language_translate.html', form = form)

@app.route('/applications/random_quotes', methods = ['GET', 'POST'])
def random_quotes():
	form = RandomQuotesForm()
	if request.method == 'POST':
		word = form.word.data
		raw_data = []
		quotes = wikiquote.quotes(word.casefold())
		for quote in quotes:
			raw_data.append(quote)
		return render_template('random_quotes.html', form = form, raw_data = raw_data)
	return render_template('random_quotes.html', form = form)

@app.route('/applications/wikipedia_search', methods = ['GET', 'POST'])
def wikipedia_search():
	form = WikipediaSearchForm()
	if request.method == 'POST':
		word = form.word.data
		raw_data = []
		contents = wikipedia.summary(word.casefold()).splitlines()
		return render_template('wikipedia_search.html', form = form, contents = contents)
	return render_template('wikipedia_search.html', form = form)

@app.route('/applications/recharge_code_generator', methods = ['GET', 'POST'])
def recharge_code_generator():
	form = RechargeCodeGeneratorForm()
	mobile_networks = ['Airtel', 'Jio', 'BSNL', 'Aircel', 'Reliance', 'Idea', 'Vodafone', 'Tata Docomo']
	states = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
	if request.method == 'POST':
		mobile_num = form.mobile_num.data
		data = "".join(random.choice(string.digits) for _ in range(16))
		return render_template('recharge_code_generator.html', form = form, data = data, mobile_networks = mobile_networks, states = states)
	return render_template('recharge_code_generator.html', form = form)

@app.route('/applications/ip_address_search', methods = ['GET', 'POST'])
def ip_address_search():
	form = IPAddressSearchForm()
	if request.method == 'POST':
		name = form.name.data
		raw_data = []
		raw_data.append(f" Input : {name}")
		raw_data.append(f" IP Address: {socket.gethostbyname(name)}")
		raw_data.append(f" Fully Qualified Domain Name: {socket.gethostbyaddr(name)}")
		return render_template('ip_address_search.html', form = form, raw_data = raw_data)
	return render_template('ip_address_search.html', form = form)

def shuffle(q):
	selected_keys = []
	i = 0
	while i < len(q):
		keys = list(q.keys())
		current_selection = random.choice(keys)
		if current_selection not in selected_keys:
			selected_keys.append(current_selection)
			i = i+1
	return selected_keys

@app.route('/applications/quiz_game')
def quiz_game():
	questions_shuffled = shuffle(questions)
	for i in questions.keys():
		random.shuffle(questions[i])
	return render_template('quiz_game.html', questions_shuffled = questions_shuffled, questions = questions)

@app.route('/applications/quiz', methods=['POST'])
def quiz_answers():
	correct = 0
	for i in questions.keys():
		print(original_questions[i][0])
		answered = request.form[i]
		if original_questions[i][0] == answered:
			correct = correct + 1
	correct = f"You have got {correct} Correct Answers out of {len(original_questions)} Questions!"
	return render_template('quiz_results.html', correct = correct)

@app.route('/applications/cryptography_security', methods = ['GET', 'POST'])
def cryptography_security():
	form = CryptographyForm()
	if request.method == 'POST':
		name = form.name.data
		raw_data = []
		raw_data.append(f" Encrypted using MD5 : {hashlib.md5(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA 1 : {hashlib.sha1(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA 224 : {hashlib.sha224(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA 256 : {hashlib.sha256(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA 384 : {hashlib.sha384(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA3 224 : {hashlib.sha3_224(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA3 256 : {hashlib.sha3_256(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using SHA3 384 : {hashlib.sha3_384(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using Blake 2B : {hashlib.blake2b(name.encode()).hexdigest()}")
		raw_data.append(f" Encrypted using Blake 2S : {hashlib.blake2s(name.encode()).hexdigest()}")
		return render_template('cryptography_security.html', form = form, raw_data = raw_data)
	return render_template('cryptography_security.html', form = form)


@app.route('/applications/ninga_gold_game')
def ninga_gold_game():
    return render_template('ninga_gold_game.html')


@app.route('/applications/process_money', methods=['POST'])
def process_money():
	try:
		session['gold']
	except KeyError:
		session['gold'] = 0

	try:
		session['activities']
	except KeyError:
		session['activities'] = []

	if request.form['building'] == 'farm':
		gold = random.randrange(10,21)
	elif request.form['building'] == 'cave':
		gold = random.randrange(5,11)
	elif request.form['building'] == 'house':
		gold = random.randrange(2,6)
	elif request.form['building'] == 'casino':
		gold = random.randrange(-50,51)

	activity = ''
	time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
	if gold >= 0:
		activity += 'Earned ' + str(gold) + ' golds from the ' + str(request.form['building'])
	else:
		activity += 'Entered a casino and lost ' + str(gold) + ' golds... Ouch...'

	activity += '! (' + str(time) + ')'
	session['gold'] += gold
	session['activities'].insert(0, activity)
	return redirect(url_for('ninga_gold_game'))

@app.route('/applications/reset')
def reset():
	session.pop('gold')
	session.pop('activities')
	return redirect(url_for('ninga_gold_game'))

@app.route('/applications/play_music', methods = ['GET', 'POST'])
def play_music():
	form = PlayMusicForm()
	if request.method == 'POST':
		audio_url = form.audio_path.data
		return render_template('play_music.html', title = 'Music', form = form, audio_url = audio_url)
	return render_template('play_music.html', form = form)

@app.route("/applications/common_passwords", methods=['GET', 'POST'])
def common_passwords():
	df = pd.read_html('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
	data = df[0][1:]
	raw_data = data.values.tolist()
	return render_template('common_passwords.html', raw_data = raw_data)

@app.route("/applications/todo_list")
def todo_list():
	return render_template('todo_list.html', title = 'To-Do List')

@app.route("/applications/tictactoe_game")
def tictactoe_game():
	return render_template('tictactoe_game.html', title = 'Tic-Tac-Toe Game')

@app.route("/applications/towerofhanoi_game")
def towerofhanoi_game():
	return render_template('towerofhanoi_game.html', title = 'Tower-of-Hanoi Game')

@app.route("/applications/game_2048")
def game_2048():
	return render_template('game_2048.html', title = '2048 Game')

@app.route('/applications/love_calculator', methods = ['GET', 'POST'])
def love_calculator():
	form = LoveCalculatorForm()
	if request.method == 'POST':
		boy_name = form.boy_name.data
		girl_name = form.girl_name.data
		score = f" Their chance of finding true love together is {100-(len(boy_name)*len(girl_name))-(random.randint(1,20))} %"
		return render_template('love_calculator.html', form = form, score = score)
	return render_template('love_calculator.html', form = form)

@app.route("/applications/snake_game")
def snake_game():
	return render_template('snake_game.html', title = '2048 Game')

@app.route('/applications/zodiac_sign', methods = ['GET', 'POST'])
def zodiac_sign():
	form = ZodiacSignForm()
	if request.method == 'POST':
		dob = form.dob.data
		b_date = datetime.strptime(dob, '%d/%m/%Y')
		day, month, result = b_date.day, b_date.month, ""
		if int(month) == 1:
			result = 'Capricorn (மகரம் )' if (day < 20) else 'Aquarius (கும்பம் )'
		elif int(month) == 2:
			result = 'Aquarius (கும்பம் )' if (day < 19) else 'Pisces (மீனம் )'
		elif int(month) == 3:
			result = 'Pisces (மீனம் )' if (day < 21) else 'Aries (மேஷம்)'
		elif int(month) == 4:
			result = 'Aries (மேஷம்)' if (day < 20) else 'Taurus (ரிஷபம்)'
		elif int(month) == 5:
			result = 'Taurus (ரிஷபம்)' if (day < 21) else 'Gemini (மிதுனம் )'
		elif int(month) == 6:
			result = 'Gemini (மிதுனம் )' if (day < 21) else 'Cancer (கடகம் )'
		elif int(month) == 7:
			result = 'Cancer (கடகம் )' if (day < 23) else 'Leo (சிம்மம் )'
		elif int(month) == 8:
			result = 'Leo (சிம்மம் )' if (day < 23) else 'Virgo (கன்னி )'
		elif int(month) == 9:
			result = 'Virgo (கன்னி )' if (day < 23) else 'Libra (துலாம் )'
		elif int(month) == 10:
			result = 'Libra (துலாம் )' if (day < 23) else 'Scorpio (விருச்சிகம் )'
		elif int(month) == 11:
			result = 'scorpio (விருச்சிகம் )' if (day < 22) else 'Sagittarius (தனுசு )'
		elif int(month) == 12:
			result = 'Sagittarius (தனுசு )' if (day < 22) else 'Capricorn (மகரம் )'
		elif int(month)>12 or day>31:
			result = 'Invalid Date-of-Birth, Please try again!'
		return render_template('zodiac_sign.html', form = form, result = result)
	return render_template('zodiac_sign.html', form = form)

@app.route("/applications/emoji_symbols")
def emoji_symbols():
	raw_data = []
	raw_data.append(emoji.emojize(" Thumps Up -> :thumbs_up:"))
	raw_data.append(emoji.emojize(" Two hearts -> :two_hearts: "))
	raw_data.append(emoji.emojize(" Sparkles -> :sparkles: "))
	raw_data.append(emoji.emojize(" Musical Notes -> :musical_note: "))
	raw_data.append(emoji.emojize(" Family -> :family: "))
	raw_data.append(emoji.emojize(" Baby -> :baby: "))
	return render_template('emoji_symbols.html', title = 'Emojis', raw_data = raw_data)

@app.route("/applications/web_camera")
def web_camera():
	return render_template('web_camera.html', title = 'WebCam')

@app.route("/applications/rock_paper_scissor_game")
def rock_paper_scissor_game():
	return render_template('rock_paper_scissor_game.html')

@app.route("/applications/python_online_compiler")
def python_online_compiler():
	online_compiler_link = 'https://console.python.org/python-dot-org-console/'
	return render_template('python_online_compiler.html', raw_link = online_compiler_link)


# Start the server with the 'run()' method.
if __name__ == '__main__':
	app.run(debug = True)
