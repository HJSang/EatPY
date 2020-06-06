# Note for Object Oriented Programming in Python
The notes are summarized from this [blog](https://github.com/HJSang/Python-100-Days/blob/master/Day01-15/09.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E8%BF%9B%E9%98%B6.md).

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

## __slot__
We can use **__slot__** to limit the attributes. 
```python
Class Person:
  __slot__ = ('_name', '_age', '_gender')
  
  def __init__(self, name, age):
    self._name = name
    self._age = age

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  
  @ag.esetter
  def age(self,age):
    self._age = age

def main():
  person = Person('xxx', 22)
  person._gender = 'male'
  # AttributeError: 'Person' object has no attribute '_who'
  # person._who = 'nobody'
```


## Static and class methods
This is summarized from this [stack overflow blog](https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod#:~:text=%40staticmethod%20function%20is%20nothing%20more,a%20bound%2Dmethod%20for%20object.)

A **staticmethod** is a method that knows nothing about the class or instance it was called on. It is callable without instantiating the class first. It's definitionis immutable via inheritance.

**Classmethod** function also callable without instantiating the class, but its definition follows Sub class, not Parent class via inheritance. Th is beclasee the first argument for @classmethod function must always be **cls** (class).

Both methods are used by **decorators** @classmethod and @staticmethod.

```python
class Triangle:
  def __init__(self,a,b,c):
    self._a = a
    self._b = b
    self._c = c

  @staticmethod
  def is_valid(a,b,c):
    return a+b>c and b+c>a and a+c>b

  def perimeter(self):
    return self._a + self._b + self._c

def main():
  a,b,c = 3,4,5
  if Triangle.is_valid(a,b,c):
    t = Triangle(a,b,c)
    print(t.perimeter())
  else:
    print('Not a Triangle!')

if __name__ == '__main__':
  main()
``` 

       

