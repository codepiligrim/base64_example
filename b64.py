#python 2.7
import base64, sys, os

class AnyFileBase64(object):
    
    def Encode(self, file):
    
        HOME_DIR = os.path.dirname(os.path.abspath(__file__))
        INPUT_DIR = HOME_DIR + '\\' + 'src' + '\\'
        FILE = open(INPUT_DIR + file, 'rb')
        ENCODED = base64.b64encode(FILE.read())
        OUTPUT_DIR = HOME_DIR + '\\' + 'encoded' + '\\'
        FILE_OUT = open(OUTPUT_DIR + sys.argv[2] + '.b64', 'w')
        FILE_OUT.writelines(ENCODED)
        FILE_OUT.close()
    
    def Decode(self, file):
    
        #read b64 file
        HOME_DIR = os.path.dirname(os.path.abspath(__file__))
        INPUT_DIR = HOME_DIR + '\\' + 'src_b64' + '\\'
        FILE = open(INPUT_DIR + file, 'r')
        FILE_READ = FILE.read()
        DECODED = base64.b64decode(FILE_READ)
        FILE.close()
        
        #set output file and write decoded data
        OUTPUT_DIR = HOME_DIR + '\\' + 'decoded' + '\\'
        FILE_OUT = open(OUTPUT_DIR + file.replace('b64',''), 'wb')
        FILE_OUT.writelines(DECODED)
        FILE_OUT.close() 

if sys.argv[1]=='encode':
    AnyFileBase64().Encode(sys.argv[2])
if sys.argv[1]=='decode':
    AnyFileBase64().Decode(sys.argv[2])
    
    
    
# image_decode = base64.decodestring(image_encode)
# with open('deer_decode.gif','wb') as dimage:
# dimage.write(image_decode)