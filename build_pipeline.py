
def build_pipeline(operation_names):
   def double(x):
        return x * 2

   def triple(x):
        return x * 3
    
   def square(x):
        return x ** 2

   def increment(x):
        return x + 1

   def decrement(x):
        return x - 1
    

   operations = {
        "double": double,
        "triple": triple,
        "square": square,
        "increment": increment,
        "decrement": decrement,
    }

   for name in operation_names:
        if name not in operations:
            raise KeyError(name)

   def pipeline(x):
        result = x
        for name in operation_names:
            result = operations[name](result)
        return result

   return pipeline

