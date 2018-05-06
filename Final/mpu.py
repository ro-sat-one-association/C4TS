def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size
    
def test():
    file  = open('/home/pi/MPU.txt', 'r')
    cfile = open('/home/pi/MPU_check.txt', 'r')
    check = cfile.read()
    cfile.close()
    
    if int(getSize(file)) != int(check):
        cfile = open('/home/pi/MPU_check.txt', 'w+')
        cfile.write(str(getSize(file)))
        cfile.close()
        file.close()
        return True
    else:
        file.close()
        return False