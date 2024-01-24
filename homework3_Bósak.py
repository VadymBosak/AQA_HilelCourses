products_list = input('Enter the products list: ').split()

while len(products_list) != 0:
    products_upd = input('Add or delete(-) the product: ')

    if not products_upd or products_upd.isspace():
        print("Products names can't be the whitespace or empty")

    elif products_upd.startswith('-'):
        if products_upd[1:] in products_list:
            products_list.remove(products_upd[1:])
            print('Product removed. Updated list: ', products_list)
        else:
            print(f"Product '{products_upd}' not found in the list")

    else:
        products_list.append(products_upd)
        print('Product added. Updated list: ', products_list)

print("List is empty. Program finished.")