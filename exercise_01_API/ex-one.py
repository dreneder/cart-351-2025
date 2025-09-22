# Exercise 1 - André Neder and Hugo Waterfall
# 4. Write the initial request: So - you are now ready to write the initial serach request in your python script... I will help you get started... You will write a request to give back all the results for montreal:
#import the lib
import requests

#my api key 
token = 'c06eff39ec548433d763465a03fdd508677b082b'

#this is the beginning of the url string which will be used for the get request
url = "https://api.waqi.info/search/"

#this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
response = requests.get(url, params={"token": token, "keyword": "montreal"})

#after getting the response from the API, we will convert it into json so that we can access the data
results = response.json()

#this prints the entire response from the API
print(results)
print()
print()

# 5. Write the code and or answer the questions as comments in the code NEATLY so that I can read it
#In your script write the code to get the type of the results variable. Run the code and document the answer.
print(type(results))
print()

#In your script write the code to get the keys of the results variable. Run the code and document the answer
print(results.keys())
print()

#The first key of the results variable is called data - and if you look at the response fields in the documentation you will see that this is where we have all the data that we want ...So - now write the code to access the content associated with the data field. Save the result from the expression as a variable called responseData. Then find out the type of responseData ... Document your findings.
print(results['data'])
print()
responseData = results['data']
print()
print(type(responseData))
print()
#When we access the data index through results, we get a list of dictionaries. The variable responseData is a list.

#What is the result of running the following code (put the code after the assignment above):
for item in responseData:
    print(item)
    print()

print()
#What does each item represent?
#Each item represents an individual dictionary

#Write the code to determine the type of the item variable
#The type of the first item:
print(type(responseData[0]))
print()

#Write the code to determine the keys associated with the item variable
print(item.keys())

#Modify the code above to now print out the name of each station from the responseData. Document the results.
for item in responseData:
    print("station name:",item['station']['name'])
    print()
#Each item in responseData is a dictionary. The string 'station' is a key, and so is the string 'name', which means the for loop will print out the 'name' of 'station' for each item

#Append the code above to also print out the geolocations of each station from the responseData. The output for the geolocation should look like the following example:lat: 45.426509. long: -73.928944. Document your results
for item in responseData:
    print("station name:",item['station']['name'])
    print("lat:", item['station']['geo'][0])
    print("long:", item['station']['geo'][1])

    print()
#Here we are accessing elements of the station element of item

#Append the code above to print out the air quality index for each item AND the uid for each item. The output needs to be neat and labelled!
for item in responseData:
    print("station name:",item['station']['name'])
    print("lat:", item['station']['geo'][0])
    print("long:", item['station']['geo'][1])
    print("long:", item['station']['geo'][1])
    print("air q index:", item['aqi'])
    print("uid:", item['uid'])

    print()

# 6. Access the feed results:
#Lets start a new request ... and say that we wanted the results for the city with uid == 5468 then this is the code:
#Add the above code and run it
url_feed = "https://api.waqi.info/feed/@5468"
response_feed = requests.get(url_feed, params={"token": token})
results_feed = response_feed.json()
print(results_feed)

print()

#So - now write the code to access the content associated with the data field. Save the result from the expression as a variable called response_data_feed. What id the type of this variable
print(results_feed['data'])
response_data_feed = results_feed['data']
print()
print(type(response_data_feed))
print()

#Write a for loop to iterate through the `response_data_feed` variable . Document the results
for item in response_data_feed:
    print(response_data_feed[item])
print()
#The results are all the elements within each index of response_data_feed

#Next write the expression to access the aqi field and the dominentpolfield - according to the documentation what does this field represent? Save both values in new variables.
print(response_data_feed['aqi'])
print(response_data_feed['dominentpol'])
#dominentpol represents the dominant pollutant, which, in this case, is pm2.5
aqi = response_data_feed['aqi']
dominentpol = response_data_feed['dominentpol']
print()

#OK ... now access you will access the iaqi field. You will see that the result is another dictionary, with keys for different pollutants. Each one of those keys—somewhat inexplicably—has another dictionary for its values, whose only key (`v`) points to the actual value for that pollutant... Write the code and document your results
print(response_data_feed['iaqi'])
print(response_data_feed['iaqi']['pm25']['v'])
# We used the variable for the dominant pollutant, and accessed its index in the iaqui, then accessed the v value

#Well now - we want to use the value from the dominentpol field to access the actual value for that pollutant... (i.e. say the `dominentpol =so2') - how can we use the data from the iaqi field to access the actual value? ... hint: the keys from the iaqi dictionary map directly to the `dominentpol` field. Write the code to access this value...and document your results
print(response_data_feed['iaqi'])
print()
print(response_data_feed['iaqi'][dominentpol]['v'])
print()

# 7. So - now that you can access the feed for a specific station in a particular city, and from that feed you can access the value of its dominant pollutant.... : explain theoretically (you do not have to write the code) what the process would be to access the value of the dominant pollutant value from different cities ...
#From the documentation we could use /feed/:city/? and create a city variable with a string(name of city) or id, from that variable the url feed will be appended and modify the other results accordingly.