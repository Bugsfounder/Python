# CAN YOU CHANGE THE SELF PARAMETER INSIDE A CLASS TO SOMETHING ELSE (SAY "HARRY"). TRY CHANGING SELF TO 'SLF' OR 'MANISHA' AND SEE THE EFFECT

class ChangeSelf:
    def __init__(manisha, name):
        manisha.name = name
        print(f"The Name is: {manisha.name}")


ch = ChangeSelf("Hello Manisha")
