"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initializes the Class when called"""
        self.start = self.next = start
    
    def __repr__(self):
        """Provides a readable representation of the Class"""
        return f'SerialGenerator(start={self.start})'
    
    def generate(self):
        """Generates a new number that is 1 more than the previous start"""
        self.next += 1
        return self.next

    def reset(self):
        """Resets start number to originally entered number"""
        self.next = self.start
        return self.next
