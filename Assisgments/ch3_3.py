'''
Sharad:  Estimate geographical areas between cities
'''
import math
##corordinates for 4 cities 
atlx,atly=math.radians(33.7489954),math.radians(-84.3879824)
charx,chary=math.radians(35.2270869),math.radians(-80.84312669999997)
savx,savy=math.radians(32.0835407),math.radians(-81.09983419999998)
orldx,orldy=math.radians(28.5383355),math.radians(-81.379236499)

##constant earth radius
EARTHRADIUS=6371.01
##distance between atlanta and Charlotte, 
dist_atl_char = EARTHRADIUS * math.acos(math.sin(atlx) * math.sin(charx) + math.cos(atlx) * math.cos(charx) * math.cos(atly - chary)) 
##distance between Charlotte and savannah
dist_char_sav = EARTHRADIUS * math.acos(math.sin(charx) * math.sin(savx) + math.cos(charx) * math.cos(savx) * math.cos(chary - savy)) 
##distance between savannah and orlando
dist_sav_orld = EARTHRADIUS * math.acos(math.sin(savx) * math.sin(orldx) + math.cos(savx) * math.cos(orldx) * math.cos(savy - orldy)) 
##distance between orlando and atlanta
dist_orld_atl = EARTHRADIUS * math.acos(math.sin(orldx) * math.sin(atlx) + math.cos(orldx) * math.cos(atlx) * math.cos(orldy - atly)) 
##distance between Charlotte and orlando
dist_char_orld=EARTHRADIUS * math.acos(math.sin(charx) * math.sin(orldx) + math.cos(charx) * math.cos(orldx) * math.cos(chary - orldy))

##calculation for area enclosed between atl, Charlotte and orlando 
s_atl_char_orld =  (dist_atl_char + dist_char_orld + dist_orld_atl) / 2 
area_atl_char_orld = (s_atl_char_orld*(s_atl_char_orld - dist_atl_char)*(s_atl_char_orld - dist_char_orld)*(s_atl_char_orld - dist_orld_atl))**0.5
##calculation for area enclosed between Charlotte,savannah and orlando
s_char_sav_orld =  (dist_char_orld + dist_char_sav + dist_sav_orld) / 2 
area_char_sav_orld = (s_char_sav_orld*(s_char_sav_orld - dist_char_orld)*(s_char_sav_orld - dist_char_sav)*(s_char_sav_orld - dist_sav_orld))**0.5

#print (dist_orld_atl)
## print total area 
print("Estimated area between Atlanta, Georgia; Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina is:" , round(area_atl_char_orld + area_char_sav_orld,2))