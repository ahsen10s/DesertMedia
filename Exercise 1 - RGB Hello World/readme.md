Exercise 1 - RGB Hello World

This project was different from most others I’ve worked on before. Having only a singular LED to work with to tell a story or convey a story was different. My mind first went to phenomena that are famous for their vivid shades, like rainbows or northern lights and I set out to recreate their colors using the LED. But then it dawned on me that these displays of lights are too literal, and don’t contain any unique input from my side. After another session of brainstorming I decided to depict the 4 seasons in the colors that matched them.
For this light show, the LED will shine 4 to 5 colors that represent my experience of each season. The LED will turn off for 3 seconds to indicate the transition to the next season. This show will progress in the following order and repeat continuously; summer, autumn, winter, spring. Each color and their corresponding meaning to me is commented in the code.

led[0] = (0, 0, 0)      #no light to indicate transition to next season
time.sleep(3)

Above is a code snippet I used to stop the LED from shining any color for 3 seconds, which indicates a transition to the next season. I repeated this code after every season. After playing around with different rgb values for the LED, I realized that the LED cannot produce black which seems very obvious to me now. So I used this to make it look like the LED turned off for specific periods of time.
With this code I believe I was able to convey the story I wanted to. The story of my experiences through the changing seasons of the year. Perhaps this project can be further developed with more components, like speakers to emit the sounds connected to my experiences. More LEDs would also help me to make more complex light shows and convey a more complex story.
