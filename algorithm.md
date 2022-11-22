how does the doomsday algorithm work?

note: all dates are in DD/MM/YYYY format

doomsdays: 	
* 3/1 or 4/1 on a leap year
* 28/2 or 29/2 on a leap year
* 14/3 AKA π-day
* 4/4; 6/6; 8/8; 10/10; 12/12
* 9/5; 11/7; 5/9; 7/11

centuries:	
* 1700 – sunday
* 1800 – friday
* 1900 – wednesday
* 2000 – tuesday
* 2100 – sunday
* 2200 – friday
* 2300 – wednesday
* 2400 – tuesday

key years:
* 0; 28; 56; 84 – all become 0
* 0; 12; 24; 36; 48; 60; 72; 84 become 0;  1;  2;  3;  4;  5;  6;  0

days:
* sunday – noneday – 0
* monday – oneday – 1
* tuesday – twoday – 2
* wednesday – threesday – 3
* thursday – foursday – 4
* friday – fiveday – 5
* saturday – sixaday – 6

algorithm:
1.	What day of the week is doomsday that century? (see centuries)
2.	What day of the week is doomsday that year? (see key years)
3.	What is the closest doomsday to wanted date? (see doomdays)
4.	Count the day (see days)

examples:
15/07/1976
1. wednesday (1900 - see centuries)
2. xx76 (see key years)
  72 of that becomes 6;       +6
  4 more years until 76;      +4
  1 leap year among those 4;  +1
  sum is 11, always subtract any multiples of 7
  remainder is 4;
  wednesday is a 3 (see days), plus remainder of 4 equals 7 (ie 0) -> 
  doomsday in 1976 was sunday
3. closest doomsday to wanted date is 11/7 (see doomsdays)
4. 4 days until 15/7;
  doomsday that year is a sunday (a 0, see days)
  0 (sunday) + 4 (days until wanted date from closest doomdays) -> 4
  4 is a thursday (see days)
5. on the 15th of July 1976 it was a thursday.
