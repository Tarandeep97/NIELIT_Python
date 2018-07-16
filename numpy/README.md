## Numpy Shorthand notes



Numpy arrays extend the functionality of Python list with lots of features like
Element-wise multiplication/Addition/Subtraction/Division

```python
    import numpy as np
    x = np.array([1,2,3])
    print(x * 2)
```
> Output : [2 , 4 , 6]

Numpy arrays assume all elements of same type
```python
  import numpy as np
  x = np.array([1,'one',2.2]      #Here adding a string element turns each element to string type
  print(x)
```
> Output :['1' , 'one' , '2.2']
