#list of destination that we are using
destination = ["Paris, France",
              "Shanghai, China",
              "Los Angeles, USA",
              "Sao Paulo, Brazil",
              "Cairo, Egypt"]

#lets define a test traveler to see how our functionality is working so far
test_traveler = ["Erin Wilkes",
                "Shanghai, China",
                "Historical site",
                "Art"]

attractions = [[] for count in destination]

#We are going to identify each location based on its index in our destination list
#need to retrieve that index first
def get_destination_index(location):
  destination_index = destination.index(location)
  return destination_index

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(destination):
  traveler_destination = destination
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location("Shanghai, China")

#print(test_destination_index)
#print(attractions)

def add_attractions(destination,theAttraction):
  try:
    destination_index = get_destination_index(destination)
    if(destination_index!=''):
      for count in range(len(theAttraction)):
        attraction_for_destination.append(theAttraction[count])
    return attraction_for_destination
  except ValueError:
    return []
  
  print(add_attraction('Los Angeles, USA'],['Venice Beach', 'beach']))