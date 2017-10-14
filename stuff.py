def data_line(line):
    assert line.startswith('DATA_NAME')

    segment_info = line.split()
    NAME, BOUNDARY, IS_FLOAT = None, None, False

    for info in segment_info:
        if info == 'FLOAT':
            IS_FLOAT=True
        else:
            parts = info.split('=')
            if parts[0] == 'DATA_NAME':
                NAME = parts[1]
            elif parts[0] == 'POSITION':
                boundary_parts = parts[1].split(':')
                BOUNDARY = (number(boundary_parts[0]), intb(boundary_parts[1]))
            else:
                print('Unrecognized field in data segment declaration line:\n\t',line)

    return DataSegment(NAME, BOUNDARY, IS_FLOAT)

def message_lines(lines):
    message_type = MessageType(message_line(lines[0]))
    data_begin_indices = [i for i, line in enumerate(lines) if line.strip().startswith('DATA_NAME')]

    if len(data_begin_indices) != 0:
        for i, begin_index in enumerate(data_begin_indices[:-1]):
            data_segment = parse_data_lines(lines[begin_index:data_begin_indices[i+1]])
            message_type.add_data_segment(data_segment)

        data_segment = parse_data_lines(lines[data_begin_indices[-1]:])
        message_type.add_data_segment(data_segment)

    return message_type

def spec(sfile):
    sfile.seek(0)
    lines = (line.strip() for line in sfile if line[0] != '#' and line.strip() != '')
    message_begin_indices = [i for i, line in enumerate(lines) if line.startswith("MESSAGE_NAME")]

    message_types = {}

    for i, begin_index in enumerate(message_begin_indices[:-1]):
        message = message_lines(lines[begin_index:message_begin_indices[i+1]])
        message_types[message.can_id] = message

    message = message_lines(lines[message_begin_indices[-1]:])
    message_types[message.can_id] = message

    return message_types
