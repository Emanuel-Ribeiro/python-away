import json
x =  [{ "nome":"Emanuel", "Idade":20, "cidade":"Brasilia"}]
y = json.loads(x)
print(y["Idade"])
y = json.dumps(x)
print(y)
json.dumps(y, indent=4)
json.dumps(y, indent=4, separators=(". ", " = "))
json.dumps(y, indent=4, sort_keys=True)