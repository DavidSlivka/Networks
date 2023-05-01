from IP import *


def check_if_IPv6_in_the_same_network(ip1: IPv6, ip2: IPv6):
    ip1.set_expanded_address()
    ip1.has_cidr_notation()
    ip1.set_binary()
    ip2.set_expanded_address()
    ip2.has_cidr_notation()
    ip2.set_binary()
    mask = ''
    if ip1.cidr_notation and ip2.cidr_notation:
        if ip1.subnet == ip2.subnet:
            mask = '1' * ip1.subnet + '0' * (128 - ip1.subnet)
        else:
            print('2 different subnets')
            return False
    elif ip1.cidr_notation or ip2.cidr_notation:  # check if only one IP has CIDR notation
        print('Only one IPv6 address was given with CIDR notation')
        return False
    else:
        print('IPv6 addresses have to have CIDR notation to check if they are in the same network')
        return False

    ip_1 = ''.join(ip1.binary_repr.split(':'))
    ip_2 = ''.join(ip2.binary_repr.split(':'))

    for i in range(len(ip_1)):
        if ip_1[i] != ip_2[i]:
            if mask[i] == '1':
                return False
    return True


IPv6_2 = IPv6('2001:db8:85a3::0023:0:9ac:12f/64')
IPv6_3 = IPv6('1:1:1:1:1:1:1:1/64')
print(check_if_IPv6_in_the_same_network(IPv6_2, IPv6_3))
