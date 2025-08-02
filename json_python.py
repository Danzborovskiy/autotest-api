import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data) # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data['name']) # Выведет: Иван

data = {
    "name": "Анна",
    "age": 30,
    "is_student": True
}
json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)