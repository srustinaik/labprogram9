def product_details(id,name,quantity,price):
    result=(
           f"product ID:{id}\n"
           f"product Name:{name}\n"
           f"product Quantity:{quantity}\n"
           f"product Price:{price}\n"
           )
    return result
if __name__=="__main__":
    id="L1001"
    name="Laptop"
    quantity=2
    price=75000
    print(product_details(id,name,quantity,price))
  
