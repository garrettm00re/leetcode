# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # INGREDIENTS = NODES o o o o o o o
        # DRAW EDGES FROM INGREDIENTS TO RECIPES (also nodes) 
        # for each supply: delete if a node with the name exists
        # explore the graph: see which recipes cant be reached (these can be created)
        # delete recipes that can be created (in the event of recipe dependencies)
        # rerun to see if any recipes (whic)

        #edge case: supply == recipe? // All the values of recipes and supplies combined are unique. 

        # graph = defaultdict(list) # ingredients -> recipes
        # for recipe, ingredientList in zip(recipes, ingredients):
        #     for ingredient in ingredientList:
        #         graph[ingredient].append(recipe)
        canCreate = []
        remaining = [set(ingredientList) for ingredientList in ingredients]
        ingredientToRecipe = defaultdict(list) # maps ingredients to the list of recipe indices that require them
        for recipeIdx, ingredientList in zip([i for i in range(len(recipes))], ingredients):
            for ingredient in ingredientList:
                ingredientToRecipe[ingredient].append(recipeIdx)

        while supplies:
            newSupplies = []
            for supply in supplies:
                if supply in ingredientToRecipe:
                    for recipeIdx in ingredientToRecipe[supply]:
                        suppliesNeeded = remaining[recipeIdx]
                        suppliesNeeded.remove(supply)
                        if len(suppliesNeeded) == 0:
                            canCreate.append(recipes[recipeIdx])
                            newSupplies.append(recipes[recipeIdx])
            supplies = newSupplies

        return canCreate
