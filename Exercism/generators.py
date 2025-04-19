"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """

    _letters = ["A", "B", "C", "D"]
    for idx in range(number):
        yield _letters[idx % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = generate_seat_letters(number)
    row = 1
    seat_number = 0

    while seat_number < number:
        if row == 13:
            row += 1

        yield f"{row}{next(letters)}"
        seat_number += 1

        if seat_number % 4 == 0:
            row += 1




def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    return {name: next(seats) for name in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f"{seat+flight_id:0<12}"


assert list(generate_seat_letters(6)) == ["A", "B", "C", "D", "A", "B"]
assert list(generate_seats(10)) == ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B']

passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
assert assign_seats(passengers) == {'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}

seat_numbers = ['1A', '17D']
flight_id = 'CO1234'
assert list(generate_codes(seat_numbers, flight_id)) == ['1ACO12340000', '17DCO1234000']

