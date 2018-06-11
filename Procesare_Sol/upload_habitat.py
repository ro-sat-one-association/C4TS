import time, struct, json, socket, httplib, crcmod, urllib, urllib2
from base64 import b64encode
from hashlib import sha256
from datetime import datetime
from aprs_to_habitat import parseData

def crc16_ccitt(data):
    """
    Calculate the CRC16 CCITT checksum of *data*.
    (CRC16 CCITT: start 0xFFFF, poly 0x1021)
    Returns an upper case, zero-filled hex string with no prefix such as
    ``0A1B``.
    >>> crc16_ccitt("hello,world")
    'E408'
    """
    crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
    return hex(crc16(data))[2:].upper().zfill(4)

def habitat_upload_payload_telemetry(payload_callsign = "C4TS", callsign="C4TS"):
    #$$habitat,123,13:16:24,51.123,0.123,11000*ABCD1

    #$$TST,46.9449,26.3595,312
    
    data = parseData() #ia de pe aprs
    
    ayy = "C4TS,"
    for i in range(0,11):
        ayy = ayy + str(data[i]) + ","
    
    ayy = ayy + str(data[11])
        
    sentence = "$$" + ayy + "*" + crc16_ccitt(ayy) + "\n"
    sentence_b64 = b64encode(sentence)

    date = datetime.utcnow().isoformat("T") + "Z"

    data = {
        "type": "payload_telemetry",
        "data": {
            "_raw": sentence_b64
            },
        "receivers": {
            callsign: {
                "time_created": date,
                "time_uploaded": date,
                },
            },
    }
    try:
        c = httplib.HTTPConnection("habitat.habhub.org",timeout=4)
        c.request(
            "PUT",
            "/habitat/_design/payload_telemetry/_update/add_listener/%s" % sha256(sentence_b64).hexdigest(),
            json.dumps(data),  # BODY
            {"Content-Type": "application/json"}  # HEADERS
            )

        response = c.getresponse()
        return (True,"OK")
    except Exception as e:
        return (False,"Failed to upload to Habitat: %s" % (str(e)))
        
print habitat_upload_payload_telemetry()