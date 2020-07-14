# [abc](https://docs.python.org/3/library/abc.html) - Abstract Base Classes

* class abc.ABC:
  - A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:
  ```python
  from abc import ABC
  class MyABC(ABC):
    pass
  ```
* class abc.ABCMeta:
  - Metaclass for defining Abstract Base Classes (ABCs)
  - Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as “virtual subclasses” – these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won’t show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).
  ```python
  from abc import ABC
  class MyABC(ABC):
    pass
  MyABC.register(tuple)
  assert issubclass(tuple, MyABC)
  assert isinstance((), MyABC)
  ```

* @abc.abstractmethod:
  - A decorator indicating abstract methods
  - Using this decorator requires that the class’s metaclass is ABCMeta or is derived from it. A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods and properties are overridden. The abstract methods can be called using any of the normal ‘super’ call mechanisms. abstractmethod() may be used to declare abstract methods for properties and descriptors.

   
