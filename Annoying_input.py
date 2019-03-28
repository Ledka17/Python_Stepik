def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        x = input()
        try:
            i = int(x)
            if i or i == 0:
                print(end_message)
                return (int(x))
        except:
            print(error_message)

x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')