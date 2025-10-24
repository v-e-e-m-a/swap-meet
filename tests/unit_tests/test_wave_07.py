import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from tests import *

#@pytest.mark.skip
def test_swap_items_by_newest():
    # Arrange
    # me
    item_a = Decor(age=7)
    item_b = Electronics(age=1)
    item_c = Clothing(age=3)
    olga = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    # them
    item_d = Decor(age=5)
    item_e = Electronics(age=8)
    item_f = Clothing(age=1)
    jack = Vendor(inventory=[item_d, item_e, item_f])

    # Act
    result = olga.swap_by_newest(jack)

    # Assert
    assert result is True
    assert len(olga.inventory) == 3
    assert len(jack.inventory) == 3
    assert item_f in olga.inventory
    assert item_b in jack.inventory
    assert olga.inventory == [item_a, item_c, item_f]
    assert jack.inventory == [item_d, item_e, item_b]