try :
    a =    [1,2,3]    ; a[4]
except IndexError :
    print ('IndexError detected.')
except :
    print ('Unknown error detected.')
try:
        print("a"+10)
except Exception:
  print("error")
a = {"a":1, "b":2, "c":3}

try:
    value = a["Z"]
except KeyError:
 print("there is no this key")
