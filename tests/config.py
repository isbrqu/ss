from collections import namedtuple
from os import getenv as env

DRIVE = {
    'id1': env('DRIVE_ID1'),
    'id2': env('DRIVE_ID2'),
    'id3': env('DRIVE_ID3'),
    'id3': env('DRIVE_ID3'),
    'pedidos': env('DRIVE_PEDIDOS'),
    'url': env('DRIVE_URL'),
}

drive = namedtuple('Drive', DRIVE.keys())(**DRIVE)

