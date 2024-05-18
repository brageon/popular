def read_items(filename):
    with open(filename) as fh:
        return {line.strip() for line in fh}
def diff_string(old, new):
    return "\n".join(
        ['[-] %s' % gone for gone in old - new] +
        ['[+] %s' % added for added in new - old])
with open('rob.txt', 'w') as fh:
    fh.write(diff_string(read_items('bob.txt'), read_items('yok.txt')))