TODO: Reflect on what you learned this week and what is still unclear.

# Exercise 1:
## countdown
This task was pretty simple, just a set of printouts that countdown from a given input to output from high to low. This is then followed by a completion message.

This one caused some grief as I was not sure whether I had to print like the original code, but turns out I had to return a list of each line. I only found out after running tests and reading tests lines and finding out it expects a return list.

*note this passes the test as the test counts the total number of elements in the list but only allows for the length of the countdown and not the completion message as well. I had to shift the countdown either -1 for countdowns and +1 for count-ups for it to make sense.

## calculation modules
Found an odd error in the original bad code.
`triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2`
This would only give a square of the hypotenuse, not the exact magnitude making it a mathematical error not a coding error.

### Triangle facts
This function just calls all the calculation functions previous to display the facts of the triangle

## Tell me about this triangle
Had to just run tests to find out what was wrong, was not sure what it wanted.


****************************************

## Update: I did it all wrong :(
I was not supposed to complete the function for everything

## Wordy pyramid
Similar to week 4 just went back and changed the url and change in data format, no longer JSON.

# Exercise 2
This was hard to wrap my head around, so mainly guard represents how many recursive repetitions you want.

## abba()
The hardest part of this was figuring out the rule change, but just following the lines in the given example is the only way to really follow it. The only other issue is that the Italian recipe uses the map function since the rule subfunction has a singular input, the abba function uses two so I do the long way around which is a loop.

```python
for letter in parts:
        result.append(apply_rules(letter,guard))
```

### koch
This was pretty easy just had to figure out that angle needed to be changed to 90 deg and that there needed to be an extra line draw function.
