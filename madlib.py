import time 
import requests

#madlib = requests.get("http://libberfy.herokuapp.com?q=Hello%20world.%20Testing%20this%20API")

#print madlib.headers



print "Welcome to dadlib powered by python"
time.sleep(1)

exclamation = raw_input("Please give an exclamation: ") 
time.sleep(0.5)
adverb = raw_input("Please give an adverb: ")
time.sleep(0.5)
noun = raw_input("Please give a noun: ")
time.sleep(0.5)
adjective = raw_input("Please give an adjective: ")


time.sleep(0.5)


print "%s! He said %s as he jumped into his convertible %s and drove off with his %s wife." %(exclamation, adverb, noun, adjective)

