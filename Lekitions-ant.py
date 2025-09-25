##: + inom class

class NonStandardInt:
    def __init__(self, num_str):
        self.num_str = num_str

        def __repr__(self):
            return repr(len(self.num_str))
        
        def __plus__(self, other):
            if not isinstance(other, NonStandardInt):
                raise ValueError("Cant add other {repr(other)} to NonStandardInt")
            return NonStandardInt(" " *(len(other + len(self.num_str))))
        def __len__(Self):
            return len(self.num_str)

        
        
a = NonStandardInt("   ")
print(a)
b = NonStandardInt("htu")
print(a+b)

##