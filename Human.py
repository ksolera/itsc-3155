class Human:
    def __new__(cls, *args, **kwargs):
        # Here, the __new__ method of the object class must be called to create
        # and allocate the memory to the object
        print("Inside new method")
        print(f"args arguments {args}")
        print(f"kwargs arguments {kwargs}")

        # The code below calls the __new__ method of the object's class.
        # Object class' __new__ method allocates a memory
        # for the instance and returns that instance
        human_obj = super(Human, cls).__new__(cls)

        print(f"human_obj instance - {human_obj}")
        return human_obj

    # As we have overridden the __init__ method, the __init__ method of the object class will not be called
    def __init__(self, first_name, last_name):
        print("Inside __init__ method")
        # self = human_obj returned from the __new__ method

        self.first_name = first_name
        self.last_name = last_name

        print(f"human_obj instance inside __init__ {self}: {self.first_name}, {self.last_name}")

human_obj = Human("My firstname", "My lastname")