# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def update_damage(listD):
  updated_dmg = []
  for dmg in listD:
    if(dmg[-1:] == 'M'):
      updated_dmg.append(float(dmg.replace("M",""))* conversion["M"])
    elif dmg[-1:] == 'B':
      updated_dmg.append(float(dmg.replace("B",""))* conversion["B"])
    else:
       updated_dmg.append("Damages not recorded")
  return updated_dmg
updated=update_damage(damages)
#print(updated)
# 2 
# Create a Table
hurricanes = {}

for name in names:
    hurricanes.update({name: {'Name': '', 
                             'Month': '',
                             'Year': '',
                             'Max Sustained Wind': '',
                             'Areas Affected': '',
                             'Damage': '',
                             'Deaths': ''}})

# Create and view the hurricanes dictionary

def create_hurricane(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for element in range(0,34):
        hurricanes[names[element]] = {'Name': names[element], 
                                     'Month': months[element],
                                     'Year': years[element],
                                     'Max Sustained Wind': max_sustained_winds[element],
                                     'Areas Affected': areas_affected[element],
                                     'Damage': damages[element],
                                     'Deaths': deaths[element]}
    return hurricanes
create_hurricane(names, months, years, max_sustained_winds, areas_affected, updated, deaths)
#print(hurricane['Cuba I'])
#print(hurricane)

# 3
# Organizing by Year
hurricane_by_year = []
# create a new dictionary of hurricanes with year and key
def hurricane_by_year_dictionary(year):
    hurricane_by_year = []
    for name in hurricanes:
        if (hurricanes[name]['Year'] == year):
            hurricane_by_year.append(hurricanes[name])
    return hurricane_by_year

#print(hurricane_by_year_dictionary(1932))
#print(hurricane_by_year_dictionary(2018))

# 4
# Counting Damaged Areas

affected_areas = {}
affected_areas_list = []
for area in areas_affected:
  for item in area:
    if item not in affected_areas_list:
      affected_areas_list.append(item)
affected_areas_list.sort()
#print(affected_areas_list)

# create dictionary of areas to store the number of hurricanes involved in

for area in affected_areas_list:
    affected_areas.update({area: 0})
for area in areas_affected:
  for item in area:
    if item in affected_areas_list:
      affected_areas[item] +=1
#print(affected_areas)

# 5 
# Calculating Maximum Hurricane Count
# # find most frequently affected area and the number of hurricanes involved in

def most_affected_area(affected_areas):
    max_count = 0
    area_name = ''
    for name, value in affected_areas.items():
        if max_count <= value:
            max_count = value
            area_name = name
    return 'The most frequently affected area was {} and {}hurricanes were involved in.'.format(area_name,max_count)
#print(most_affected_area(affected_areas))
# 6
# Calculating the Deadliest Hurricane
def most_deadliest_hurricane(hurricanes):
    max_death = 0
    hurricane_name = 0
    for names in hurricanes:
        if max_death <= hurricanes[names]['Deaths']:
            max_death = hurricanes[names]['Deaths']
            hurricane_name = names
    return "The Deadliest Hurricane was \'{}\' and caused {} deaths.".format(hurricane_name, max_death)
# find highest mortality hurricane and the number of deaths

#print(most_deadliest_hurricane(hurricanes))

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, # > 0  and <= 100
                   1: 100, # > 100 and <= 500
                   2: 500, # > 500  and <= 1000
                   3: 1000, # > 1000 and <= 10000
                   4: 10000} # > 10000

mortality_hurricanes_dictionary = {}
for key in mortality_scale:
    mortality_hurricanes_dictionary.update({key: []})

# categorize hurricanes in new dictionary with mortality severity as key
for name in hurricanes:
    if (hurricanes[name]['Deaths'] > mortality_scale[0] and hurricanes[name]['Deaths'] <= mortality_scale[1]):
        mortality_hurricanes_dictionary[0].append(hurricanes[name])
    elif (hurricanes[name]['Deaths'] > mortality_scale[1] and hurricanes[name]['Deaths'] <= mortality_scale[2]):
        mortality_hurricanes_dictionary[1].append(hurricanes[name])
    elif (hurricanes[name]['Deaths'] > mortality_scale[2] and hurricanes[name]['Deaths'] <= mortality_scale[3]):
        mortality_hurricanes_dictionary[2].append(hurricanes[name])
    elif (hurricanes[name]['Deaths'] > mortality_scale[3] and hurricanes[name]['Deaths'] <= mortality_scale[4]):
        mortality_hurricanes_dictionary[3].append(hurricanes[name])
    else:
        mortality_hurricanes_dictionary[4].append(hurricanes[name])
#print(mortality_hurricanes_dictionary)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def greatest_damage_hurricane(hurricanes):
    max_damage = 0
    hurricane_name = 0
    for names in hurricanes:
        if hurricanes[names]['Damage'] != "Damages not recorded":
            if max_damage <= float(hurricanes[names]['Damage']):
                max_damage = float(hurricanes[names]['Damage'])
                hurricane_name = names
    return "The hurricane that caused the greatest damage was \'{}\' and caused {} $ in damages.".format(hurricane_name, max_damage)
#print(greatest_damage_hurricane(hurricanes))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

damages_hurricanes_dictionary = {}
for key in damage_scale:
    damages_hurricanes_dictionary.update({key: []})
  
# categorize hurricanes in new dictionary with damage severity as key
for name in hurricanes:
    if hurricanes[name]['Damage'] != "Damages not recorded":
        if (float(hurricanes[name]['Damage']) > damage_scale[0] and float(hurricanes[name]['Damage']) <= damage_scale[1]):
            damages_hurricanes_dictionary[0].append(hurricanes[name])
        elif (float(hurricanes[name]['Damage']) > damage_scale[1] and float(hurricanes[name]['Damage']) <= damage_scale[2]):
            damages_hurricanes_dictionary[1].append(hurricanes[name])
        elif (float(hurricanes[name]['Damage']) > damage_scale[2] and float(hurricanes[name]['Damage']) <= damage_scale[3]):
            damages_hurricanes_dictionary[2].append(hurricanes[name])
        elif (float(hurricanes[name]['Damage']) > damage_scale[3] and float(hurricanes[name]['Damage']) <= damage_scale[4]):
            damages_hurricanes_dictionary[3].append(hurricanes[name])
        else:
            damages_hurricanes_dictionary[4].append(hurricanes[name])
print(damages_hurricanes_dictionary[4])