from Get_Data import items

username = 'standard_user'
password = 'secret_sauce'
buyer_name = 'axel'
buyer_last_name = 'kim'
zip_code = '00010'

def convert(item):
    words = item.split(" ")
    title = [word.lower() for word in words]
    join = "-".join(title)
    return join

xpath_items = [convert(item) for item in items]
print(xpath_items)