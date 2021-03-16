def hex_to_binary( hex_code ):
    bin_code = bin( hex_code )[2:]
    padding = (4-len(bin_code)%4)%4
    if (len('0'*padding + bin_code) < 32):
        padding = 32 - len('0'*padding + bin_code) + 1
        print (len('0'*padding + bin_code))
        if (len('0'*padding + bin_code) > 32):
            padding = 32 - len('0'*padding + bin_code)
            return '0'*padding + bin_code
        else:
            return '0'*padding + bin_code
    else:
        print(len('0'*padding + bin_code))
        return '0'*padding + bin_code


print (hex_to_binary(0xffe001ff))