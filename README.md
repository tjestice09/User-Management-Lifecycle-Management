# User Access Lifecycle Manager

A simple Python project that simulates basic Identity and Access Management (IAM) processes for onboarding, transferring, and offboarding users—just like an IT or security team would do in a real company.

---

## 🚀 What This Project Does

- **Assigns permissions** to users based on their role when they join the company
- **Updates permissions** when users move to a new role or department
- **Revokes access** when users leave the company
- **Logs all access changes** in a structured JSON file for easy auditing and review

---

## 🧑‍💻 How It Works

- Users are defined in a Python list with their name, status (Joiner, Mover, Leaver), and role (Engineer, HR, Finance, etc.)
- The script automatically:
  - Assigns the right permissions for new hires (Joiners)
  - Changes permissions if an employee changes roles (Movers)
  - Removes all access for employees who leave (Leavers)
- Every action is **logged with a timestamp** in `access_log.json`

---

## 💼 Why I Built This

I’m learning core IAM concepts and practicing automation for real-world tech jobs.  
This project helps demonstrate my understanding of:
- **Role-Based Access Control (RBAC)**
- **User provisioning and deprovisioning**
- **Lifecycle management (Joiner, Mover, Leaver)**
- **Audit logging for compliance**

---

## 🏗️ Project Structure
user-access-lifecycle-manager/
├── main.py # Main script to process users
├── roles.py # Role and permission definitions
├── utils.py # Logging and timestamp functions
├── access_log.json # Log of all access changes (auto-generated)
└── README.md # This file!

## How To Use
1. Edit the 'users' list in 'main.py' to add or change users.
2. Run the script with: python3 main.py or just run the script using the "play" button in the IDE that you are using.
3. See output messages in your terminal.
4. Check the 'access_log.json file to review all changes and timestamps.

## Example Log Output
```json
[
  {
    "name": "Tommy",
    "status": "Joiner",
    "role": "Engineer",
    "permissions": [
      "access_repo",
      "deploy_code"
    ],
    "timestamp": "2025-07-16, 21:41:24"
  }
]

