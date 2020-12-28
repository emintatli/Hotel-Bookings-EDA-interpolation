# Hotel-Bookings-EDA-interpolation
We gonna try to fill the NaN values of Hotel-Bookings.csv

csv File loaded by pandas
![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_1.png?raw=True)

Then we gonna check all columns data types and pop all the non integer columns

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_2.png?raw=True)

We gonna check how many NaN values exist in our Data Frame

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_3.png?raw=True)

We checked for any outlier data but they dont exist

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_4.png?raw=True)

Lets start with children column
![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_6-1.png?raw=True)

We got the mean of children counts who has 2 parents.It's near 0 so we can say the value of the children who have 2 parents is going to be 0.

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_5.png?raw=True)

We replace NaN values to 0. 

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_6.png?raw=True)

We got the children counts who has 3 parents. It's pretty the same as 2 so we replace it with 0 for this one too.Now we dont have any children which have NaN value.

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_7.png?raw=True)

So we have Company column and Agent column.We have to figure it out how we gonna replace the NaN values for them.To do that we use correlation map which gives us which column related to the other one.

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_8.png?raw=True)

As you can see Agent column and Company column are more related than the other ones so we use them to compare.

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_9.png?raw=True)

We get rid of those who have NaN values on both company and agent column and we split that dataframe into 2 pcs.One of them which have only NaN values in the company column and the other one have only NaN values in the agent column

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_10.png?raw=True)

Then we get a number which gives us their relation. (company*0.773=agent)

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_12.png?raw=True)

Then we fill the Nan values for both columns

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_13.png?raw=True)

In the end we dont have any NaN values left.

![Image](https://github.com/emintatli/Hotel-Bookings-EDA-interpolation/blob/main/res/Screenshot_14.png?raw=True)
