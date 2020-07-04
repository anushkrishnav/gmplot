from gmplot.drawables.symbols.circle import _Circle
from gmplot.drawables.symbols.plus import _Plus
from gmplot.drawables.symbols.x import _X

class _Symbol(object):
    _SHAPES = {
        'o': _Circle,
        '+': _Plus,
        'x': _X
    }

    @staticmethod
    def is_valid(shape):
        '''
        Return whether or not a shape is valid.

        Args:
            shape (str): Shape of a symbol.
        
        Returns:
            bool: True if the shape is valid, False otherwise.
        '''
        return shape in _Symbol._SHAPES

    def __init__(self, shape, lat, lng, size, precision, **kwargs):
        '''
        Args:
            shape (str): Shape of the symbol, as 'o', 'x', or '+'.
            lat (float): Latitude of the center of the symbol.
            lng (float): Longitude of the center of the symbol.
            size (int): Size of the symbol, in meters.
            precision (int): Number of digits after the decimal to round to for lat/lng values.

        Optional:

        Args:
            edge_color (str): Color of the symbol's edge.
            edge_alpha (float): Opacity of the symbol's edge, ranging from 0 to 1.
            edge_width (int): Width of the symbol's edge, in pixels.
            face_color (str): Color of the symbol's face.
            face_alpha (float): Opacity of the symbol's face, ranging from 0 to 1.
        '''
        # Copy parameters for symbols without a face:
        kwargs['color'] = kwargs.get('edge_color')
        kwargs['alpha'] = kwargs.get('edge_alpha')
        kwargs['width'] = kwargs.get('edge_width')

        self._symbol = self._SHAPES[shape](lat, lng, size, precision, **kwargs)

    def write(self, w):
        '''
        Write the symbol.

        Args:
            w (_Writer): Writer used to write the symbol.
        '''
        self._symbol.write(w)
