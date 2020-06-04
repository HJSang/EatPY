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


       

