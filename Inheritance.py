class VegPreparation:
    """handle basic vegetable preparation steps such as washing and cutting.

    This class interacts with the user to simulate preparation of vegetables
    using input-based steps interactively."""

    def __init__(self, vegetables: list[str]) -> None:
        """
        Initialize the VegPreparation object with a list of vegetables.
        """
        self.vegetables = vegetables

    def __str__(self) -> str:
        """Return a user-friendly string representation of the object.

        """
        return f"Vegetables to prepare: {self.vegetables}"

    def __repr__(self) -> str:
        """ Return a developer-friendly representation of the object.
        """
        return f"{self.__class__.__name__}(vegetables={self.vegetables})"

    def wash(self) -> list[str]:
        for veg in self.vegetables:
            while True:
                check = input(f'Is {veg} clean? yes/no: ')

                if check == 'yes':
                    print(f'{veg} is clean')
                    break
                elif check == 'no':
                    print(f'Wash {veg} again!')
                else:
                    print("Invalid input!")

        print("All vegetables are clean")
        return self.vegetables


    def cut(self) -> None:
        for veg in self.vegetables:
            while True:
                cut = input(f'Is {veg} cut? yes/no: ')

                if cut == 'yes':
                    print(f'{veg} is cut')
                    break
                elif cut == 'no':
                    print(f'Please finish cutting {veg}')
                else:
                    print("Invalid input!")

        print("All vegetables are cut")

class TypeOfCooking(VegPreparation):
    """Simulate a cooking workflow for a vegetable dish.

    This class will perform the cooking steps of Cabbage dish using user input"""
    @staticmethod
    def stove_checking() -> None:
        """
            Check whether the stove can be turned on and gas Availability
        """
        while True:
            check_stove = input("Enter on/off to on the stove:")
            gas_available = input("Enter yes/no to check gas available:")
            if check_stove == "on" and gas_available == "yes":
                print("Stove is on")
                print("Place pan on stove")
                break
            elif check_stove == "on" and gas_available == "no":
                print("Gas not available! Cannot start stove")
                continue
            else:
                print("Stove is off")


    @staticmethod
    def ingredient_checking()-> str:
        """
           Handle adding oil and checking whether it is heated
           before proceeding to the next cooking step.
        """

        while True:

            add_ingredients = input("Add oil yes/no: ")
            if add_ingredients == "yes":
                print("Oil is poured.")
                while True:
                    heated = input("Is the oil heated yes or no: ")
                    if heated == "yes":
                        print("Add mustard to oil.")
                        return "Wait Oil is burst"
                    elif heated == "no":
                        print("Wait for the oil to be heated.")
                        continue
                    else:
                        print("Invalid input! Please enter 'yes' or 'no'.")

            elif add_ingredients == "no":
                print("Oil is not available. Buy from shop or neighbors.")
                continue

            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        return "Oil check not completed"

    @staticmethod
    def check_oil_is_burst()-> None:
        """
            Check whether the oil is burst before proceeding to the next cooking step
        """

        while True:

            burst = input("Is it burst enter yes/no:")
            if burst == "yes":
                print("Ready to add curry leaves")
                break
            else:
                print("wait for burst")



    @staticmethod
    def add_onion_to_pan()-> str:
        """
            Add onion to the pan and wait until it is properly fried.
        """
        while True:

            add_onion = input("Add onion to the pan? yes/no: ")
            if add_onion == "yes":
                print("Onion is added to the pan.")
                while True:
                    fry = input("Is the onion fry? yes/no: ")
                    if fry == "yes":
                        print("Onion is perfectly cooked.")
                        return "Add cut cabbage"
                    elif fry == "no":
                        print("Wait until onion is cooked.")
                        continue
                    else:
                        print("Invalid input! Please enter 'yes' or 'no'.")
            elif add_onion == "no":
                print("Please add onion to proceed.")
                continue
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        return "Onion cooking not completed"

    @staticmethod
    def check_cabbage_cook()-> None:
        """
            Check whether the cabbage is fully cooked.
        """

        while True:

            cabbage = input("Is the cabbage cook? yes/no: ")
            if cabbage == "yes":
                print("Cabbage is cooked.")
                break
            else:
                print("Wait until cabbage is cooked.")

    @staticmethod
    def mixing_ingredients(items:list[str])-> None:
        """
            Add a list of ingredients into a mixing jar one by one
            based on user input.
        """
        for k in items:
            while True:

                add = input(f"Add {k} to mixing jar? yes/no: ")
                if add == "yes":
                    print(f"{k} added to mixing jar.")
                    break
                elif add == "no":
                    print(f"Please add {k} to proceed.")

                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")


        print("All ingredients are in the jar.")
    @staticmethod
    def grinder_start()-> None:
        """
            Start the grinder based on user input
        """

        while True:

            starting_grinder = input("Would you like to start grinder? yes/no: ")
            if starting_grinder == "yes":
                print("It is grind well")
                break
            else:
                print("Wait until grinder is grind well.")



    @staticmethod
    def add_mixture_to_cabbage()-> None:
        """
            Add the prepared mixture to the cooked cabbage and
            verify salt before finishing the dish.
        """

        while True:

            mix = input("Add mixture to cabbage? yes/no: ")
            if mix == "yes":
                print("Mixture added.")


                while True:
                    salt = input("Check the salt is crt or not yes/no: ")
                    if salt == "yes":
                        print("stir it well and close the lid the dish is ready!")
                        break
                    else:
                        print("Please add salt and stir it properly.")
                break
            else:
                print("Add mixture to proceed.")


if __name__ == "__main__":
    cabbage_kootu = TypeOfCooking(
        vegetables = ["Cabbage", "Green chilli", "Curry leaves", "Onion"])
    print(repr(cabbage_kootu))
    print(cabbage_kootu)
    cabbage_kootu.wash()
    cabbage_kootu.cut()
    cabbage_kootu.stove_checking()
    cabbage_kootu.ingredient_checking()
    cabbage_kootu.check_oil_is_burst()
    cabbage_kootu.add_onion_to_pan()
    cabbage_kootu.check_cabbage_cook()
    mixture = ["Cumin", "Garlic", "Green chilli", "Turmeric", "Grated Coconut"]
    cabbage_kootu.mixing_ingredients(mixture)
    cabbage_kootu.grinder_start()
    cabbage_kootu.add_mixture_to_cabbage()
