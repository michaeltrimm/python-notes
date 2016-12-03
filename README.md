# Python Notes

## Generators vs Lists

In Python `generators` do not hold results in memory whereas `lists` do.

See the [memory.py](memory.py) file for an example.

## Lambdas

Anonymous functions `lambda`, but they different from other programming languages' definitions of anonymous functions. 

`lambda`s are *first class* functions and are treated like any other function.

## Maps

A `map` takes a `function` and an `array` as an argument, then runs each value of the `array` through the `function` and returns a new `array` of those results. 

## Operators

### Arithmetic

| Operand | Comment |
|---------|---------|
| `//` | floor division |
| `**` | expondent |
| `%` | modulus (gives remainder if any available, returns 0 if no remainder) |

### Comparison

| Operand | Comment |
|---------|---------|
| `<>` | similar to `!=` means Not Equal To |

### Assignment

| Operand | Comment |
|---------|---------|
| `+=` | ADD AND which is similar to `c += a` === `c = c + a` |
| `-=` | SUBTRACT AND which is similar to `c -= a` === `c = c - a` |
| `*=` | MULTIPLY AND which is similar to `c *= a` === `c = c * a` |
| `/=` | DIVIDE AND which is similar to `c /= a` === `c = c / a` |
| `%=` | MODULUS AND which is similar to `c %= a` === `c = c % a` |
| `**=` | EXPONDENT AND which is similar to `c **= a` === `c = c ** a` ie `c^a` |
| `//=` | FLOOR DIVISION AND which similar to `c //= a` === `c = c // a` |

### Order Of Operations

| Operand | Comment |
|---------|---------|
| `**` | EXPONENT |
| `~` `+` `-` | COMPLEMENT, UNARY PLUS `+@` AND MINUS `-@` |
| `*` `/` `%` `//` | MULTIPLY, DIVIDE, MODULUS, FLOOR DIVIDE |
| `+` `-` | ADD OR SUBTRACT |
| `>>` `<<` | BITWISE SHIFT |
| `&` | BITWISE AND |
| `^` `|` | BITWISE `OR` EXCLUSIVE `XOR` |
| `<=` `<` `>` `>=` | COMPARISON OPERATORS |
| `<>` `==` `!=` | EQUALITY OPERATORS |
| `=` `%=` `/=` `//=` `-=` `+=` `*=` `**=` | ASSIGNMENT OPERATORS |
| `is` `is not` | IDENTITY OPERATORS |
| `in` `not in` | MEMBERSHIP OPERATORS |
| `not` `or` `and` | LOGICAL OPERATORS |


## Python 3 Advantages

### Advanced Unpacking

Python 2.7.x

    >>> a, b = range(2)
    >>> a
    0
    >>> b
    1

Python 3.x

    >>> a, b, *rest = range(10)
    >>> a
    0
    >>> b
    1
    >>> rest
    [2, 3, 4, 5, 6, 7, 8, 9]

    >>> a, *rest, b = range(10)
    >>> a
    0
    >>> b
    9
    >>> rest
    [1, 2, 3, 4, 5, 6, 8]
    
    >>> *rest, b = range(10)
    >>> b
    9
    >>> rest
    [0, 1, 2, 3, 4, 5, 6, 7, 8]

### Refactor Arguments

Python 2.7.x

    def f(a, b, *args):
      # stuff

Python 3.x

    def f(*args):
      a, b, *args = args
      # stuff

## Differences Between 2.7.x and 3.x

### Integer Division

No `SyntaxError` is called when using integer division.

    print 'Python', python_version()
    print '3 / 2 =', 3 / 2
    print '3 // 2 =', 3 // 2
    print '3 / 2.0 =', 3 / 2.0
    print '3 // 2.0 =', 3 // 2.0
  
