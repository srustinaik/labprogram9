from product import product_details
def test_product_details():    
    expected_output=(
         "product id=L1001\n"
         "product name=Laptop\n"
         "quantity=2\n"
         "price=75000\n"
    )
  assert product_details("L1001","Laptop",2,75000) == expected_output
  
