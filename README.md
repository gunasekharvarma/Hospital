# Hospital Management System

A Django-based web application designed to streamline hospital operations by effectively managing staff and patient information.

## Features

- Patient Registration and Management  
- Staff Details and Scheduling  
- Appointment Booking  
- Billing System  
- Medical Record Storage  

### Key Components

- **Django**: Provides the MVC architecture and built-in admin panel.  
- **Django Rest Framework (DRF)**: Enables the creation of RESTful APIs for data handling.  
- **Models**: Represent entities such as Patients and Staff in the database.  
- **Views**: Handle business logic and route incoming HTTP requests.  
- **Serializers**: Convert complex data types like querysets into native Python datatypes and vice versa.  
- **URLs**: Map views to endpoints.  
- **Admin Interface**: Used for managing records via the Django admin panel.
- 
## Tech Stack

1. Python  
2. Django  
3. Django Rest Framework (DRF)  
4. HTML  
5. CSS  
6. JavaScript  
7. Template Engine  
8. Jinja Syntaxing

### 🏠 Home Page
![Capture](https://github.com/user-attachments/assets/a443ec7f-18a6-43af-9ea9-b2b6455d9d56)


### 🔐 Login Page
![Capture1](https://github.com/user-attachments/assets/b1a31e0a-2584-40a9-8ab2-556a3437b8a0)


### 📊 Dashboard
![Capture2](https://github.com/user-attachments/assets/97f46589-1f1e-4864-b7b9-f83929aae5d4)


### 📋 Patient Details Page
![Capture5](https://github.com/user-attachments/assets/2dbe521c-d54b-492d-a9df-313fc12f7931)


### ➕ Add Patient Page
![Capture3](https://github.com/user-attachments/assets/bc29c3ca-90aa-434e-bd99-29510ac53458)


### 🔄 Update Patient Page
![Capture4](https://github.com/user-attachments/assets/0f2c724f-0c9b-4c88-a8ca-846eb474b917)



## Getting Started

### Prerequisites

- Python 3.x  
- pip  

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/gunasekharvarma/Hospital.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Hospital
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## Contributing

Contributions are welcome! Feel free to fork the project and submit a pull request.

