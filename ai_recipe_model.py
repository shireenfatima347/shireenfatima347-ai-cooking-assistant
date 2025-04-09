def get_recipes_by_diet(user_input):
    input = user_input.lower()

    # Simple AI-like logic using keyword matching
    if "vegan" in input:
        return [
            
            "🌱 Vegan Buddha Bowl: quinoa, chickpeas, avocado, spinach, tahini dressing",
            "🥗 Green Smoothie Bowl: kale, banana, almond milk, chia seeds"
        ]
    elif "keto" in input:
        return [
            "🍳 Keto Egg Muffins: eggs, spinach, cheese, bacon",
            "🥩 Grilled Chicken & Avocado Salad: lettuce, avocado, olive oil"
        ]
    elif "gluten free" in input:
        return [
            "🍠 Sweet Potato Hash: sweet potato, bell peppers, eggs",
            "🥘 Chickpea Stew: chickpeas, tomato, spices, herbs"
        ]
    elif "high protein" in input:
        return [
            "🥗 Grilled Tofu Power Bowl: tofu, brown rice, edamame, broccoli",
            "🐟 Baked Salmon with Asparagus: salmon, garlic, lemon, asparagus"
        ]
    else:
        return [
            "👩‍🍳 Oops! I couldn't find recipes for that dietary type. Try: vegan, keto, gluten-free, or high protein."
        ]
