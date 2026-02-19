#  Expense Tracker API

A RESTful API built with Django REST Framework (DRF) to manage personal financial records. This project was developed to demonstrate backend fundamentals, object-relational mapping (ORM), and secure API endpoint design.

##  Tech Stack
* **Language:** Python
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite3

##  Core Concepts Applied
* **Data Serialization:** Used `ModelSerializer` to efficiently convert complex database QuerySets into JSON format.
* **Authentication & Security:** Implemented DRF's `IsAuthenticated` permission class to ensure data privacy (users can only access their own data).
* **Relational Database Design:** Managed Foreign Key relationships between `Users`, `Categories`, and `Expenses`.
* **HTTP Protocol:** Handled request-response cycles with appropriate HTTP status codes (200 OK, 201 Created, 400 Bad Request).

##  API Endpoints
* `GET /api/expenses/` - Retrieves a list of all expenses for the currently authenticated user.
* `POST /api/expenses/` - Creates a new expense securely tied to the user's account.
