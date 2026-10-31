# Django Student Management System (Full CRUD Project)

**Internship Task 30** — Python Development at **Logirtha Technologies Private Limited**

## 📌 Project Overview
A full-stack web-based **Student Management System** built with **Python** and **Django** using an **SQLite** database. The application allows administrators and institutes to create, view, update, delete (CRUD), filter, and search student records through a clean, responsive Bootstrap 5 user interface.

---

## ✨ Key Features

### Core CRUD & Search Features
- **Add Student (Create):** Validated `ModelForm` to register new students with name, email, phone number, course, date of birth, and address.
- **View Student List (Read):** Displays all student records in a responsive table ordered by creation date.
- **Update Student Details (Update):** Pre-populated form to edit existing student records.
- **Delete Student (Delete):** Dedicated confirmation page before permanently removing a record.
- **Multi-Field Search:** Case-insensitive search across **Student Name**, **Email Address**, and **Course** using Django `Q` objects.

### Bonus Challenges Implemented
- ✅ **Total Student Counter:** Displays the total count of matching student records dynamically.
- ✅ **Pagination:** Paginates student records (5 per page) while preserving active search and course filter parameters.
- ✅ **Course-Wise Filtering:** Dynamic dropdown menu to filter records by specific courses.
- ✅ **Flash Messages:** Displays Bootstrap success alerts after adding, updating, or deleting records.
- ✅ **Export to CSV/Excel:** One-click export of all student records to a downloadable `students_records.csv` file.
- ✅ **Student Profile Photos:** Supports uploading and displaying student profile photos (`ImageField` with `Pillow`).

---

## 🛠️ Tech Stack
- **Backend:** Python 3, Django
- **Database:** SQLite3
- **Frontend:** HTML5, Bootstrap 5, Django Template Language (Template Inheritance via `base.html`)
- **Image Processing:** Pillow

---

## 📂 Project Structure
```text
internship_project/
├── manage.py
├── db.sqlite3
├── internship_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── students/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
        ├── base.html
        └── students/
            ├── student_list.html
            ├── student_form.html
            └── student_confirm_delete.html
