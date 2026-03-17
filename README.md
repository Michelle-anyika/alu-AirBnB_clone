# AirBnB Clone Project

##  Project Description 

This project is the first step in building a full web application that replicates the core features of AirBnB.

The goal is to develop a **command-line interpreter** that manages different objects (like users, places, cities, etc.) and handles data storage through serialization and deserialization.

This project lays the foundation for:

* Frontend development (HTML/CSS)
* Backend APIs
* Database integration
* Full-stack web application development

---

##  Command Interpreter 

###  What it does 

The command interpreter allows you to:

* Create new objects (e.g., User, Place)
* Retrieve stored objects
* Update object attributes
* Delete objects
* Perform operations like counting instances

---

##  How to Start 

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/alu-AirBnB_clone.git
cd alu-AirBnB_clone
```

### 2. Make the console executable

```bash
chmod +x console.py
```

### 3. Run the console

#### Interactive mode:

```bash
./console.py
```

#### Non-interactive mode:

```bash
echo "help" | ./console.py
```

---

##  How to Use 

Once inside the console:

```bash
(hbnb)
```

### Available commands:

| Command | Description             |
| ------- | ----------------------- |
| help    | Show available commands |
| quit    | Exit the console        |
| EOF     | Exit the console        |

---

##  Examples 

### Start console

```bash
$ ./console.py
(hbnb)
```

### Show help

```bash
(hbnb) help
```

### Exit console

```bash
(hbnb) quit
$
```

### Non-interactive example

```bash
$ echo "help" | ./console.py
```

---

##  Project Structure 

```
alu-AirBnB_clone/
│
├── models/              # All class models
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── place.py
│   └── amenity.py
│
├── tests/               # Unit tests
│   └── test_models/
│
├── console.py           # Command interpreter
├── README.md
└── AUTHORS
```

---

##  Core Concepts Implemented 

* Object-Oriented Programming (OOP)
* Inheritance
* Serialization & Deserialization
* JSON file handling
* UUID for unique object IDs
* Datetime management
* Command-line interface using `cmd` module
* Unit testing with `unittest`

---

##  Technologies Used 

* Python 3.8+
* cmd module
* unittest
* JSON
* Linux / Ubuntu environment

---

##  Running Tests 

Run all tests:

```bash
python3 -m unittest discover tests
```

Run a specific test file:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

---

##  Authors 

See the `AUTHORS` file for the list of contributors.

---

##  Future Improvements 

* Add more models (Place, Review, etc.)
* Connect to a database (MySQL)
* Build RESTful APIs
* Develop frontend interface
* Deploy as a full web application

---

