# 1st of December

## Synopsis

### Day 1

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

### Day 2

Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

---

## Notes :

Assortments of notes has been found with some significant locations.
Those locations can be used to determine where to beign to search.

Those locations doesn't have a name but an ID called **Location ID**.
Those notes has been splitted in two groups

Pair up the numbers and mesure how far apart they are. Pair up the smallest in the left lsit with the smallest in the right list.
Within each pair figure out how fare apart the two mubers are.

Example : 9 + 3 = 6; 7 + 4 = 3 So the total is 3 + 6 = 9

Need to add up all of those distances

---

## Steps of resolving :

Input list left
Input list right

Sort them from the smallest to the biggest
Add the result from each operation in a new array

Add up all the numbers after the loop ends

Get the result of how far apart they are
