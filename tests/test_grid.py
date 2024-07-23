from unittest import TestCase
from grid import Grid


class TestGrid(TestCase):
    def test_update_grid(self):
        # set up a simple 3 by 3 grid
        test_grid = Grid(screen_dimensions=(10, 10), width=3, height=3)
        # creates an empty grid that is 3 by 3
        # |_|_|_|
        # |_|_|_|
        # |_|_|_|
        for row in range(test_grid.width):
            for col in range(test_grid.height):
                test_grid.flip(col, row)
        # this flips the cell at column 2, row 1, so the grid would look like:
        # |_|_|_|
        # |_|_|X|
        # |_|_|_|

                # You can get a specific cell from the grid by using the get_cell method
                self.assertTrue(test_grid.get_cell(col, row).active, f' The cell ({col}, {row}) should be active.')

        # You should test a few scenarios of the update method here.
        # recall that the idea of the update method is to:
        # first compute all the future states using __compute_future_states
        # then call update on each cell.
        # at a minimum, you should check that the scenario we tested in 04_04 is working correctly now


