"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    new_train = []
    locomotive = each_wagons_id[each_wagons_id.index(1)]
    last_wagons = each_wagons_id[:locomotive+1]
    middle_wagons = each_wagons_id[locomotive+2:]
    new_train.append(locomotive)
    new_train.extend(missing_wagons)
    new_train.extend(middle_wagons)
    new_train.extend(last_wagons)
    return new_train


def add_missing_stops(route: dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops" : list(kwargs.values())}


def extend_route_information(route: dict, more_route_information: dict):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple]]):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return list(map(list, zip(*wagons_rows)))
