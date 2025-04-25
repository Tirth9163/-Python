import json

employee = {
    "empcode": input("Enter Employee Code: "),
    "empname": input("Enter Employee Name: "),
    "doj": input("Enter Date of Joining (DD-MM-YYYY): "),
    "salary": float(input("Enter Salary: "))
}

with open("employee.json", "w") as f:
    json.dump(employee, f)

print("Employee data serialized and saved to 'employee.json'.")

with open("employee.json", "r") as f:
    loaded_employee = json.load(f)

print("\nDeserialized Employee Data:")
print("Employee Code:", loaded_employee["empcode"])
print("Name:", loaded_employee["empname"])
print("Date of Joining:", loaded_employee["doj"])
print("Salary:", loaded_employee["salary"])
