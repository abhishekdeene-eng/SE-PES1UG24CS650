
from laundry_service import (
    extra_weight_charge,
    order_acceptable,
    dropoff_status
)


# ==========================================
# EXTRA WEIGHT CHARGE TESTS
# ==========================================

# 1. Invalid garment type
def test_invalid_garment():
    try:
        extra_weight_charge("shoes", 5, "standard", False)
        assert False
    except ValueError:
        assert True


# 2. Valid garment type
def test_valid_garment():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


# 3. Negative weight
def test_negative_weight():
    try:
        extra_weight_charge("regular", -1, "standard", False)
        assert False
    except ValueError:
        assert True


# 4. Zero weight
def test_zero_weight():
    assert extra_weight_charge("regular", 0, "standard", False) == 0


# 5. Member with regular clothes
def test_member_regular():
    assert extra_weight_charge("regular", 8, "standard", True) == 30


# 6. Non-member with regular clothes
def test_non_member_regular():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


# 7. Member with bedding (special exception)
def test_member_bedding():
    assert extra_weight_charge("bedding", 9, "standard", True) == 30


# 8. No extra weight
def test_no_extra_weight():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


# 9. Standard service
def test_standard_service():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


# 10. Express service
def test_express_service():
    assert extra_weight_charge("regular", 7, "express", False) == 100


# 11. More than 10 kg extra with standard service
def test_large_extra_standard():
    assert extra_weight_charge("regular", 16, "standard", False) == 495


# 12. More than 10 kg extra with express service
def test_large_extra_express():
    assert extra_weight_charge("regular", 16, "express", False) == 825


# ==========================================
# ORDER ACCEPTABILITY TESTS
# ==========================================

# 13. Delicate order accepted
def test_delicate_accepted():
    assert order_acceptable(10, 5, True) is True


# 14. Delicate order rejected
def test_delicate_rejected():
    assert order_acceptable(10, 6, True) is False


# 15. Heavy non-delicate order rejected
def test_heavy_order():
    assert order_acceptable(26, 20, False) is False


# 16. Normal order accepted
def test_normal_order():
    assert order_acceptable(20, 30, False) is True


# 17. Too many items
def test_too_many_items():
    assert order_acceptable(20, 41, False) is False


# 18. Exactly 25 kg
def test_exactly_25kg():
    assert order_acceptable(25, 40, False) is True


# ==========================================
# DROPOFF STATUS TESTS
# ==========================================

# 19. Normal order accepted
def test_normal_accepted():
    assert dropoff_status(60, False, False) == "accepted"


# 20. Normal order late
def test_normal_late():
    assert dropoff_status(50, False, False) == "late"


# 21. Normal order rejected
def test_normal_rejected():
    assert dropoff_status(39, False, False) == "rejected"


# 22. Bedding order accepted
def test_bedding_accepted():
    assert dropoff_status(90, True, False) == "accepted"


# 23. Bedding order late
def test_bedding_late():
    assert dropoff_status(80, True, False) == "late"


# 24. Bedding order rejected
def test_bedding_rejected():
    assert dropoff_status(69, True, False) == "rejected"


# 25. Express order accepted
def test_express_accepted():
    assert dropoff_status(90, False, True) == "accepted"


# 26. Express order late
def test_express_late():
    assert dropoff_status(80, False, True) == "late"


# 27. Express order rejected
def test_express_rejected():
    assert dropoff_status(69, False, True) == "rejected"


# 28. Bedding express order accepted
def test_bedding_express_accepted():
    assert dropoff_status(120, True, True) == "accepted"


# 29. Bedding express order late
def test_bedding_express_late():
    assert dropoff_status(110, True, True) == "late"


# 30. Bedding express order rejected
def test_bedding_express_rejected():
    assert dropoff_status(99, True, True) == "rejected"
