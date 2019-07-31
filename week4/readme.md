TODO: Reflect on what you learned this week and what is still unclear.

# get_some_detail
This one was not too difficult, just had to create some variables that held the json/dict values for the necessary items:
* last name
* email password
* the addition of the postcode and the id value

# wordy pyramid
Defining this was difficult because I had to figure out if I had to keep reloading the page which different arguments or I can just do a single webpage with
'minLength = 3, maxLength = 20 and limit = 18'. This is dependant on whether there are duplicates of words of different lengths.

Turns out it does have duplicates and the lengths are just randomly generated with the constraints given which makes sense...

Therefore, I had to just call the webpage repeatedly with the constraints for min and max set at each length from 3 to 20. This was found to produce an interesting error, where the random number generator failed to generate words with 17+ characters on the first try. This has cause me to change my for loop to a while loop and include a counter that only increments when a word has been generated otherwise, it will repeated request the url.

Inserting in middle of array:
```python
array = ["banana","oranges"]
array.insert(int(len(array)/2),"apples")
array
```
will output:
```
["banana","apples,"oranges"]
```
For this specific case, the order will look something like [2,4,6,5,3,1] which can be reverse using `reverse()` to get the desired order.

## UPDATO
So the wordy api was not great for the whole class to use so Ben wrote his own (MVP).
Had to change it up found that since it only gave one word at a time the data came in was no longer in json format had to change up code slightly to reflect that and changed variables to reflect the reduced input arguments in the new URL.

# pokedex api
This one was not too difficult the items needed for the tallest poke in the given range were:
* Name
* Weight
* Height
A single loop for to linear search the range is used to comb the range and the height was used as a comparator.

# diarist
## Gcode
From what I have read gcode is the name for the programming language used by numerical control machines or computer numerical control machines (CNC). Diversely used for CAM and CAD manufacturing, the gcode is read by the machine and intepreted as a set of commands to control the translational and rotational actions of the CNC machine. 

*Note: I work in a small volume manufacturing company so I see a lot of gcode in action.*

## code bit
This one isn't too difficult just followed the template from the IOexamples.py. The key here was to run the file as exercise1.py first to create the lasers.pew file although it is tested in a different dir than the actual tests.py.

Running exercise1.py tests that lasers.pew is in the /me dir, while running tests.py tests that lasers.pew is in /me/week4 dir.

Another key note is that the comments mention to count laser on and off but gave the laser off gcode `M10 P1` only. I counted both initially, looked the test file and saw that it was just over half of that and concluded it must be counted just laser off and subsequently accounted for such.