# Lezione del 10/11/2025 Dictionary2

student = {"name":"Lorenzo", "age":"16"}
print(student["name"])
print(student["age"])
print(student.get("name"))
print(student.get("email","not found"))

len(student)
student.keys()
student.values()
student.items() # --> as a tuple

student.update({"grade":"A"})
print(student)
student.pop("grade")
student.clear()

