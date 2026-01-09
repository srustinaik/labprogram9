from product import product_details

def test_product_details():
    expected_output = (
        "product ID:L1001\n"
        "product Name:Laptop\n"
        "product Quantity:2\n"
        "product Price:75000"
    )

    assert product_details("L1001", "Laptop", 2, 75000) == expected_output
