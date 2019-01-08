def packer(**kwargs):
    print(kwargs)

    
def packer2(name=None, **kwargs):
    print (kwargs)

    
def unpacker(example=None, first_name=None, last_name=None):
    if first_name and last_name:
        print("{}:  Hi {} {}!".format(example, first_name, last_name))
    else:
        print("Hi no name!")



packer(example=1, name="Obi Won Kinobi", num=42, spanish_inquisition=None)
packer2(example=2, name="Obi Won Kinobi", num=42, spanish_inquisition=None)
unpacker(**{"example": "Example 3", "last_name": "Kinobi", "first_name": "Obi"})
