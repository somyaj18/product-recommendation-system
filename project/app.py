from flask import Flask, render_template, request, jsonify
from neo4j import GraphDatabase

app = Flask(__name__)

# Connect to Neo4j
db = GraphDatabase.driver("neo4j+s://3205dd99.databases.neo4j.io", auth=("neo4j", "bc_JiFacp8CDN1_cjqPsGox9PNprgu18yGVkTpRyLPA"))

# 🔹 Fetch all products for the dropdown
def get_all_products():
    query = "MATCH (p:Product) RETURN p.product_id AS id, p.name AS name"
    with db.session() as session:
        result = session.run(query)
        return [{"id": record["id"], "name": record["name"]} for record in result]

# 🔹 Recommendation Query
def get_recommendations(product_id):
    query = """
    MATCH (p:Product {product_id: $product_id})<-[:REVIEWS]-(:Review)-[:REVIEWS]->(other:Product)
    RETURN other.product_id AS id, other.name AS name, other.category AS category, COUNT(*) AS score
    ORDER BY score DESC LIMIT 5
    """
    with db.session() as session:
        result = session.run(query, {"product_id": product_id})
        return [{"id": record["id"], "name": record["name"], "category": record["category"]} for record in result]

# 🔹 Render homepage with dropdown
@app.route("/")
def home():
    products = get_all_products()
    return render_template("product_recommendation.html", products=products)

# 🔹 Handle recommendation request
@app.route("/recommend", methods=["POST"])
def recommend():
    product_id = request.form.get("product_id")  # Get selected product's ID
    recommendations = get_recommendations(product_id)  # Get recommendations
    return jsonify(recommendations)  # Return JSON response

if __name__ == "__main__":
    app.run(debug=True)
