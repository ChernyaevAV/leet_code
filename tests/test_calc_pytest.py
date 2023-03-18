from calc_square_eq_solver import square_eq_solver


class TestCase:
    @staticmethod
    def test_calc_no_roots():
        res = square_eq_solver(10, 0, 2)
        assert len(res) == 0

    @staticmethod
    def test_single_root():
        res = square_eq_solver(10, 0, 0)
        assert len(res) == 1
        assert res == [0]

    @staticmethod
    def test_multiple_root():
        res = square_eq_solver(2, 5, -3)
        assert len(res) == 2
        assert res == [0.5, -3]


