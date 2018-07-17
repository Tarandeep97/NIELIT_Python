## Numpy Shorthand notes



Numpy arrays extend the functionality of Python list with lots of features like
**element-wise** multiplication, addition, subtraction or division
```python
    import numpy as np
    x = np.array([1,2,3])
    print(x * 2)
```
> [2 , 4 , 6]

Numpy arrays assume all elements of same type
```python
  import numpy as np
  x = np.array([1,'one',2.2]      #Here adding a string element turns each element to string type
  print(x)
```
> ['1' , 'one' , '2.2']

#### Subsetting array follow same technique as used in lists
```python
   import numpy as np
   a = np.array([2,3,4])
   print(a[0])
```
> 2

To subset numpy arrays , Boolean operators (==, !=, >, <) can also be used. 

```python
   a = np.array([1,2,3,4])
   print(a<3)
   print(a[a<3])
```
> [True  True]  #array of Bool type

  [1,2]

    
