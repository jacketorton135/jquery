from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

dinners = [
    "牛肉麵", "壽司", "火鍋", "炸雞", "便當",
    "披薩", "拉麵", "漢堡", "燒烤", "咖哩飯"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-dinner')
def get_dinner():
    choice = random.choice(dinners)
    return jsonify({'dinner': choice})

if __name__ == '__main__':
    app.run(debug=True)
