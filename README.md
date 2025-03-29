# product-recommendation-system

📌 Overview

This project builds a Product Recommendation System using Neo4j as a graph database. The system analyzes product relationships based on customer reviews and provides recommendations.
It integrates Python, Cypher Queries, and Neo4j AuraDB for efficient data storage and retrieval.

🚀 Features

✔ Graph-based recommendation system using Neo4j✔ Efficient Cypher queries for fetching recommendations✔ Python integration using Neo4j Python Driver✔ Data preprocessing & filtering to improve recommendations✔ Scalable & adaptable for real-world e-commerce applications


🛠 Technologies Used

1-Neo4j (Graph Database)

2-Cypher Query Language (CQL)

3-Python (Neo4j Python Driver, Pandas, Scikit-Learn,Flask)

4-Jupyter Notebooks (For data analysis and visualization)

Run Cypher Queries in Neo4j
Example:
1-Import Data

LOAD CSV WITH HEADERS FROM 'CSV_LINK' AS row
RETURN row LIMIT 5;

2-Create Nodes and Relationships

CREATE (:Product {product_id: 'P001', name: 'Laptop'});
CREATE (:Review {review_id: 'R001', content: 'Great product!'});
MATCH (p:Product), (r:Review)
WHERE p.product_id = 'P001'
CREATE (r)-[:REVIEWS]->(p);

3-Fetch Recommendations

MATCH (p:Product {product_id: $product_id})<-[:REVIEWS]-(:Review)-[:REVIEWS]->(other:Product)
RETURN other.product_id AS recommended_product, COUNT(*) AS score
ORDER BY score DESC LIMIT 5;

4-Run Python Scripts

📊 How It Works

1️⃣ Dataset Preparation: Kaggle dataset cleaned & filtered using Pandas.
2️⃣ Import Data into Neo4j: Nodes for Products, Categories, Reviews created.
3️⃣ Define Relationships: Products linked to reviews using Cypher queries.
4️⃣ Fetch Recommendations: Querying Neo4j using Python & Cypher.


📌 Visualization (Flask for web framework)

(In Neo4j Database)
To visualize the full graph structure, use:
MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 100;
