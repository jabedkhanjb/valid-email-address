import re

email = input("Enter your email: ").strip()

if re.search(r"^\w.+@\w+\.(\w+\.)?(edu|com|bd|uk|it|net|org)$", email):
    print("Valid Email")
else:
    print("Invalid Email")