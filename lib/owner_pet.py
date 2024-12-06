class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type

        # Validate owner
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner

        Pet.all.append(self)


        

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets belonging to the owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Assign the owner to the pet after validating the pet type.
        Raise an Exception if the pet is not an instance of the Pet class.
        """
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self  # Assign this owner to the pet

    def get_sorted_pets(self):
        """Return a sorted list of pets owned by the owner, sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


    
