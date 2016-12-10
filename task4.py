def readfile(cl='CustomerList.txt'):
    if cl:
        try:
            here = open(cl, 'r')
        except IOError:
            print "Error opening file"
            return None
        else:
            cc = []
            data = here.readlines()
            for customer in data:
                c = customer.split('\n')[0]
                c = c.split(',')
                cc.append(c)
            here.close()
            return cc


def append_customer(new_customer, filename='CustomerList.txt'):
    if filename:
        try:
            fp = open(filename, 'a')
        except IOError:
            print "Error opening file"
        else:
            line = ",".join(new_customer)
            line += '\n'
            fp.write(line)
            fp.close()
            return readfile(filename)


def match_customer(input_id, cc):
    for customer in cc:
        if customer[0] == input_id:
            return customer

    return None


def print_no(num):
    print "(%s) %s-%s" % (num[:3], num[3:6], num[6:])


def print_customer_detail(customer):
    print
    print customer[0], customer[2] + ",", customer[1]
    print customer[3]
    print customer[4] + ',', customer[5], customer[6]
    print_no(customer[7])
    print


def get_input(prompt):
    ipt = ''
    while not ipt:
        ipt = raw_input(prompt)

    return ipt.title()


def get_number(prompt):
    th = ''

    while len(th) != 10:
        try:
            th = raw_input(prompt)
            if len(th) != 10:
                raise ValueError
            temp = int(th)
        except ValueError:
            print "Not a valid number"
            th = ''

    return th


def generate_id(last_customer, phone):
    last_id = last_customer[0]
    s = int(last_id[:2])
    s = s+1
    ph = phone[-4:]
    uid = str(s) + str(ph)
    return uid


def rc():
    input_id = raw_input("Enter ID number: ")
    customer = match_customer(input_id, cc)

    if customer:
        print_customer_detail(customer)
        confirmation = raw_input("Confirm (Y/N): ")
        if confirmation == 'Y' or confirmation == 'y':
            return customer
    print 'Customer ID not found'
    return []


def nc():
    global cc
    print "\nWelcome, new Customer!"
    print "Please enter all data: "

    fname = get_input("First Name: ")
    lname = get_input("Last Name: ")
    street = get_input("Street Address: ")
    city = get_input("City: ")
    state = get_input("State: ").title()
    zipcode = get_input("Zipcode: ")
    phone = get_number("Phone: ")
    uid = generate_id(cc[-1], phone)

    print "The Account has been successfully created, the new User ID number is: " + uid
    new_customer = [uid, fname, lname, street, city, state, zipcode, phone]
    cc = append_customer(new_customer, 'CustomerList.txt')

    print "New customer added:"
    print_customer_detail(new_customer)
    return new_customer


def guestlist():
    print "Welcome and please enjoy, Guest User"
    print "Enjoy our complimentary features available to you \n"


def main():

    selection = 0
    while selection >= 0:
        print "---------------------------------"
        print "1) Returning Customer"
        print "2) New Customer"
        print "3) Guest"
        print "---------------------------------\n"

        selection = int(raw_input("Please select your customer type: "))

        if selection == 1:
            customer = rc()
            selection = -1
        elif selection == 2:
            customer = nc()
            selection = -1
        elif selection == 3:
            guestlist()
            selection = -1
        else:
            print "\nPlease enter your customer type from a value 1-3:"
            selection = 0


if __name__ == '__main__':
    cc = readfile('CustomerList.txt')
    main()
