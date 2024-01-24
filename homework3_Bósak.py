products_list = input('Enter the products list: ').split()

while len(products_list) != 0:
    products_upd = input('Add or delete(-) the product: ')

    if not products_upd or products_upd.isspace():
        print("Products names can't be the whitespace or empty")
    else:
        if products_upd.isdigit():
            print("The products can't be numbers")
        elif products_upd.startswith('-') and products_upd[1:] in products_list:
            products_list.remove(products_upd[1:])
            print('Product removed. Updated list: ', products_list)

        else:
            products_list.append(products_upd)
            print('Product added. Updated list: ', products_list)

print("List is empty. Program finished.")