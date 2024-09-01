calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = string.lower()
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armaggedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # No matches
print(is_contains('cycle', ['recycling', 'cyclic'])) # Urban ~ urBAN

print(calls)