Python 2.7.6
3 / 2 = 1 `Not converted to a float`
3 // 2 = 1 `Not converted to a float`
3 / 2.0 = 1.5 `Inherits float from denominator`
3 // 2.0 = 1.0 `Inherits float from denominator`

    print('Python', python_version())
    print('3 / 2 =', 3 / 2)
    print('3 // 2 =', 3 // 2)
    print('3 / 2.0 =', 3 / 2.0)
    print('3 // 2.0 =', 3 // 2.0)

Python 3.4.1
3 / 2 = 1.5 `Converts to float from result`
3 // 2 = 1 `Not converted into a float`
3 / 2.0 = 1.5 `Converts into float from result`
3 // 2.0 = 1.0 `Converts into a float from denominator`

Notice how the `float` conversion is taking place in *Python 3* where it does not in *Python 2*...

### Unicode

#### Python 2

ASCII `str()` type
Unicode `unicode()` type
No `byte` type

    print type(unicode("this is a python3 str type"))
    # <type 'unicode'>
    
    print type(b'byte type does not exist...')
    # <type 'str'>
    
    print 'they are really' + b' the same'
    # they are really the same
    
    print type(bytearray(b'bytearray does exist in Python 2.7 though'))
    # <type 'bytearray'>


#### Python 3

Uncode `str()` UTF-8 type
2-byte class `byte` and `bytearray`

    print('Python', python_version())
    # Python 3.4.1
    
    print('strings are now utf-8 \u03BCnico\u0394é!')
    # strings are now utf-8 μnicoΔé!
    
    print('Python', python_version(), end="")
    print(' has', type(b' bytes for storing data'))
    # Python 3.4.1 has <class 'bytes'>
    
    print('and Python', python_version(), end="")
    print(' also has', type(bytearray(b'bytearrays')))
    # and Python 3.4.1 also has <class 'bytearray'>

### `xrange` and `range`

Python 3 replaced `range`'s implementation with `xrange`'s implementation to make it faster.

Python removed `xrange` since `range` now does what `xrange` did.

### For-Loops Global Namespace

Python 3 fixed a bug where in-loop variables aren't leaked into the global namespace.

### Comparing Unorderable Types

Python 3 now raises a `TypeError` when trying to order unorderable types

### Reading user input via `input()`

In Python 3 all `input()` data is stored as a `str` type rather than attempt to interpret what the data type is and then return a type such as `<type 'int'>`



### `print` function

### 2.7.x

The `print` function in Python 2.7 is known as a `statement` which can be declared with:

    print "Hello world!"
    print("Hello World!")
    print "Hello ", python_version()

Important note: When you have a `,` and multiple items inside the `print` statement, it can be processed like a tuple

    print "Python ", python_version()
    print ("a","b") # this is a tuple
    print 'a', 'b' # this is a string

### 3.x

In 3.x, the `print` function is now a `function` and not a `statement` which means it *requires* parentheses to declare.

    print("Hello world")
    print("On the same line", end=" ")
    print("as above!")

## BigO

### O(1) Constant Time

### O(n) Linear Time

  - Binary Search
  - Binary Conversion
  
### O(log n) Logarithmic Time

  - Merge Sort
  
### O(n^2) Quadratic Time

  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  
### O(n^3) Cubic Time

### O(2^n) Exponential Time
  - Brute Force
### O(n!) Factoral Time
  - Travel Salesman Problem
    
    Given a list of cities and the distances between each pair of cities, 
    what is the shortest possible route that visits each city exactly once 
    and returns to the origin city?

## Ranges

Handles one element at a time (generator)

    xrange
  
Loads all elements in memory at once
  
    range

## Lists vs Tuples

### Tuples

tuples (immutable) === heterogenous collections

  - Cannot add/remove elements to tuples via `append` `extend` `pop` `push` etc. 
  - You can `find` elements since it doesn't change the tuple
  - You can use the `in` operator to check if an element exists
  - 2x faster than lists because tuples are stored in the constants table upon declaration and referenced by the compiler at runtime
  - Tuplies help enforce the implication that data inside a tuple is like a C `const` or constant
  - Tuples can be used as dictionary keys 

### Lists
  
lists (mutable) === homogeneous collections

  - Cannot be used as dictionary keys
  - Used sort of like arrays
  - Faster than arrays usually