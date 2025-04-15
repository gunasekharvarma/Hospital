# Hospital Management System

This project is for effectively managing staff and patients in a hospital.

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

## License

This project is licensed under the MIT License.
