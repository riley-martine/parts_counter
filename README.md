# part_counter

Real simple script to count the parts I needed to build an adder-subtractor circuit, using recursion!


For example: I can say I need one full adder (`python parts.py "Full Adder"`), and the script will figure out this means two half adders and an OR gate, and each half adder needs an XOR and an AND gate. The script sums this up and says I need:

      Num  Part
    -----  --------
        2  XOR gate
        2  AND gate
        1  OR gate


## usage
See file `partslist.txt` for example data. Edit this to contain the data for everything you need.

