
import aprs

APRS = aprs.APRS( "noam.aprs2.net", 14580, "YO8PAS-10", "21422")

def callback(arg):
    print "AM PRIMIT" 
    print arg
    return


APRS.callsign_filter(["YO8PAS-10", "YO8PAS"])
APRS.connect()
APRS.consumer(callback, True)