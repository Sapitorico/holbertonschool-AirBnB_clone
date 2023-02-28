<div><h1 align="center">AirBnB clone</h1> <!-- titulo -->

The objective of the project is to deploy on your server a simple copy of the Airbnb website.
The first part of this project is to create a command interpreter to manipulate data without a visual interface, as in a Shell (perfect for development and purification)
</div>

<h2 align="center">The console</h2>

## Primer paso

Write a command interpreter to manage your Airbnb objects.
Each task is linked and will help you: launch a father class that is responsible for the initialization, serialization and deserialization of your future instances to create a simple serialization/deserialization flow: instances dictionary Chain Archive Json Create all the classes usedFor Airbnb that inherit from BaseModel to create the first abstract storage engine of the project: file storage.
Second step: Write a console command to manipulate the objects of your application.
Each task is linked and will help you: Create a console command to manipulate your application objects Create the methods of creation, updating and destruction of your application objects Create the consultation methods of your objects of your application

-----

<details>
<summary><h1><a href="https://github.com/Sapitorico/holbertonschool-AirBnB_clone/blob/main/console.py">Console</a></h1></summary>

The console, HBNBCommand, is a command interpreter that allows the user to create, update, eliminate and search objects using specific commands.In other words, this console is a command line interface that interacts with program objects.

<details>
<summary><h3>Modulos</h3></summary>

* cmd: The cmd module is a standard Python library that provides a base class to create interactive consoles.This module facilitates the definition of personalized commands, the administration of arguments and the customization of the appearance of the console.It is a useful tool to create interactive command line interfaces in Python.

* Storage: It is the variable of an object that manages the storage and recovery of objects of the different classes inheriting from BaseModel.Storage is used by different methods to perform operations in objects, such as creating new objects, showing information from existing objects, eliminating objects, updating objects of object attributes, and listing objects.

</details>


<details>
<summary><h1>Subclasses</h1></summary>

# User:
    The User class is a subclass of the BaseModel class, which is used to represent a user in an application.It has four public class attributes: email, password, first_name and last_ame.

    These attributes represent the basic information of a user, such as its email address, password and full name.Inheriting the BaseModel class, the User class also has access to the attributes and methods of the base class, which allows greater flexibility and personalization in the implementation of the user functionality in the application.

# State:
    The Subclass State inheritance of the BaseModel class and represents the status of a location.It has a public class attribute called Name and represents the name of the State.

# City:
    The subclass City also inherits the BaseModel class and represents a city in a specific location.It has two public attributes: state_id and represents the id of the state associated with the city, and name and represents the name of the city.
# Amenity:
    The amenity inherited subclass of the BaseModel class and represents a comfort or service offered in one place.It has a public class attribute called name and represents the name of comfort or service.
# Place:
    The subclass place also inherits the BaseModel class and represents a place in a specific location. It has several public attributes, such as city_id, user_id, name, Description, number_rooms, number_Bathrooms, max_Guest, price_by_night, latitude, length and amenity_ids.These attributeList of comforts associated with the place.

# Review:
    The subclass review also inherits from the BaseModel class and represents a review or comment of a user on a place.It has three public attributes: place_id and represents the ID of the place associated with the review, user_id, which is an empty default chain and represents the user's ID that made the review, and text and represents the text of the review.

</details>

<details>
<summary align="center"><h1>Uso</h1></summary>

<details align="center">
<summary><h3>commands</h3></summary>

<table align="center" width="100%">

<tr>
<th>command</th>
<th align="center">Description</th>
</tr>

<tr>
<td>create</td>
<td>Create a new instance, keep it in a JSON file and show your ID</td>
</tr>

<tr>
<td>show</td>
<td>Shows the chain representation of an instance based on the name of the class and the ID</td>
</tr>

<tr>
<td>destroy</td>
<td>Eliminate an instance based on the name of the class and the ID (keep the change in the JSON file)</td>
</tr>

<tr>
<td>all</td>
<td>Shows the chain representation of all instances based or not on the name of the class</td>
</tr>

