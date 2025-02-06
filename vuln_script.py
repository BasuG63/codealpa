import os
import ast
password = os.getenv("MY_SECRET_PASSWORD")
if not password:
    raise ValueError("MY_SECRET_PASSWORD environment variable is not set!")
user_input = input("Enter a number or list: ")
try:
    print(ast.literal_eval(user_input)) 
except (ValueError, SyntaxError):
    print("Invalid input! Please enter a valid number or list.")
file_name = input("Enter filename: ")
file_name = input("Enter filename: ").strip()

if not os.path.isfile(file_name):  
    print("Error: File not found.")
else:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read()) 
    except Exception as e:
        print(f"Error reading file: {e}")