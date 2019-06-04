class Converter:
    def __init__(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F']

    def decimal_to_base(self, num, base=2):
        """
        Converts a decimal number to a number in the indicated number system.
        The default is base two. Assumes that the provided number is a valid
        positive integer in base 10 and the base is 1-16.

        :param num: the integer to be converted
        :param base: the number system to convert to

        :return: the converted number
        """
        new_val = []
        quot = num
        if num == 0:
            return '0'
        while quot > 0:
            remain = quot % base
            new_val += [self.convert_remain(remain)]
            quot = quot // base
        if base == 16:
            new_val += ['0x']
        new_val.reverse()
        return ''.join(new_val)

    @staticmethod
    def base_to_decimal(num, base):
        """
        Converts a number in any base to a number in base 10 (decimal). Assumes
        that the provided number is valid.

        :param num: the number to be converted
        :param base: the base of the provided number
        :return:
        """
        pass

    def convert_remain(self, remain):
        if remain > 9:
            index = remain - 10
            return self.letters[index]
        else:
            return str(remain)
