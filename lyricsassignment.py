from PyLyrics import *

#print(PyLyrics.getLyrics('Run-D.M.C.','Sucker M.C.\n\'s (Krush Groove 1)')) #Print the lyrics directly

hip_pop = [PyLyrics.getLyrics('Grandmaster Flash and the Furious Five ','The Message')]
hip_pop.append(PyLyrics.getLyrics('Sugarhill Gang','Rappers Delight'))
hip_pop.append(PyLyrics.getLyrics('Afrika Bambaataa','Planet Rock'))
#hip_pop.append(PyLyrics.getLyrics('Run-D.M.C.','Sucker M.C.s')) 
hip_pop.append(PyLyrics.getLyrics('Geto Boys','Mind Playing Tricks on Me'))
hip_pop.append(PyLyrics.getLyrics('Snoop Dogg','Nuthin But a G Thang'))
hip_pop.append(PyLyrics.getLyrics('Public Enemy','Fight the Power'))
hip_pop.append(PyLyrics.getLyrics('Notorious B.I.G.','Juicy'))
hip_pop.append(PyLyrics.getLyrics('Eric B.','Paid in Full'))

country =[PyLyrics.getLyrics('Johnny Cash', 'I Walk the Line')]
country.append(PyLyrics.getLyrics('Patsy Cline', 'Crazy'))
country.append(PyLyrics.getLyrics('Gretchen Wilson','Redneck Woman'))
country.append(PyLyrics.getLyrics('George Jones', 'He Stopped Loving Her Today'))
country.append(PyLyrics.getLyrics('Jimmie Rodgers', 'Blue Yodel 9'))
country.append(PyLyrics.getLyrics('Tammy Wynette', 'Stand By Your Man'))
country.append(PyLyrics.getLyrics('Ray Charles', 'You Dont Know Me'))
country.append(PyLyrics.getLyrics('Merle Haggard', 'Mama Tried'))
country.append(PyLyrics.getLyrics('Dolly Parton', 'Jolene'))
country.append(PyLyrics.getLyrics('Waylon Jennings and Willie Nelson', 'Mammas, Dont Let Your Babies Grow Up to Be Cowboys'))

motown =[PyLyrics.getLyrics('The Temptations', 'My Girl')]
motown.append(PyLyrics.getLyrics('Marvin Gaye', 'Whats Going On'))
motown.append(PyLyrics.getLyrics('Marvin Gaye', 'I Heard it Through the Grapevine'))
motown.append(PyLyrics.getLyrics('The Temptations', 'Papa was a Rolling Stone'))
motown.append(PyLyrics.getLyrics('Smokey Robinson and the Miracles', 'Tracks of My Tears'))
motown.append(PyLyrics.getLyrics('The Temptations', 'Aint Too Proud to Beg'))
motown.append(PyLyrics.getLyrics('Smokey Robinson and the Miracles', 'Tears of a Clown'))
motown.append(PyLyrics.getLyrics('Marvin Gaye and Tammi Terrell', 'Aint No Mountain High Enough'))
motown.append(PyLyrics.getLyrics('Martha and the Vandellas', 'Dancing in the Street'))
motown.append(PyLyrics.getLyrics('Marvin Gaye', 'Lets Get it On'))

boyband = [PyLyrics.getLyrics('The Jackson 5', 'I Want You Back')]
boyband.append(PyLyrics.getLyrics('The Jackson 5', 'Ill be There'))
boyband.append(PyLyrics.getLyrics('Bay City Rollers', 'Saturday Night'))
boyband.append(PyLyrics.getLyrics('The Monkees', 'Im a Believer'))
boyband.append(PyLyrics.getLyrics('Backstreet Boys', 'I Want It That Way'))
boyband.append(PyLyrics.getLyrics('N Sync', 'Bye, Bye, Bye'))
boyband.append(PyLyrics.getLyrics('The Jackson 5', 'ABC'))
boyband.append(PyLyrics.getLyrics('Take That', 'Back for Good'))
boyband.append(PyLyrics.getLyrics('New Kids on the Block', 'You Got It'))
boyband.append(PyLyrics.getLyrics('One Direction', 'Story of My Life'))

randb = [PyLyrics.getLyrics('Otis Redding', 'I Cant Turn You Loose')]
randb.append(PyLyrics.getLyrics('Marvin Gaye', 'Sexual Healing'))
randb.append(PyLyrics.getLyrics('Sam Cooke', 'You Send Me'))
randb.append(PyLyrics.getLyrics('Ray Charles', 'Mess Around'))
randb.append(PyLyrics.getLyrics('Al Green', 'Lets Stay Together'))
randb.append(PyLyrics.getLyrics('Stevie Wonder', 'Uptight'))
randb.append(PyLyrics.getLyrics('James Brown', 'Please, Please, Please'))
randb.append(PyLyrics.getLyrics('Smokey Robinson', 'Shop Around'))
randb.append(PyLyrics.getLyrics('Luther Vandross', 'Here and Now'))
randb.append(PyLyrics.getLyrics('B.B King', 'You Upset Me Baby'))




f = open("hip_pop.py", "w")
g_hp = [hip_pop]
f.write("\n".join(map(lambda x: str(x), g_hp)))
f.close()

f2 = open("")


#Test the following print(genre) list 
'''
print(hip_pop[0])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print(hip_pop[1])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print(hip_pop[2])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
#pickup 
'''
