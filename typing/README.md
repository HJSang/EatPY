# typing -- Suport for type hints
* The most fundamental support consists of the types: ``Any, Union, Tuple, Callable, TypeVar`` and ``Generic``.
```python
def greeting(name: str) -> str:
  return 'Hello' + name
```
* Type aliases
  * A type alias is defined by assigning the type to the alias.
  * For example:
  ```python
  from typing import List
  Vector = List[float]
  def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num fpr num in vector]
  ```
  * Type aliases are useful for simplifying complex type signatures.
  ```python
  from typing import Dict, Tuple, Sequence
  ConnectionOptions = Dict[str, str]
  Address = Tuple[str, int]
  Server = Tuple[Address, ConnectionOptions]
  def boardcast_message(message: str, servers: Sequence[Server]) -> None:
    pass
  ```
  * Note that ``None`` as a type hint is a special case

* NewType
  * Use the ``NewType()`` helper function to create distinct types:
  ```python
  from typing import NewType
  UserId = NewType('UserId', int)
  some_id = UserId(54321)
  def get_user_name(user_id: UserId) -> str:
    ...
  ```

* Callable
  * Frameworks expecting callback functions of specific signatures might be type hinted using ``Callable[[Arg1Type, Arg2Type], ReturnType]``.
  * For example:
  ```python
  from typing import Callable
  def feeder(get_next_item: Callable[[], str]) -> None:
    #Body
  ```

* Generics
  * Generics can be parameterized by using a new factory available in typing called ``TypeVar``.
  * For example:
  ```python
  from typing import TypeVar, Generic
  from logging import Logger

  T = TypeVar('T')

  class LoggedVar(Generic[T]):
      def __init__(self, value: T, name: str, logger: Logger) -> None:
          self.name = name
          self.logger = logger
          self.value = value

      def set(self, new: T) -> None:
          self.log('Set ' + repr(self.value))
          self.value = new

      def get(self) -> T:
          self.log('Get ' + repr(self.value))
          return self.value

      def log(self, message: str) -> None:
          self.logger.info('%s: %s', self.name, message)
  ```
