import json
import pandas as pd
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

result = json.loads(obj)
print("-----result-----")
print(result)

print("-----json.dumps()-----")
print(json.dumps(result))

print("JSON转DataFrame数据结构")
siblings = pd.DataFrame(result["siblings"], columns=["name", "age"])
print(siblings)

print("-----read_json()-----")
data = pd.read_json("examples/example.json")
print(data)

print("-----to_json-----")
print(data.to_json())
print(data.to_json(orient="records"))