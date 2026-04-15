
import json

api_response = '{"model": "claude", "score": 0.95, "passed": true}'

data = json.loads(api_response)

print(data)

resultt = {"test": "hallucination", "score": 0.12}

json_string = json.dumps(resultt)
print(json_string)
print(type(json_string))