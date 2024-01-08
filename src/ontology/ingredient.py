from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Ingredient(Thing):
        pass


    class DryPowderIngredient(Ingredient):
        pass


    class Flour(DryPowderIngredient):
        label = [locstr("flour", "en")]


    class Salt(DryPowderIngredient):
        label = [locstr("salt", "en")]


    class Sugar(DryPowderIngredient):
        label = [locstr("sugar", "en")]


    class LiquidIngredient(Ingredient):
        pass


    class Milk(LiquidIngredient):
        label = [locstr("milk", "en")]


    class Water(LiquidIngredient):
        label = [locstr("water", "en")]


    class SolidIngredient(Ingredient):
        pass


    class WetIngredient(Thing):
        pass


    class Butter(WetIngredient):
        label = [locstr("butter", "en")]


    class Egg(WetIngredient):
        label = [locstr("egg", "en")]


    class EggWhite(Egg):
        label = [locstr("egg white", "en")]


    class EggYolk(Egg):
        label = [locstr("egg yolk", "en")]
