# Note for Object Oriented Programming in Python
## Class and Instance

In Python, **class** is used to define the class object. For example,
```python
class Student:
  # __init__ is a special method to initialize
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def study(self, course_name):
    print('%s is studying %s.'%(self.name, course_name))
  def watch_movie(self):
    if self.age < 18:
      print('Not an adult')
    else:
      print('Andult')
```
Note that, functions in class are called methods.

how to create and use class and its methods?

```python
def main():
  stu1 = Student('xxx', 20)
  stu1.study('Python')
  stu1.watch_movie()

if __name__=='__main__':
  main()
```

How to access class methods and attributes? The common attributes are public. If you want to use private or protected attributes, please use '__' to start the attribute names.

```python
Class Test:
  def __init__(self,foo):
    self.__foo = foo
  def __bar(self):
    print(self.__foo)
    print('__bar')

def main():
  test = Test('hello')
  # AttributeError: 'Test' object has no attribute '__bar'
  test.__bar()
  # AttributeError: 'Test' object has no attribute '__foo'
  print(test.__foo)

if __name__ == '__main__':
  main()
```
In fact, you can always access all atrributes, even they are private. You can access by ** test._Test__bar()**.


## @property decorator
If you want to access the private atrribute, you can use the @property: **getter** and **setter**.

```python
class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, age):
    self._age = age

  def play(self):
    if self._age <=18:
      print('age <= 18')
    else:
      print('age > 18')

def main():
  person = Person('xxx', 12)
  person.Play()
  person.age = 22
  person.play()
  # person.name = 'aaa' # AttributeError: cannot set attribute

if __name__ == '__main__':
  main()
```



       

