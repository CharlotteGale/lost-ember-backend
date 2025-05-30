from flask import jsonify, Blueprint
from app.lore.loader import load_lineages

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/api/lineages/<origin>', methods=['GET'])
def get_lineages_by_origin(origin):
    all_lineages = load_lineages()
    origin = origin.capitalize()

    if origin not in all_lineages:
        return jsonify({"error": f"No lineages found for '{origin}'."}), 404

    return jsonify({origin: all_lineages[origin]}), 200