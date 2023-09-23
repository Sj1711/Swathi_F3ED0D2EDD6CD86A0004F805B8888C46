def linear_search_product(productlist, targetproduct):
  indices = []
  for i, product in  enumerate(productlist):
    if product == targetproduct:
      indices.append(i)
  return indices


#example usage :

products = ["pen", "pencil", "eraser", "pen", "pencil", "pen"]
target = input("ENTER THE TARGET: ")
result = linear_search_product(products, target)
print(result)