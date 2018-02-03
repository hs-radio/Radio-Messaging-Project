msg = 'hello friend?'

def b2a(bin_msg):
    return bin(ord(bin_msg))[2:]    

b2a(msg) 
