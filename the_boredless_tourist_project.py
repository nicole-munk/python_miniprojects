destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

#This function takes a list as a parameter
def get_traveler_location(traveler):
  traveler_destination=traveler[1]
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index=get_traveler_location(test_traveler)


attractions=[]

for city in destinations:
  attractions.append([])


def add_attraction(destination, attraction):
  destination_index=get_destination_index(destination)
  try:
    get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  attractions_with_interest=[]
  for i in attractions_in_city:
    possible_attraction=i
    attraction_tags=possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts=find_attractions("Los Angeles, USA", ['art'])


def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination, traveler_interests)
  interests_string="Hi "+traveler[0]+", we think you'll like these places around "+traveler_destination+": "
  for lugar in traveler_attractions:
    if lugar in interests_string:
      continue
    interests_string+=lugar
    interests_string+=", "
  return interests_string

smills_france=get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument', 'art']])
print(smills_france)
users_name=input('Your name: ')
place_user=input("Where are you? (Paris, France, Shanghai, China, Los Angeles, USA, São Paulo, Brazil, Cairo, Egypt)")
interest_one=input("Interest one: (beach, art, museum, historical site, monument, garden, skyscraper, viewing deck, zoo)")

def Convert(string):
    li = list(string.split(" "))
    return li
user_i=Convert(interest_one)

users_attractions=get_attractions_for_traveler([users_name, place_user, user_i])
print(users_attractions)
