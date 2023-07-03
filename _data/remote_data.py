

class RemoteData:

    input_bits = [False, False, False, False, False, False, False, False]
    output_bits = [False, False, False, False, False, False, False, False]

    __output_bits_old = [False, False, False, False, False, False, False, False]

    @property
    def input_data(self):
        data = 0x00
        mask = 0x01

        for bit in self.input_bits:
            if bit:
                data += mask
            mask *= 2

        return data

    @property
    def output_data(self):
        data = 0x00
        mask = 0x01

        for bit in self.output_bits:
            if bit:
                data += mask
            mask *= 2

        return data

    @output_data.setter
    def output_data(self, data):
        mask = 0x01

        for index in range(0, 8):
            if data & mask:
                self.output_bits[index] = True
            else:
                self.output_bits[index] = False
            mask *= 2

    def output_data_bit_is_change(self, bit_index):
        if self.output_bits[bit_index] != self.__output_bits_old[bit_index]:
            self.__output_bits_old[bit_index] = self.output_bits[bit_index]
            return True
        return False

