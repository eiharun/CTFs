# 1. Seaside | File: [JPG](Seaside1.jpg)
~~~
From the picture, can you find the closest train station?

Wrap the English name, as it appears on Google Maps, in lowercase, with the DOCTF{---} flag format, replacing any spaces with _.
~~~
![Seaside Imade](https://github.com/eiharun/CTFs/blob/461978aeb7ec6d1eea736e988e793540dc33b597/DigitalOverdose2022/MayaWentOnATrip/Seaside1.jpg)
#### Step 1
Zooming into the name of the building:

![image](https://user-images.githubusercontent.com/92404926/202931703-fb0e413d-f7d4-4783-9494-4a7cc0983b21.png)

#### Step 2
I can make out `Darakhyu Compact Luxury Hotel`. We found it in google images! The name of the hotel is `Darakhyu Yeosu`

![image](https://user-images.githubusercontent.com/92404926/202931764-bba7cf34-626c-4ffd-a65e-6133238e5872.png)

#### Step 3
As we can see this is the location of the photo, the nearest train station is `Yeosu EXPO`

![image](https://user-images.githubusercontent.com/92404926/202931817-357978f7-99f5-47da-8883-613b6f5c61c7.png)
![image](https://user-images.githubusercontent.com/92404926/202931857-c2bc18e6-bbdf-43e3-9920-9218bee6e363.png)

#### Step 4
Form the flag
`DOCTF{yeosu_expo}`

# 2. SympoZzzium
~~~
I attended an event near Yeosu, and it was a bit boring, so I decided to play with Wigle. 

What institution did this event take place at?

Wrap the English name, in lowercase, with the DOCTF{xxxxx} flag format, replacing any spaces with _.
~~~
#### Step 1
Looking through the csv file, I noticed there are a lot of `eduroam` SSIDs.
Eduroam is a network that is commonly used in universities. So we can narrow the institution to an university
I also noticed `JNU`, which sounds like an abbreviation for an university.

![image](https://user-images.githubusercontent.com/92404926/202945649-50e83c22-42dc-4c33-8eee-87951fcc0d39.png)

#### Step 2
Googling JNU in Yeosu, gives us the location of an university: `Chonnam National University`

![image](https://user-images.githubusercontent.com/92404926/202945594-f4f992a2-3434-424e-ba1f-9d67e2f4deab.png)

#### Step 3
Form the flag
`DOCTF{chonnam_national_university}`
