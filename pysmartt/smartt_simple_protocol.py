
# Escapes a string value according to the protocol
def escape(value):
    if not hasattr(escape, "encoded_characters"):
        escape.encoded_characters = [';', '$', '\\']
        escape.encoded_characters += [chr(i) for i in range(0,32)]

    encoded = ''
    for x in xrange(0, len(value)):
        c = value[x]
        if c in escape.encoded_characters:
            encoded += '\\x'+'{:02x}'.format(ord(c))
        else:
            encoded += c

    return encoded


# Unescapes a string value according to the protocol
def unescape(value):
    decoded = ''
    hex_escape_count = 0
    for x in xrange(0, len(value)):
        c = value[x]
        if hex_escape_count == 0:
            if c == '\\' and (x+3 < len(value)) and value[x+1] == 'x':
                hex_escape_count = 3
                decoded += chr(int(value[x+2:x+4], 16))
            else:
                decoded += c
        else:
            hex_escape_count -= 1

    return decoded



##############################################################################
### SmarttSimpleProtocol - handles the Smartt simplest protocol, using any
### source and destination for writing and receiving the data
class SmarttSimpleProtocol(object):
    # Protocol specific characters
    SEPARATOR_CHAR = b";"
    END_OF_MESSAGE_CHAR = b"$"
    # Encoding of string data sent by the server
    SERVER_ENCODING = "utf-8"
    # Encoding used by this client
    CLIENT_ENCODING = "utf-8"
    # Maximum number of characters read on each call of the read function
    MAXIMUM_READ_SIZE = 4096

    ### Init function - just stores the read and write functions and inits
    ### the data receiving buffer
    def __init__(self, read_function, write_function,
                 print_raw_messages=False):
        self.read_function = read_function
        self.write_function = write_function
        self.data_buffer = b""
        self.print_raw_messages = print_raw_messages

    ### Sending function - sends a message according to the protocol; just
    ### concatenates the escaped strings using the ';' character as a
    ### separator and '$' as the end of message character
    def send(self, message):
        # Escape all tokens
        escaped_message = [escape(token).encode(self.SERVER_ENCODING)
                           for token in message]

        # Join tokens and append end of message character
        formatted_message = (self.SEPARATOR_CHAR.join(escaped_message)
                             + self.END_OF_MESSAGE_CHAR)

        if self.print_raw_messages:
            print(formatted_message)

        self.write_function(formatted_message)

    ### Receiving function - receives data until finding the termination
    ### character, then extracts the message received up until this character
    ### from the buffer, and parses it; just removes the end of message
    ### character, splits the string at the ';' characters and unescapes the
    ### resulting strings; this implementation only supports a escaping scheme
    ### where the end of message and token separator characters aren't present
    ### anywhere in a escaped token string
    def receive(self):
        # Reads data until the end of message character ('$') is found
        terminator_index = self.data_buffer.find(self.END_OF_MESSAGE_CHAR)
        while terminator_index == -1:
            _tmp_buffer = self.read_function(self.MAXIMUM_READ_SIZE)

            if len(_tmp_buffer) == 0:
                raise Exception('Smartt Protocol error: could not read any '+\
                                'bytes')

            self.data_buffer += _tmp_buffer
            terminator_index = self.data_buffer.find(self.END_OF_MESSAGE_CHAR)

        # Extracts the message from the buffer
        data = self.data_buffer[:terminator_index]
        # Truncates the buffer
        self.data_buffer = self.data_buffer[terminator_index + 1:]

        # Handle data encoding
        data = unicode(data.decode(self.SERVER_ENCODING))

        if self.print_raw_messages:
            print(data + "$")

        if len(data) == 0:
            return []

        # Split message, unescape tokens and return
        return [unescape(token)
                for token in data.split(
                    self.SEPARATOR_CHAR.decode("utf8"))]

##############################################################################
