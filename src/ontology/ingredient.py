from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")
obo = get_ontology("http://purl.obolibrary.org/obo/")

with onto:
    class Ingredient(Thing):
        pass


    class DryIngredient(Ingredient):
        pass


    class SolidIngredient(DryIngredient):
        comment = ["of uniformly close and coherent texture : not loose or spongy : compact"]


    class PowderIngredient(DryIngredient):
        pass


    class FOODON_03316449(PowderIngredient):
        namespace = obo
        label = [locstr("baking supply")]


    class FOODON_00004510(PowderIngredient):
        namespace = obo
        label = [locstr("flour", "en")]


    class FOODON_00002221(PowderIngredient):
        namespace = obo
        label = [locstr("salt", "en")]


    class FOODON_03301073(PowderIngredient):
        namespace = obo
        label = [locstr("sugar (granulated)", "en")]


    class WetIngredient(Ingredient):
        pass


    class LiquidIngredient(WetIngredient):
        pass


    class FOODON_03302116(LiquidIngredient):
        namespace = obo
        label = [locstr("cows milk", "en")]


    class FOODON_00002340(LiquidIngredient):
        namespace = obo
        label = [locstr("water", "en")]


    class FOODON_03310387(LiquidIngredient):
        namespace = obo
        label = [locstr("oil", "en")]


    class FOODON_00001073(LiquidIngredient):
        namespace = obo
        label = [locstr("vinegar", "en")]


    class FOODON_03311146(LiquidIngredient):
        namespace = obo
        label = [locstr("sauce", "en")]


    class SemiLiquidIngredient(WetIngredient):
        pass


    class FOODON_03302515(SemiLiquidIngredient):
        namespace = obo
        label = [locstr("sour cream", "en")]


    class FOODON_00001014(SemiLiquidIngredient):
        namespace = obo
        label = [locstr("yogurt", "en")]


    class FOODON_00001178(SemiLiquidIngredient):
        namespace = obo
        label = [locstr("honey", "en")]


    class FOODON_00001772(SemiLiquidIngredient):
        namespace = obo
        label = [locstr("butter", "en")]


    class FOODON_03315102(SemiLiquidIngredient):
        namespace = obo
        label = [locstr("egg", "en")]
