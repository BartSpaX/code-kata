"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add: tuple):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item not in current_cart:
            current_cart[item] = 1
        else: current_cart[item] += 1
    return current_cart


def read_notes(notes: tuple):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates: dict):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates
    return ideas


def sort_entries(cart: dict):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    cart_sorted = dict(sorted(cart.items()))
    return cart_sorted


def send_to_store(cart: dict, aisle_mapping: dict):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for key, value in cart.items():
        cart[key] = [value] + aisle_mapping[key]
    return dict(sorted(cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key in fulfillment_cart.keys():
        store_inventory[key][0] -= fulfillment_cart[key][0]
        if store_inventory[key][0] <= 0:
            store_inventory[key][0] = "Out of Stock"
    return store_inventory