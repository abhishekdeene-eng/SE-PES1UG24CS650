
import pytest

from laundry_service import (
    extra_weight_charge,
    order_acceptable,
    dropoff_status
)


# Test 1: Unknown garment type
def test_invalid_garment_type():
    with pytest.raises(ValueError):
        extra_weight_charge("shoes", 5, "standard", False)


# Test 2: Negative weight
def test_negative_weight():
    with pytest.raises(ValueError):
        extra_weight_charge("regular", -2, "standard", False)


# Test 3: Member gets additional weight allowance
def test_member_extra_allowance():
    assert extra_weight_charge("regular", 8, "standard", True) == 30


# Test 4: Weight within included limit
def test_no_extra_charge():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


# Test 5: Standard service extra charge
def test_standard_extra_charge():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


# Test 6: Express service extra charge
def test_express_extra_charge():
    assert extra_weight_charge("regular", 7, "express", False) == 100


# Test 7: Extra weight greater than 10 kg
def test_large_extra_weight_express():
    assert extra_weight_charge("regular", 16, "express", False) == 825


# Test 8: Delicate order accepted
def test_delicate_order_accepted():
    assert order_acceptable(10, 5, True) is True


# Test 9: Delicate order rejected
def test_delicate_order_rejected():
    assert order_acceptable(10, 6, True) is False


# Test 10: Heavy order rejected
def test_heavy_order_rejected():
    assert order_acceptable(26, 20, False) is False


# Test 11: Normal order accepted
def test_normal_order_accepted():
    assert order_acceptable(20, 30, False) is True


# Test 12: Normal order rejected due to item count
def test_too_many_items():
    assert order_acceptable(20, 41, False) is False


# Test 13: Normal dropoff accepted
def test_dropoff_accepted():
    assert dropoff_status(60, False, False) == "accepted"


# Test 14: Bedding express dropoff accepted
def test_bedding_express_accepted():
    assert dropoff_status(120, True, True) == "accepted"


# Test 15: Late dropoff
def test_dropoff_late():
    assert dropoff_status(50, False, False) == "late"


# Test 16: Rejected dropoff
def test_dropoff_rejected():
    assert dropoff_status(30, False, False) == "rejected"