<tr>
<td>update</td>
<td>Update an instance based on the name of the class and the ID adding or updating an attribute (keep the change in the JSON file).You can only update one attribute at the same time.It can be assumed that the name of the attribute is valid (exists for this model) and that the attribute value becomes the appropriate type of attribute</td>
</tr>

</table>
</details>


The code provides a command line interpreter to manipulate objects in a database of object using the Storage module that is imported from the Models package.This interpreter accepts the following commands:

* quit: To get out of the interpreter
* EOF: equivalent to quit
* create <class name>: Create a new instance of a given class and store your data in the database.Returns the ID of the created instance.
* show <class name> <id>: It shows the chain representation of a specific instance depending on its id and class.
* destroy <class name> <id>: Eliminates a specific instance based on its id and class.
* all [class name]: It shows the chain representation of all instances stored in the database.If a class name is provided, only the instances of that class will be shown.
* update <class name> <id> <attribute name> <attribute value>: Update an attribute of a specific instance depending on your id and class.

To use this interpreter, execute the Console.py file, which imports the HBNBCommand class and the instance.In the command line, write one of the previous commands along with any required argument.Here are some examples:

* To create a new instance of the User class:
```py
(hbnb) create User
```

* To show the instance chain representation with ID 123 of the State class:
```py
(hbnb) show State 123
```

* To eliminate the instance with ID 456 of the City class:
```py
(hbnb) destroy City 456
```

* To show all instances stored in the database:
```py
(hbnb) all
```

* To show all instances of the amenity class:
```py
(hbnb) all Amenity
```

* To update the Name attribute of the instance with ID 789 of the Place class to New York:
```py
(hbnb) update Place 789 name "New York"
```

</details>


</details>




<table align="center" width="100%"> <!-- tabla de clases -->

<tr> <!-- columnas de la tabla -->

<th>constructionClasses</th>
<th>description</th>
<th>testsFiles</th>

</tr>

<tr> <!-- fila 1  -->

<td><a href="https://github.com/Sapitorico/holbertonschool-AirBnB_clone/blob/main/models/base_model.py">BaseModel</a></td> <!-- Class columna 1-->

<td> <!-- description -->

<details>
<summary><h2>BaseModel</h2></summary>

It is the base class of all Airbnb models.This class is in charge of managing the serialization/deerialization of the attributes of the other models, and to save in a JSON file all the instantaneous objects.It is also the base class of all other Airbnb models, so it inherits from it.

<h3>Modules</h3>

