from unittest import TestCase
from cell import Cell


class TestCell(TestCase):
    def test_draw(self):
        self.fail()


class TestCell(TestCase):
    def test_set_future_state(self):
        # Set up your test
        # an active cell with 2 neighbors will have future_state = True
        active_cell =  Cell((0,0),(0,0), active = True)
        no_living_neighbors = 10
        for index in range (no_living_neighbors):
            active_cell.set_future_state(no_living_neighbors=index)
            if index == 2 or index == 3:
                self.assertTrue(active_cell.future_state,f' Should be set up to remain active with {index} neighbors.')
            elif not active_cell.active and no_living_neighbors == 3:
                self.assertTrue(active_cell.future_state, f' Should be set up to remain active with {index} neighbors.')
            else:
                self.assertFalse(active_cell.future_state,f' Should be set up to remain inactive with {index} neighbors.')
