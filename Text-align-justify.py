# 4 kyu Text align justify
# https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python

def justify(text, width):
    if not text.count(' '):
        return text
    words = text.split()
    o = []
    while words:
        line = []
        count = 0
        while len(' '.join(line)) < width and words:
            line.append(words.pop(0))
        if len(' '.join(line)) > width:
            words.insert(0, line.pop())
            o.append(compose_line(line, width))
        elif len(' '.join(line)) <= width:
            if words:
                o.append(compose_line(line, width))
            else:
                o.append(' '.join(line))

    return '\n'.join(o)


def compose_line(line: list, width: int):
    if len(line) == 1:
        return line[0]
    width_net = sum(len(word) for word in line)
    spaces_count = len(line) - 1
    gap_len = width - width_net
    spaces = [' '*(gap_len // spaces_count)] * spaces_count
    for i in range(gap_len % spaces_count):
        spaces[i] += ' '
    spaces.append('')
    return ''.join(word + space for word, space in zip(line, spaces))


if __name__ == '__main__':
    #l = ['Lorem',  'ipsum',  'dolor',  'sit', 'amet,']
    #print(compose_line(l, 30))
    # print(justify('123 45 6', 7), '123  45\n6')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
    print(justify(text, 15))