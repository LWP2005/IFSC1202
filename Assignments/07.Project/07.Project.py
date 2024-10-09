def parse_degree_string(ddmmss):
    """
    Parses a location value in the format DD°MM'SS" and returns degrees, minutes, and seconds as floats.
    """
    degree_symbol = chr(176)  # ° character
    minute_symbol = "'"
    second_symbol = '"'

    degrees = float(ddmmss.split(degree_symbol)[0].strip())
    minutes = float(ddmmss.split(degree_symbol)[1].split(minute_symbol)[0].strip())
    seconds = float(ddmmss.split(minute_symbol)[1].split(second_symbol)[0].strip())

    return degrees, minutes, seconds

def ddmmssto_decimal(degrees, minutes, seconds):
    """Converts degrees, minutes, and seconds to decimal degrees."""
    return degrees + (minutes / 60) + (seconds / 3600)

def convert_angles(input_file, output_file):
    """Reads angles from a file, converts them to decimal degrees, and writes the results to another file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line:
                decimal_degrees = ddmmssto_decimal(*parse_degree_string(line))
                outfile.write(f"{decimal_degrees:.6f}\n")

convert_angles('Assignments/07.Project/07.Project Angles Input.txt', 'Assignments/07.Project/07.Project Angles Output.txt')
