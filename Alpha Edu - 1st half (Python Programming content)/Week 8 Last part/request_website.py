import requests
import json

BASE_URL = "https://data.nasdaq.com/institutional-investors" # The adress of our flask

def get_all_students():
    requests_to_server = requests.get(url=f'{BASE_URL}/students')

    # Request status
    # 404, 500, 502, 400, 200, 300
    if requests_to_server.status_code == 200:
        results = requests_to_server.json() #The answer from serve we convert to json
        for each_result in results:
            print(
                f" ID: {each_result['ID']}, Name: {each_result['name']}"
            )
    return "All done good job"

get_all_students()

def get_exact_student(student_id: int):
    requests_to_server = requests.get(url=f'{BASE_URL}/students/{student_id}')
    if requests_to_server.status_code == 200:
        student_info = requests_to_server.json()
        print(
            f"ID: {student_info['id']}"
            f"Name: {student_info['name']}"
            f"Name: {student_info['age']}"
            f"Name: {student_info['grade']}"
        )

# Get requests are for reading

get_exact_student(8)

def create_new_student(name, age, grade):
    student_data = {
        "name": name,
        "age": age,
        "grade": grade
    }
    response = requests.post(f"{BASE_URL}/create-student", json=student_data)
    if response.status_code = 200:
        print(response.json()["message"])
    else:
        print("Failed to add student")

add_new_student("Darkhan", 21, 44)