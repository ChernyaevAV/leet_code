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
    a, b, *c = each_wagons_id
    idx = c.index(1)
    return c[:idx+1] + missing_wagons + c[idx+1:] + [a, b]

assert fix_list_of_wagons(
    [2, 5, 1, 7, 4, 12, 6, 3, 13],
    [3, 17, 6, 15]
) == [1, 3, 17, 6, 15, 7, 4,  12, 6, 3, 13, 2, 5]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route

assert add_missing_stops(
    {'from': 'Berlin', 'to': 'Hamburg'},
    stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
    stop_4="Jacksonville", stop_5="Orlando"
) == {'from': 'Berlin',
      'to': 'Hamburg',
      'stops': ['Washington, DC', 'Charlotte', 'Atlanta', 'Jacksonville', 'Orlando']}



def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


assert extend_route_information(
    {"from": "Berlin", "to": "Hamburg"},
    {"length": "100", "speed": "50"}
) == {"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(row) for row in zip(*wagons_rows)]


assert fix_wagon_depot([
    [(2, "red"), (4, "red"), (8, "red")],
    [(5, "blue"), (9, "blue"), (13,"blue")],
    [(3, "orange"), (7, "orange"), (11, "orange")],
]) == [
    [(2, "red"), (5, "blue"), (3, "orange")],
    [(4, "red"), (9, "blue"), (7, "orange")],
    [(8, "red"), (13,"blue"), (11, "orange")]
]