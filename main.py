from roles import roles
from utils import get_timestamp, log_access_event

def handle_user_event(user):
    name = user["name"]
    status = user["status"]
    role = user.get("role", "")
    permissions = []

    if status == "Joiner":
        permissions = roles.get(role, [])
        print(f"{name} has been added to the {role} with permissions: {permissions}")

    elif status == "Mover":
        permissions = roles.get(role, [])
        print(f"{name} has moved to a new role {role} with permissions: {permissions}")
    
    elif status == "Leaver":
        print(f"{name} has left the company. All access revoked from their role.")
    
    else:
        print("Invalid status")
        return 
    
    event = {
        "name": name,
        "status": status,
        "role": role, 
        "permissions": permissions if status != "Leaver" else [],
        "timestamp": get_timestamp() 
        }
    log_access_event(event)

if __name__== "__main__":
    users = [
        {"name": "Tommy",
        "status": "Joiner",
        "role": "Engineer"}, 
        
        {"name": "Michelle",
         "status": "Mover",
         "role": "HR"},

        {"name": "Mike",
         "status": "Mover",
         "role": "Finance"},

        {"name": "Phil",
         "status": "Leaver",
         "role": "Engineer"},

    ]
    for user in users:
        print(user["name"])
        handle_user_event(user)




