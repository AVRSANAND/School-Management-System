# School Management System

This project is a School Management System implemented using Object-Oriented Programming principles and PyQt6 for the graphical user interface. The system allows for managing student records, including adding, editing, deleting, and searching for student information.

## Features

- **Add Student**: Add a new student record to the database.
- **Edit Student**: Edit existing student records.
- **Delete Student**: Delete student records from the database.
- **Search Student**: Search for students by name.
- **View Students**: Display all student records in a table.

## Requirements

To run this project, you'll need to install the following dependencies:

- PyQt6==6.7.1
- PyQt6-Qt6==6.7.2
- PyQt6_sip==13.8.0

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Files

- `main.py`: The main script that runs the application.
- `requirements.txt`: A list of required dependencies for the project.

## How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/AVRSANAND/School-Management-System.git
cd School-Management-System
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the application**:

```bash
python main.py
```

## Project Structure

- `main.py`: Contains the main application logic, including class definitions and the GUI setup.
- `requirements.txt`: Specifies the Python dependencies required to run the project.

## Classes and Methods

### MainWindow

The main window of the application, which includes the menu, toolbar, status bar, and a table to display student records.

- `__init__()`: Initializes the main window.
- `cell_clicked()`: Handles cell click events in the table.
- `load_Data()`: Loads student data from the database into the table.
- `insert()`: Opens the dialog to add a new student.
- `search()`: Opens the dialog to search for students.
- `edit()`: Opens the dialog to edit a student record.
- `delete()`: Opens the dialog to delete a student record.
- `about()`: Opens the about dialog.

### AboutDialog

A dialog that displays information about the application.

### EditDialog

A dialog that allows editing of student records.

- `__init__()`: Initializes the dialog with fields to edit a student record.
- `update_student()`: Updates the student record in the database.

### DeleteDialog

A dialog that confirms the deletion of a student record.

- `__init__()`: Initializes the dialog with confirmation options.
- `delete_student()`: Deletes the student record from the database.

### InsertDialog

A dialog that allows adding new student records.

- `__init__()`: Initializes the dialog with fields to add a student record.
- `add_student()`: Adds the student record to the database.

### SearchDialog

A dialog that allows searching for student records by name.

- `__init__()`: Initializes the dialog with a search field.
- `search()`: Searches for student records in the database.

## Database

The application uses an SQLite database (`database.db`) to store student records. The `Students` table includes the following columns:

- `id`: The student ID (integer, primary key).
- `name`: The student's name (text).
- `course`: The student's course (text).
- `mobile`: The student's mobile number (text).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
