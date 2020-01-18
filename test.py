#list of destination that we are using
destinations = ["Paris, France",
              "Shanghai, China",
              "Los Angeles, USA",
              "Sao Paulo, Brazil",
              "Cairo, Egypt"]

#lets define a test traveler to see how our functionality is working so far
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#attractions = [[] for count in destinations]

#We are going to identify each location based on its index in our destination list
#need to retrieve that index first
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
