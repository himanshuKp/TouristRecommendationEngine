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

#We are going to identify each location based on its index in our destination list
#need to retrieve that index first
def get_destination_index(location):
  destination_index = destination.index(location)
  return destination_index

print(get_destination_index("Los Angeles, USA"))