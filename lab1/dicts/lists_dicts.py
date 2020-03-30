my_list = [ {"title": "Information Systems", "id": "DS-512"},
            {"title": "C Programming", "id":"DS-501"},
            {"title": "Operating Systems", "id":"DS-209"}
]

for item in my_list:
    if item["id"]=="DS-512":
        print("There is a course with that ID.")
        print(item["title"])

