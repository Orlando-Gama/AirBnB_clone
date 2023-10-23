PROJECT NAME: 0x00. AirBnB clone - The console

0. README, AUTHORS
mandatory
Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page

1. Be pycodestyle compliant!
mandatory
Write beautiful code that passes the pycodestyle checks.

2. Unittests
mandatory
All your files, classes, functions must be tested with unit tests
3. BaseModel
mandatory
Write a class BaseModel that defines all common attributes/methods for other classes:

models/base_model.py
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>

4. Create BaseModel from dictionary
mandatory
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.
5. Store first object
mandatory
Now we can recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)
It’s not human readable
Using this file with another program in Python or other language will be hard.
6. Console 0.0.1
mandatory
Write a program called console.py that contains the entry point of the command interpreter:

You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything

7. Console 0.1
mandatory
Update your command interpreter (console.py) to have these commands:

create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
If the class name is missing, print ** class name missing ** (ex: $ create)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ show)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)

8. First User
mandatory
Write a class User that inherits from BaseModel:

models/user.py
Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
9. More classes!
mandatory
Write all those classes that inherit from BaseModel:

State (models/state.py):
Public class attributes:
name: string - empty string
City (models/city.py):
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string
Amenity (models/amenity.py):

10. Console 1.0
mandatory
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!

No unittests needed for the console

11. All instances by class name
#advanced
Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().

12. Count instances
#advanced
Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
13. Show
#advanced
Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).

Errors management must be the same as previously.
14. Destroy
#advanced
Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).

Errors management must be the same as previously.
15. Update
#advanced
Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

Errors management must be the same as previously.
16. Update from dictionary
#advanced
Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

Errors management must be the same as previously.
17. Unittests for the Console!
#advanced
Write all unittests for console.py, all features!

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:

