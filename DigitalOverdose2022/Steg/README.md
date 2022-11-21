# Arrow

#### Step 1
Use https://www.aperisolve.com/ and upload the image

![image](https://user-images.githubusercontent.com/92404926/202953737-2e2170b7-609a-40fa-b88e-d44361a47751.png)

![image](https://user-images.githubusercontent.com/92404926/202953855-ffc40082-af1c-4475-b920-63c8bffa0757.png)

#### Step 2
I noticed this in the Exiftool data. The answer here is `x=3`. I also noticed this weird string `sdvvrug : qrmlq`.
This could be a ceaser cipher with a shift of 3.

![image](https://user-images.githubusercontent.com/92404926/202954093-570be164-c53c-419b-ad0b-f2b1045d6813.png)

Indeed it is. The password is `nojin`. So we go back to aperisolve and input the password and we unlocked the file hidden within the image

![image](https://user-images.githubusercontent.com/92404926/202954269-5508e2c7-189c-4843-a65a-a2883227794a.png)
![image](https://user-images.githubusercontent.com/92404926/202954225-f37ab7d5-1a0b-40b1-9912-576431ba0f82.png)

#### Step 3

Contents of text file:
![image](https://user-images.githubusercontent.com/92404926/202954452-8ffdb0fb-5e43-4781-a1b7-e7f58dcd9b39.png)

The answer to these questions:
~~~
1. Which component on the Motherboard generates the most heat? (hint:three letters)
CPU

2. What is the name of the fastest cache on the motherboard?
L1

3. What is the maximum amount of DRAM that a 32-bit system can support?
4GB

4. The LGP CPU is mostly used by which company? (Hint: there are two companies that build CPUs; one of them is the answer!)
Intel
~~~

#### Step 4

One problem... where is the zip file. There is a hint at the bottom `ARROW#5141`. This is a discord tag. I added him and discovered his github was linked in his profile.

![Discord](https://user-images.githubusercontent.com/92404926/202953343-b4c3044f-3e7b-4fe8-a5ab-a8d0f0036a34.png)
![image](https://user-images.githubusercontent.com/92404926/202954693-318c1847-8513-4c4e-81d6-306e2607745d.png)

The zip file has a password. But we know it is one of the answers to the questions above. I tried all 4, the correct one was `Intel`
Contents of the file:

#### Step 5

![image](https://user-images.githubusercontent.com/92404926/202954787-979d9615-a8db-42f1-bc47-adafab5b238a.png)

The audio file was a DMF corresponding to 445599

![image](https://user-images.githubusercontent.com/92404926/202954842-98f2de42-9947-455a-b8ab-3a078916dd51.png)

I assume this is the password to the hidden file within `panda.jpg`

![PandaStegHide](https://user-images.githubusercontent.com/92404926/202953608-d70da8eb-97d8-4e65-a451-4093c337e3ee.png)

#### Step 6

Its an audio file, so I import it into audacity. Nothing interesting in its waveform, but lets check the spectrogram

![image](https://user-images.githubusercontent.com/92404926/202955006-e3da7c69-ace7-44ed-8c87-b6f9cc8a305a.png)
![image](https://user-images.githubusercontent.com/92404926/202955075-b4ab99b6-1a74-4f06-a013-f1b6ba4d30f4.png)

#### Step 7

We have the flag!
`DOCTF{CompTia_A+}`