* uuid:
    The UUID module in Python provides immutable UUID objects (the UUID class) and the UUID1 (), UUID3 (), UUID4 (), UUID5 () functions to generate universally unique identifiers.The UUID Version 1 values are calculated using the MAC address ((Mac Address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address) of the host, while version 4 uses pseudo-Random Number Generators to generate UUIDS.The module also offers a tool to shorten the UUIDS for use in URLs
* datetime:
    The Datetime module in Python provides classes to manipulate dates and hours, allowing arithmetic operations with dates and hours.You can create a datetime manually passing the parameters (Year, Month, Day, Hour = 0, Minute = 0, Second = 0, Microscond = 0, Tzinfo = None).To work with dates in Python, the datetime module that incorporates the Date, Time and Datetime data to represent dates and hours must be imported.

* storage:
    The Storage variable provides data storage and recovery functionalities.The New () function of the Storage module is used to register a new class instance in the application.In addition, the Save () method uses the Storage module to save the changes in the instance

<h3>Public instance attributes:</h3>
    id: string - assigns a unique identifier to each instance created
    creates_at: assign an exact date and time in which the instance was created
    updated_at: assign an exact date and time in which the instance was updated

<h3>METHODS:</h3>

* save: It is a method that updates the value of the UPDATED_AT attribute with the current date and time of the system

* to_dict: Returns a dictionary with all the attributes of the instance in the form of key-value.This method is used to serialize instance information and turn it into a format that can be stored or transmitted through a network

</details>
</td>

<td><a href="https://github.com/Sapitorico/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py">test_base_model</a></td>



</tr> <!-- fin de fila 1-->

<td><a href="https://github.com/Sapitorico/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py">FileStorage</a></td>


<td>

<details>
<summary><h2>FileStorage</h2></summary>

Filestorage is a class that is used to handle persistent storage of objects in a web application.It focuses on file storage and is used to separate the storage management of the logic of the model, which allows modular and independent models.By using class attributes instead of instance attributes, a clear description and predetermined value of any attribute are provided, allowing a consistent behavior of the model in any storage system used.In summary, Filestorage is an implementation of a file storage system using the JON format to store information about classes.


<h3>Modules</h3>

* json:
    It provides a way to code and decode JSON data.It is used to convert Python objects into a serialized representation that can be stored in a file or transmitted through the network.The Module (%) operator in Python is used to obtain the rest of a division.

* os.path:
    In Python it is used for different purposes, such as merger, normalization and recovery of route names in Python.

</details>
</td>
<td><a href="https://github.com/Sapitorico/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py">test file_storage</a></td>


<tr>

</table>



-----


<details>
<summary><h2 align="center">Resources</h2></summary>

# *args and **kwargs in python explained

A python, "args" and "kwargs" They are two special parameters that can be used in the definitions of the functions to receive variable arguments.

"Args" It is a parameter that allows a function to receive a variable number of unpalled arguments.This means that any amount of arguments can be passed to the function and Python will all pack them in a tupla.Let's look at an example:

```py
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```

In this example, we define a function called my_function with a parameter *args.Then we call the function with three arguments: 1, 2 and 3. By printing the args values in the body of the function, we obtain:

```
1
2
3
```

This means that Python packed the arguments in a tupla and passed them to the function.

"Kwargs" It is a parameter that allows a function to receive a variable number of arguments named.This means that any amount of arguments can be passed with a specific name to the function and Python will pack them in a dictionary.Let's look at an example:

```py
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='Alice', age=30, city='New York')
```

In this example, we define a function called my_function with a parameter ** kwargs.Then we call the function with three arguments named: Name, AGE and City.By printing Kwargs values in the body of the function, we get:

```py
name Alice
age 30
city New York
```

This means that Python packed the arguments named in a dictionary and passed them to the function.

In summary, "args" y "kwargs" They are special parameters that allow Python functions to receive variable arguments."ARGS" is used to receive unpalled arguments, while "Kwargs" is used to receive appointed arguments.These parameters can help make functions more flexible and easy to use.

# JSON encoder and decoder

The bookstore "json" Python allows you to encode and decode data in JSON format.JSON is a light and easy -to -read data format that is commonly used in web and mobile applications to send and receive data.
Once we have imported the bookstore, we can use its functions to code and decode data in JSON format.For example, to encode a Python dictionary in JSON format, we can use the JSON.DUMPS () function:

```py
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_str = json.dumps(my_dict)
print(json_str)
```

In this example, we create a dictionary called My_DICT and then we encode it in JSON format using the JSON.DUMPS () function.Then we print the JSON chain resulting in the console.

To decode a JSON chain in a python object, we can use the JSON.Loads () function:

```py
json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
my_dict = json.loads(json_str)
print(my_dict)
```

In this example, we create a JSON chain called JSON_STR and then decode it in a Python dictionary using the JSON.Loads () function.Then we print the resulting dictionary in the console.

The "JSON" bookstore also provides advanced options to customize the coding and decoding process.For example, we can provide a personalized function to encode an object in JSON format using the default parameter of the JSON.DUMPS () function:

```py
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def encode_person(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age, 'city': obj.city}
    else:
        raise TypeError('Object of type Person is not JSON serializable')

my_person = Person('Alice', 30, 'New York')
json_str = json.dumps(my_person, default=encode_person)
print(json_str)
```

In this example, we define a person who represents a person with a name, an age and a city.Then we define an ENCODE_PERSON () function that is used to encode class objects in JSON format.Finally, we create an My_person object of the Person class and we encode it in JSON format using the JSON.DUMPS () function and the default parameter.

In summary, Python's "JSON" bookstore allows you to code and decode data in JSON format.This is useful for sending and receiving data in web and mobile applications.The bookstore provides simple functions to encode and decode data, as well as advanced options to customize the coding and decoding process.

# Unitests

The Unittest library of Python is an integrated test frame that is used to write and execute unit tests in Python.Unittest provides a series of classes and methods to create and execute unit tests.

To use the Unittest library, we must first import it:
```py
import unittest
```

Then, we can create a proof class that inherits Unittest.testcase.Within this class, we can define different methods that contain the unit tests that we want to execute.For example, the following code defines a simple test class with a unitary test:
```py
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)
```

In this example, we create a class called Mytestcase that inherits Unittest.testcase.Then we define a method called test_addition () that performs a simple unitary test.The test compares the result of 1 + 2 with the expected value of 3 using the Assertequal () method of Unittest.testcase.

To execute our unit tests, we can use the Unittest.Main () method.For example, we can add the following code at the end of our trial file to execute all the unit tests defined in our test class:

```py
if __name__ == '__main__':
    unittest.main()
```

The Unittest library provides a wide variety of assertion methods that are used to verify the expected behavior of our code in the unit tests.Some of the most common assertion methods include:

ASSERTEQUAL (A, B): Verify if A and B are equal Assertnotequal (A, B): Verify if A and B are not the same assertrue (x): Verify if x is true Assertfalse (x): Verify if x is false assertin (A, B): Verify if A is in B Assertinin (A, B): Verify if A is not in B asSertrais (Exception, Callable, *Args, ** KWDS): Verify if CALLABLE ( *ARGS, ** KWDS) generates an exceptionOf the exception type, an example of how to use some of these assertion methods in a unit test is shown below:

```py
class MyTestCase(unittest.TestCase):
    def test_math(self):
        # Verificar la suma
        self.assertEqual(1 + 2, 3)

        # Verificar la resta
        self.assertEqual(5 - 2, 3)

        # Verificar la multiplicación
        self.assertEqual(2 * 3, 6)

        # Verificar la división
        self.assertEqual(6 / 2, 3)

        # Verificar si una cadena está en otra
        self.assertIn('hello', 'hello world')

        # Verificar si se produce una excepción
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)
```

In this example, we define a test_Math () test method that performs several unit tests using different assertion methods.The test verifies the sum, subtraction, multiplication and number division, and also verifies whether one chain is contained in another.The last test uses the Assertrais () method to verify if an exception of division by zero occurs when executing a zero division operation.

In addition to the assertion methods, the Unittest library also provides a series of methods to configure and clean the tests, as well as to group and execute tests more effectively.Some of these methods include:

Setup (): It is executed before each test and is used to configure the test environment.Teardown (): It is executed after each test and is used to clean the test environment.Setupclass (): It is executed once at the beginning of the execution of all the tests and is used to configure the test environment at class level.Teardawnclass (): It is executed once at the end of the execution of all the tests and is used to clean the proof environment at class level.Skip (Reason): It is used to omit a test and an optional reason for omission can be provided.Below is an example of how to use some of these methods in a test class:

```py
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar el entorno de prueba a nivel de clase
        pass

    def setUp(self):
        # Configurar el entorno de prueba
        pass

    def test_addition(self):
        # Verificar la suma
        self.assertEqual(1 + 2, 3)

    @unittest.skip("Esta prueba está desactivada temporalmente")
    def test_subtraction(self):
        # Verificar la resta
        self.assertEqual(5 - 2, 3)

    def tearDown(self):
        # Limpiar el entorno de prueba
        pass

    @classmethod
    def tearDownClass(cls):
        # Limpiar el entorno de prueba a nivel de clase
        pass
```

In this example, we define a MyTestCase test class that uses the Setup (), Teardown (), Setupclass () and Teardownclass () methods to configure and clean the test environment.We also use the SKIP () method to temporarily omit a subtraction test.

In summary, Unittest is a Python library that is used to write and execute unit tests.It allows to define unit tests using different assertion methods and provides methods to configure and clean the test environment.Unittest is an essential tool to guarantee the quality of the code and reduce errors in Python projects.

</details>

---

<footer align="center">
<p align="center"><h3>Authors:</h3><p>
<p align="center"><a href="https://github.com/Sapitorico" target="blank">Sapitorico</a></p>
<p align="center"><a href="https://github.com/NeoDau" target="blank">NeoDau</a></p>
</footer>