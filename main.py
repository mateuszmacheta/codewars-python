from string import ascii_lowercase as l


def find_the_number_plate(customer_id):
    id = customer_id + 1
    s = len(l)
    return '{}{}{}{:03d}'.format(
        l[id // 1000 % s],
        l[id // (s * 1000) % s],
        l[id // (s * s * 1000) % s],
        id % 1000
    )


if __name__ == '__main__':
    # print(find_the_number_plate(3),'aaa004')
    print(find_the_number_plate(1000),'baa000')