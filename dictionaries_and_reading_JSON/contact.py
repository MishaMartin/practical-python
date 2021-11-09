contacts = {
    "number":4,
    "students":
    [
        {"name":"Sarah Holderness", "email":"sarah@ex.com"},
        {"name":"Harry Potter", "email":"harry@ex.com"},
        {"name":"Ron Weasley", "email":"ron@ex.com"},
        {"name":"Hermione Granger", "email":"hermione@ex.com"}
    ]    
}

for student in contacts["students"]:
    print(student["email"])