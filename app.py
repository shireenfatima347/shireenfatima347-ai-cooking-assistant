from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple recipe logic
def get_recipes_by_diet(diet_input):
    diet_input = diet_input.lower()
    if "vegan" in diet_input:
        return [
            "🌱 Vegan Buddha Bowl: quinoa, chickpeas, avocado, spinach, tahini dressing",
            "🥗 Green Smoothie Bowl: kale, banana, almond milk, chia seeds"
        ]
    elif "keto" in diet_input:
        return [
            "🍳 Keto Egg Muffins: eggs, spinach, cheese, bacon",
            "🥩 Grilled Chicken & Avocado Salad"
        ]
    elif "gluten free" in diet_input:
        return [
            "🍠 Sweet Potato Hash with Eggs",
            "🥘 Chickpea Tomato Stew"
        ]
    elif "high protein" in diet_input:
        return [
            "🍗 Grilled Chicken with Quinoa",
            "🐟 Baked Salmon with Asparagus"
        ]
    else:
        return ["❌ No recipes found. Try 'vegan', 'keto', 'gluten free', or 'high protein'."]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()
    user_input = data.get("diet", "")
    recipes = get_recipes_by_diet(user_input)
    return jsonify({"recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)
