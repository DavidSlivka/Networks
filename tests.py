import unittest
import IP


class TestIPAddress(unittest.TestCase):
    def setUp(self):
        self.IPv4_1 = IP.IPv4('37.11.222.6/10')
        self.IPv4_2 = IP.IPv4('')
        self.IPv4_3 = IP.IPv4('192:11.222.6/24')
        self.IPv4_4 = IP.IPv4('192.168./.612/12')
        self.IPv4_5 = IP.IPv4('./33')
        self.IPv6_1 = IP.IPv6('abcd::')
        self.IPv6_2 = IP.IPv6('2001:db8:85a3::0370:7344/64')
        self.IPv6_3 = IP.IPv6('2001:db8:85a3::23:0:9ac:12f/134')
        self.IPv6_4 = IP.IPv6('1:1:1:1:1:1:1:0/80')
        self.IPv6_5 = IP.IPv6('::f/5')

    def test_ip_format(self):
        self.assertEqual(self.IPv4_1.ip_format, 'IPv4')
        self.assertEqual(self.IPv4_2.ip_format, '')
        self.assertEqual(self.IPv4_3.ip_format, 'IPv4')
        self.assertEqual(self.IPv4_4.ip_format, 'IPv4')
        self.assertEqual(self.IPv4_5.ip_format, 'IPv4')
        self.assertEqual(self.IPv6_1.ip_format, 'IPv6')
        self.assertEqual(self.IPv6_2.ip_format, 'IPv6')
        self.assertEqual(self.IPv6_3.ip_format, 'IPv6')
        self.assertEqual(self.IPv6_4.ip_format, 'IPv6')
        self.assertEqual(self.IPv6_5.ip_format, 'IPv6')


class TestIPv4(unittest.TestCase):
    def setUp(self):
        self.IPv4_1 = IP.IPv4('37.11.222.6/10')
        self.IPv4_2 = IP.IPv4('')
        self.IPv4_3 = IP.IPv4('192:11.222.6/24')
        self.IPv4_4 = IP.IPv4('192.168./.612/12')
        self.IPv4_5 = IP.IPv4('./33')

    def test_check_format(self):
        self.assertEqual(self.IPv4_1.check_format(), True)
        self.assertEqual(self.IPv4_2.check_format(), False)
        self.assertEqual(self.IPv4_3.check_format(), False)
        self.assertEqual(self.IPv4_4.check_format(), False)
        self.assertEqual(self.IPv4_5.check_format(), False)

    def test_check_values(self):
        self.assertEqual(self.IPv4_1.check_values(), True)
        self.assertEqual(self.IPv4_2.check_values(), False)
        self.assertEqual(self.IPv4_3.check_values(), False)
        self.assertEqual(self.IPv4_4.check_values(), False)
        self.assertEqual(self.IPv4_5.check_values(), False)

    def test_has_cidr_notation(self):
        self.assertEqual(self.IPv4_1.has_cidr_notation(), True)
        self.assertEqual(self.IPv4_1.subnet, 10)
        self.assertEqual(self.IPv4_2.has_cidr_notation(), False)
        self.assertEqual(self.IPv4_3.has_cidr_notation(), True)
        self.assertEqual(self.IPv4_3.subnet, 24)
        self.assertEqual(self.IPv4_4.has_cidr_notation(), False)
        self.assertEqual(self.IPv4_5.has_cidr_notation(), False)

    def test_binary_format(self):
        self.assertEqual(self.IPv4_1.get_binary_format(), '00100101.00001011.11011110.00000110')
        self.assertEqual(self.IPv4_2.get_binary_format(), '')
        self.assertEqual(self.IPv4_3.get_binary_format(), '')
        self.assertEqual(self.IPv4_4.get_binary_format(), '')
        self.assertEqual(self.IPv4_5.get_binary_format(), '')


