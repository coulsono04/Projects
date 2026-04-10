
# This program tests and uses functions to display travel data


destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination = "destination"):
  destination_index = destinations.index(destination)
  #print(destination_index)
  return destination_index

get_destination_index("Paris, France")

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[], [], [], [], []]

print(attractions)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  #attractions_for_destination = destination_index.index(attraction)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])



def find_attractions(destination, interests):
  attractions_with_interest = []
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attraction_tags = []
  for possible_attraction in attractions_in_city:
    attraction_tags += possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around "
  #remove
  print(traveler_destination)
  print(traveler_attractions)
  interests_string += traveler_destination
  for i in traveler_attractions:
    interests_string += i + ", "
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
