"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class gps_message(object):
    __slots__ = ["timestamp", "gpstime", "latitude", "longitude", "altitude", "easting", "northing"]

    def __init__(self):
        self.timestamp = 0
        self.gpstime = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.easting = 0.0
        self.northing = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(gps_message._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qqddddd", self.timestamp, self.gpstime, self.latitude, self.longitude, self.altitude, self.easting, self.northing))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != gps_message._get_packed_fingerprint():
            raise ValueError("Decode error")
        return gps_message._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = gps_message()
        self.timestamp, self.gpstime, self.latitude, self.longitude, self.altitude, self.easting, self.northing = struct.unpack(">qqddddd", buf.read(56))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if gps_message in parents: return 0
        tmphash = (0x8f576b6a1c4415a0) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if gps_message._packed_fingerprint is None:
            gps_message._packed_fingerprint = struct.pack(">Q", gps_message._get_hash_recursive([]))
        return gps_message._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
