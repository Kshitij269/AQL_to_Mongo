from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from aql_to_mongo import parse_aql
import traceback

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["ehr_db"]  # Your actual MongoDB database name

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    aql = ""

    if request.method == 'POST':
        try:
            aql = request.form.get('aql')
            if not aql:
                error = "Missing AQL query input."
            else:
                # Parse AQL to MongoDB structure
                parsed = parse_aql(aql)

                if not parsed or 'collection' not in parsed:
                    error = f"Parsing failed. Returned: {parsed}"
                else:
                    collection_name = parsed['collection']
                    collection = db[collection_name]

                    mongo_filter = parsed.get('filter', {})
                    projection = parsed.get('projection', {})
                    aliases = parsed.get('aliases', {})
                    sort_clause = parsed.get('sort', [])

                    # Run query with optional sort
                    cursor = collection.find(mongo_filter, projection)
                    if sort_clause:
                        cursor = cursor.sort(sort_clause)

                    results = []
                    for doc in cursor:
                        doc['_id'] = str(doc['_id'])
                        results.append(doc)

                    result = {
                        "results": results,
                        "aliases": aliases,
                        "mongo_query": {
                            "collection": collection_name,
                            "filter": mongo_filter,
                            "projection": projection,
                            "sort": sort_clause
                        }
                    }

        except Exception as e:
            error = f"Exception occurred:\n{traceback.format_exc()}"

    return render_template("index.html", result=result, error=error, aql=aql)

if __name__ == '__main__':
    app.run(debug=True)
