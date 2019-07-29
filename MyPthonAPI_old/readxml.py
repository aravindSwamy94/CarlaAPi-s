import xml.etree.ElementTree as ET
import math
def getPlanView(roadid):
    lat=49.000000
    lon=8.000000
    tree = ET.parse('Town01.xml')
    root = tree.getroot()
    latlon = root.find('header').find('geoReference').text
    for child in root.iter('road'):
        if(int(child.attrib['id'])==roadid):
            distX=float(child.find('planView').find('geometry').attrib['x'])
            distY=float(child.find('planView').find('geometry').attrib['y'])
            dist= math.sqrt((distX*distX)+ (distY*distY))            
            break

def main():
    getPlanView(2)
        
   
if __name__ == '__main__':
    main()
