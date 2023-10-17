from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for 5 users
users = [
    {"society_name": "Religião", "user_name": "João Bispo", "percentage": 25, "bg_color": "bg-yellow-100"},
    {"society_name": "Hippie", "user_name": "Carolina Araujo", "percentage": 30, "bg_color": "bg-indigo-100"},
    {"society_name": "Ciência", "user_name": "David Antunes", "percentage": 35, "bg_color": "bg-green-100"},
    {"society_name": "Cinema", "user_name": "José Pereira", "percentage": 40, "bg_color": "bg-rose-100"},
    {"society_name": "Desporto", "user_name": "Raquel Figueira", "percentage": 45, "bg_color": "bg-blue-100"},
]

@app.route('/')
def index():
    user_id = request.args.get('user', default = 0, type = int)
    user = users[user_id]
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
