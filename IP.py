class IPAddress:
    def __init__(self, ip: str):
        self.ip = ip
        self.ip_format = self.set_format()

    def set_format(self):
        if '.' in self.ip:
            return 'IPv4'
        elif ':' in self.ip:
            return 'IPv6'
        else:
            print(f'{self.ip} is an invalid IP address')
            # exit(1)
            return ''


class IPv4(IPAddress):
    def __init__(self, ip: str):
        super().__init__(ip)
        self.subnet = None
        self.cidr_notation = False
        self.values = []
        self.binary_repr = ''

    def check_format(self):
        if isinstance(self.ip, str):
            self.values = [i for i in self.ip.split('/')[0].split('.') if i != '']
            if len(self.values) == 4:
                if all(len(val) < 4 for val in self.values):
                    return True

        return False

    def check_values(self):
        if self.check_format():
            try:
                return all(int(val) < 256 for val in self.values)
            except ValueError:
                return False
        return False

    def get_binary_format(self):
        if self.check_values():
            binary_repr = ''
            for val in self.values:
                binary_repr += f'{int(val):08b}.'

            binary_repr = binary_repr[0:-1]

            return binary_repr
        else:
            print("Invalid IPv4 format")
            # exit(1)
            return ''

    def has_cidr_notation(self):
        if '/' in self.ip and self.ip.count('/') == 1:
            [ip, subnet] = self.ip.split('/')
            self.ip = ip
            try:
                self.subnet = int(subnet)
                self.cidr_notation = True
                if self.subnet > 31:
                    print('Invalid IPv4 address with CIDR notation')
                    # exit(1)
                    return False
                return True
            except ValueError:
                print("Invalid IPv4 address with CIDR notation")
                # exit(1)
                return False
        return False


class IPv6(IPAddress):
    def __init__(self, ip: str):
        super().__init__(ip)
        self.values = []
        self.cidr_notation = False
        self.subnet = None
        self.expanded_ip_address = self.set_expanded_address()
        self.binary_repr = ''

    def check_format(self):
        if isinstance(self.ip, str):
            values = self.ip.split('/')[0].split(':')
            for val in values:
                if len(val) < 5:
                    if val != '':
                        try:
                            int(val, 16)
                        except ValueError:
                            return False
                else:
                    return False

            return True
        return False

    def set_expanded_values(self):
        if '/' in self.ip:
            ip = self.ip.split('/')[0]
        else:
            ip = self.ip
        if self.check_format():
            new_values = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000']
            colons = ip.count(':')
            double_colons = ip.count('::')
            if double_colons > 1:
                return []

            if colons == 7:
                vals = [i for i in ip.split(':')]
                for i in range(len(vals)):
                    new_values[i] = f'{vals[i].zfill(4)}'

                return new_values

            if 1 < colons < 7:
                vals_before = [i for i in ip[0:ip.index('::')].split(':')]
                for i in range(len(vals_before)):
                    new_values[i] = f'{vals_before[i].zfill(4)}'

                values_to_fill = 8 - colons

                vals_after = [i for i in ip[ip.index('::') + 2:].split(':')]

                for i in range(len(vals_after)):
                    new_values[i + len(vals_before) + values_to_fill] = f'{vals_after[i].zfill(4)}'

                return new_values
            return []

        return []

    def set_expanded_address(self):
        if self.check_format() and self.set_format():
            self.values = self.set_expanded_values()
            return ':'.join(self.values)
        return ''

    def return_binary(self):
        if self.check_format() and self.set_format():
            binary_repr = ''
            for val in self.values:
                binary_repr += f'{int(val, 16) :016b}:'

            binary_repr = binary_repr[0:-1]

            return binary_repr
        return ''

    def set_binary(self):
        self.binary_repr = self.return_binary()

    def has_cidr_notation(self):
        if '/' in self.ip:
            [ip, subnet] = self.ip.split('/')
            self.ip = ip
            try:
                self.subnet = int(subnet)
                self.cidr_notation = True
                if self.subnet > 127:
                    print("Invalid IPv6 address with CIDR notation")
                    # exit(1)
                    return False
                return True
            except ValueError:
                print("Invalid IPv6 address with CIDR notation")
                # exit(1)
                return False
        return False
