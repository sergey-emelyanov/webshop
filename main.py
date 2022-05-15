from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import CreateForm

app = Flask(__name__)
app.secret_key = 'you_need_a_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	price = db.Column(db.Integer)
	isActive = db.Column(db.Boolean, default=True)

	def __repr__(self):
		return self.title


@app.route('/')
def index():
	goods = Items.query.order_by(Items.price).all()
	return render_template('index.html', goods=goods)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateForm()
	if request.method == 'POST':
		title = request.form['title']
		price = request.form['price']
		item = Items(title=title, price=price)
		try:
			db.session.add(item)
			db.session.commit()
			return redirect('/')
		except:
			'erorr'

		return render_template('create.html', form=form)
	else:
		return render_template('create.html', form=form)


@app.route('/buy/<int:number>')
def buy_good(number):
	item = Items.query.get(number)
	return render_template('buy.html', item=item)


if __name__ == '__main__':
	app.run(debug=True)
