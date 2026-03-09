# Minecraft Crafting Database

CRAFTING_RECIPES = {
    "wooden_pickaxe": {"requires": ["wood", "sticks"], "craftable": True},
    "stone_pickaxe": {"requires": ["stone", "sticks"], "craftable": True},
    "iron_pickaxe": {"requires": ["iron_ingot", "sticks"], "craftable": True},
    "diamond_pickaxe": {"requires": ["diamond", "sticks"], "craftable": True},
    "wooden_sword": {"requires": ["wood", "sticks"], "craftable": True},
    "stone_sword": {"requires": ["stone", "sticks"], "craftable": True},
    "iron_sword": {"requires": ["iron_ingot", "sticks"], "craftable": True},
    "diamond_sword": {"requires": ["diamond", "sticks"], "craftable": True},
    "wooden_axe": {"requires": ["wood", "sticks"], "craftable": True},
    "stone_axe": {"requires": ["stone", "sticks"], "craftable": True},
    "iron_axe": {"requires": ["iron_ingot", "sticks"], "craftable": True},
    "crafting_table": {"requires": ["wood"], "craftable": True},
    "furnace": {"requires": ["stone"], "craftable": True},
    "chest": {"requires": ["wood"], "craftable": True},
    "sticks": {"requires": ["wood"], "craftable": True},
    "planks": {"requires": ["wood"], "craftable": True},
}

def get_crafting_recipes():
    """Returns all available crafting recipes"""
    return CRAFTING_RECIPES

def get_suggested_builds(items):
    """
    Analyzes available items and suggests what can be crafted
    Args: items (list) - list of item names
    Returns: list of suggested builds
    """
    items_set = set(item.lower() for item in items)
    suggestions = []
    
    for recipe_name, recipe_data in CRAFTING_RECIPES.items():
        required = set(req.lower() for req in recipe_data['requires'])
        
        # Check if all required items are available
        if required.issubset(items_set):
            suggestions.append({
                "name": recipe_name,
                "requires": recipe_data['requires']
            })
    
    return suggestions
