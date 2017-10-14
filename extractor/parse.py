import re

SI_MOD = {
    '' : 1,
    'k' : 1e3,
    'm' : 1e6,
}

def frequency(freq_str):
    """
    Extract frequency of CAN Message from spec.
    """
    match = re.search('(\d\.*\d*)*([A-Za-z]*)', freq_str)
    unit = match.group(2)
    num = float(match.group(1))
    if unit.lower().endswith('hz'):
        return num * SI_MOD[unit.lower()[:-2]]
    else:
        raise ValueError('Unrecognized frequency unit {}.'.format(unit))

def number(num, reverse_endian=False):
    '''
    Parses a number. Reverses its endianess if `reverse_endian`.
    '''
    assert isinstance(num, (int, float, str))

    if isinstance(num, (int, float)):
        return num
    if reverse_endian:
        return int(bin(int(num, 0))[-1:1:-1], 2)

    return float(num) if '.' in num else int(num, 0)

def log(line):
    return {
        'time' : re.search('\(([0-9]+(.[0-9]+)?)\)', line).group(1),
        'can_id' : '0x' + re.search('([0-9]+)#', line).group(1),
        'data' : '0x' + re.search('#([0-9, A-F]+)', line).group(1),
    }
