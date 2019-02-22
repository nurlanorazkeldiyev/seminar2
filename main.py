from mybox import MyBox
from myboxiterator import MyBoxIterator
from myclass import travell	
a=MyBox ()
a.add (travell('Italy', 'Rome', 'June'))
a.add (travell('England', 'London', 'september'))
a.add (travell('Kazakhstan', 'Taraz', 'march'))
a.remove ( 1  )
for i in a:
    i.meth_1()

