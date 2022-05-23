def ip_to_int32(ip):
    octets = ip.split('.')
    return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])


if __name__ == '__main__':
    print(ip_to_int32("128.114.17.104"))