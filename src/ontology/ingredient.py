from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Ingredient(Thing):
        pass


    class DryPowderIngredient(Ingredient):
        pass


    class Flour(DryPowderIngredient):
        pass


    class Salt(DryPowderIngredient):
        pass


    class Sugar(DryPowderIngredient):
        pass


    class LiquidIngredient(Ingredient):
        pass


    class Milk(LiquidIngredient):
        pass


    class Water(LiquidIngredient):
        pass


    class SolidIngredient(Ingredient):
        pass


    class WetIngredient(Thing):
        pass


    class Butter(WetIngredient):
        pass


    class Egg(WetIngredient):
        pass


    class EggWhite(Egg):
        pass


    class EggYolk(Egg):
        pass
