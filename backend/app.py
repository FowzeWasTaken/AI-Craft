from flask import Flask, request, jsonify
from flask_cors import CORS
from craft_db import get_crafting_recipes, get_suggested_builds

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "AI-Craft Backend Running!",
        "status": "ready"
    })

@app.route('/analyze', methods=['POST'])
def analyze_chest():
    """
    Receives chest contents and returns suggested builds/crafts
    Expected JSON: {"items": ["wood", "stone", "iron", ...]}
    """
    try:
        data = request.json
        items = data.get('items', [])
        
        if not items:
            return jsonify({"error": "No items provided"}), 400
        
        suggestions = get_suggested_builds(items)
        
        return jsonify({
            "items": items,
            "suggestions": suggestions,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Returns all available crafting recipes"""
    recipes = get_crafting_recipes()
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)