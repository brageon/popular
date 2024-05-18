import pandas as pd
with open('Act.csv', 'r') as cv1, open('Adv.csv', 'r') as cv2, open('Arc.csv', 'r') as cv3, \
open('Bet.csv', 'r') as cv4, open('Bod.csv', 'r') as cv5, open('Bok.csv', 'r') as cv6, 
open('Bus.csv', 'r') as cv7, open('Car.csv', 'r') as cv8, open('Cas.csv', 'r') as cv9, 
open('Com.csv', 'r') as c10, open('Cop.csv', 'r') as c11, open('Dat.csv', 'r') as c12, 
open('Des.csv', 'r') as c13, open('Edu.csv', 'r') as c14, open('Ent.csv', 'r') as c15, 
open('Eve.csv', 'r') as c16, open('Fin.csv', 'r') as c17, open('Foo.csv', 'r') as c18, 
open('Hem.csv', 'r') as c19, open('Ino.csv', 'r') as c20, open('Lib.csv', 'r') as c21, 
open('Lif.csv', 'r') as c22, open('Map.csv', 'r') as c23, open('Med.csv', 'r') as c24, 
open('Mus.csv', 'r') as c25, open('New.csv', 'r') as c26, open('Par.csv', 'r') as c27, 
open('Pho.csv', 'r') as c28, open('Pro.csv', 'r') as c29, open('Puz.csv', 'r') as c30, 
open('Rac.csv', 'r') as c31, open('Rol.csv', 'r') as c32, open('Sho.csv', 'r') as c33, 
open('Sim.csv', 'r') as c34, open('Soc.csv', 'r') as c35, open('Spo.csv', 'r') as c36, 
open('Sta.csv', 'r') as c37, open('Tol.csv', 'r') as c38, open('Tra.csv', 'r') as c39, 
open('Tri.csv', 'r') as c40, open('Veh.csv', 'r') as c41, open('Vid.csv', 'r') as c42, 
open('Wea.csv', 'r') as c43, open('Woo.csv', 'r') as c44:
    import1 = cv1.readlines()
    import2 = cv2.readlines()
    import3 = cv3.readlines()
    import4 = cv4.readlines()
    import5 = cv5.readlines()
    import6 = cv6.readlines()    
    import7 = cv7.readlines()
    import8 = cv8.readlines() 
    import9 = cv9.readlines()
    import10 = c10.readlines()       
    import11 = c11.readlines()
    import12 = c12.readlines()       
    import13 = c13.readlines()
    import14 = c14.readlines()       
    import15 = c15.readlines()
    import16 = c16.readlines()       
    import17 = c17.readlines()
    import18 = c18.readlines()       
    import19 = c19.readlines()
    import10 = c10.readlines()       
    import11 = c11.readlines()
    import12 = c12.readlines()       
    import13 = c13.readlines()
    import14 = c14.readlines()       
    import15 = c15.readlines()
    import16 = c16.readlines()       
    import17 = c17.readlines()
    import18 = c18.readlines()       
    import19 = c19.readlines()
    import20 = c20.readlines()       
    import21 = c21.readlines()
    import22 = c22.readlines()       
    import23 = c23.readlines()
    import24 = c24.readlines()       
    import25 = c25.readlines()
    import26 = c26.readlines()       
    import27 = c27.readlines()
    import28 = c28.readlines()       
    import29 = c29.readlines()
    import30 = c30.readlines()       
    import31 = c31.readlines()
    import32 = c32.readlines()       
    import33 = c33.readlines()
    import34 = c34.readlines()       
    import35 = c35.readlines()
    import36 = c36.readlines()       
    import37 = c37.readlines()
    import38 = c38.readlines()       
    import39 = c39.readlines()
    import40 = c40.readlines()       
    import41 = c41.readlines()
    import42 = c42.readlines()       
    import43 = c43.readlines()
    import44 = c44.readlines()                     
with open('dif.csv', 'w') as outFile:        
    for row in import2:
        if row not in import1:
            outFile.write(row)
    for row in import4:
        if row not in import3:
            outFile.write(row)
    for row in import6:
        if row not in import5:
            outFile.write(row)
    for row in import8:
        if row not in import7:
            outFile.write(row)
    for row in import10:
        if row not in import9:
            outFile.write(row)
    for row in import12:
        if row not in import11:
            outFile.write(row)
    for row in import14:
        if row not in import13:
            outFile.write(row)
    for row in import16:
        if row not in import15:
            outFile.write(row)
    for row in import18:
        if row not in import17:
            outFile.write(row)
    for row in import20:
        if row not in import19:
            outFile.write(row)
    for row in import22:
        if row not in import21:
            outFile.write(row)
    for row in import24:
        if row not in import23:
            outFile.write(row)
    for row in import26:
        if row not in import25:
            outFile.write(row)
    for row in import28:
        if row not in import27:
            outFile.write(row)
    for row in import30:
        if row not in import29:
            outFile.write(row)            
    for row in import32:
        if row not in import31:
            outFile.write(row)
    for row in import34:
        if row not in import33:
            outFile.write(row)
    for row in import36:
        if row not in import35:
            outFile.write(row)
    for row in import38:
        if row not in import37:
            outFile.write(row)
    for row in import40:
        if row not in import39:
            outFile.write(row)
    for row in import42:
        if row not in import41:
            outFile.write(row)
    for row in import44:
        if row not in import43:
            outFile.write(row)