class TestIPv6(unittest.TestCase):
    def setUp(self):
        self.IPv6_1 = IP.IPv6('abcd::')
        self.IPv6_2 = IP.IPv6('200g:db8:8qwa3::0370:7344/64')
        self.IPv6_3 = IP.IPv6('2001:db8:85a3::23:0:9ac:12f/134')
        self.IPv6_4 = IP.IPv6('1:1:1:1:1:1:1:0000/80')
        self.IPv6_5 = IP.IPv6('::f::/5')

    def test_check_format(self):
        self.assertEqual(self.IPv6_1.check_format(), True)
        self.assertEqual(self.IPv6_2.check_format(), False)
        self.assertEqual(self.IPv6_3.check_format(), True)
        self.assertEqual(self.IPv6_4.check_format(), True)
        self.assertEqual(self.IPv6_5.check_format(), True)

    def test_set_expanded_values(self):
        self.assertEqual(self.IPv6_1.set_expanded_values(), ['abcd', '0000', '0000', '0000', '0000', '0000', '0000', '0000'])
        self.assertEqual(self.IPv6_2.set_expanded_values(), [])
        self.assertEqual(self.IPv6_3.set_expanded_values(), ['2001', '0db8', '85a3', '0000', '0023', '0000', '09ac', '012f'])
        self.assertEqual(self.IPv6_4.set_expanded_values(), ['0001', '0001', '0001', '0001', '0001', '0001', '0001', '0000'])
        self.assertEqual(self.IPv6_5.set_expanded_values(), [])

    def test_set_expanded_address(self):
        self.assertEqual(self.IPv6_1.set_expanded_address(), 'abcd:0000:0000:0000:0000:0000:0000:0000')
        self.assertEqual(self.IPv6_2.set_expanded_address(), '')
        self.assertEqual(self.IPv6_3.set_expanded_address(), '2001:0db8:85a3:0000:0023:0000:09ac:012f')
        self.assertEqual(self.IPv6_4.set_expanded_address(), '0001:0001:0001:0001:0001:0001:0001:0000')
        self.assertEqual(self.IPv6_5.set_expanded_address(), '')

    def test_return_binary(self):
        self.assertEqual(self.IPv6_1.return_binary(), '1010101111001101:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000')
        self.assertEqual(self.IPv6_2.return_binary(), '')
        self.assertEqual(self.IPv6_3.return_binary(), '0010000000000001:0000110110111000:1000010110100011:0000000000000000:0000000000100011:0000000000000000:0000100110101100:0000000100101111')
        self.assertEqual(self.IPv6_4.return_binary(), '0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000000')
        self.assertEqual(self.IPv6_5.return_binary(), '')

    def test_set_binary(self):
        self.IPv6_1.set_binary()
        self.assertEqual(self.IPv6_1.binary_repr, '1010101111001101:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000')
        self.IPv6_2.set_binary()
        self.assertEqual(self.IPv6_2.binary_repr, '')
        self.IPv6_3.set_binary()
        self.assertEqual(self.IPv6_3.binary_repr, '0010000000000001:0000110110111000:1000010110100011:0000000000000000:0000000000100011:0000000000000000:0000100110101100:0000000100101111')
        self.IPv6_4.set_binary()
        self.assertEqual(self.IPv6_4.binary_repr, '0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000001:0000000000000000')
        self.IPv6_5.set_binary()
        self.assertEqual(self.IPv6_5.binary_repr, '')

    def test_has_cidr_notation(self):
        self.assertEqual(self.IPv6_1.has_cidr_notation(), False)
        self.assertEqual(self.IPv6_2.has_cidr_notation(), True)
        self.assertEqual(self.IPv6_3.has_cidr_notation(), False)
        self.assertEqual(self.IPv6_4.has_cidr_notation(), True)
        self.assertEqual(self.IPv6_5.has_cidr_notation(), True)


class TestMask(unittest.TestCase):
    def setUp(self):
        self.mask_1 = IP.Mask('255.255.224.0')
        self.mask_2 = IP.Mask('255.255.252.0')
        self.mask_3 = IP.Mask('255.255.255.1')
        self.mask_4 = IP.Mask('255.0.255.0')
        self.mask_5 = IP.Mask('255.300.255.0')

    def test_check_format(self):
        self.assertEqual(self.mask_1.check_format(), True)
        self.assertEqual(self.mask_2.check_format(), True)
        self.assertEqual(self.mask_3.check_format(), True)
        self.assertEqual(self.mask_4.check_format(), True)
        self.assertEqual(self.mask_5.check_format(), True)

    def test_check_values(self):
        self.assertEqual(self.mask_1.check_values(), True)
        self.assertEqual(self.mask_2.check_values(), True)
        self.assertEqual(self.mask_3.check_values(), True)
        self.assertEqual(self.mask_4.check_values(), True)
        self.assertEqual(self.mask_5.check_values(), False)

    def test_get_binary_format(self):
        self.assertEqual(self.mask_1.get_binary_format(), '11111111.11111111.11100000.00000000')
        self.assertEqual(self.mask_2.get_binary_format(), '11111111.11111111.11111100.00000000')
        self.assertEqual(self.mask_3.get_binary_format(), '11111111.11111111.11111111.00000001')
        self.assertEqual(self.mask_4.get_binary_format(), '11111111.00000000.11111111.00000000')
        self.assertEqual(self.mask_5.get_binary_format(), '')

    def test_check_valid_mask(self):
        self.assertEqual(self.mask_1.check_valid_mask(), True)
        self.assertEqual(self.mask_2.check_valid_mask(), True)
        self.assertEqual(self.mask_3.check_valid_mask(), False)
        self.assertEqual(self.mask_4.check_valid_mask(), False)
        self.assertEqual(self.mask_5.check_valid_mask(), False)
