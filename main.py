from aql_to_mongo import parse_aql
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ehr_db"]

aql = """
SELECT c/content/items/parts[at0000]/parts[at0002]/value/magnitude AS Systolic
FROM EHR e CONTAINS Composition c
WHERE e/subjectOfCare/extension = 'ANON_SERV_RSC:5506084300';
"""

parsed = parse_aql(aql)
print("Parsed Mongo Query:", parsed)

collection = db[parsed['collection'].lower()]
docs = collection.find(parsed["filter"], parsed["projection"])

for doc in docs:
    result = {}
    for alias, field in parsed["aliases"].items():
        # Support nested field access
        parts = field.split('.')
        val = doc
        for part in parts:
            val = val.get(part, {})
        result[alias] = val
    print(result)
