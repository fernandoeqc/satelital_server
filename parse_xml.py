from xml.dom import minidom

# parse an xml file by name




# one specific item attribute
# print('Item #2 attribute:')
# print(items[1].attributes['name'].value)

# all item attributes
# print('\nAll attributes:')
# for elem in items:
#   print(elem)

# one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)

# all items data


def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


def look_for_esn(file):
    mydoc = minidom.parse(file)
    items = mydoc.getElementsByTagName('esn')

    print('\nAll item data:')
    for elem in items:
        print('found', elem.firstChild.data, ': ', end='')
        if check_if_string_in_file('lista_sat.txt', elem.firstChild.data):
            with open('sat_pass.txt', 'a') as apd:
                apd.write(elem.firstChild.data)
                apd.write('\n')

            print('ok')
        else:
            print('not found in list')
