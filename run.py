from PIL import Image, ImageFont, ImageDraw
import random

im = Image.new("RGB", (500, 200), "#fff")
draw = ImageDraw.Draw(im)

word_list = [[ "1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9", "10", "11", "12", "13", "14", "15"], #B
             ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"], #I
             ["31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45"], #N
             ["46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"], #G
             ["61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75"]] #O

for num in range(0,20):
  im = Image.new('RGB', (850,1100), (255,255,255))
  draw = ImageDraw.Draw(im)

  font = ImageFont.truetype("Montserrat-Black.ttf", 120)
  draw.text((85+170*0,180), "B", "red", font, align='center', anchor='mm')
  draw.text((85+170*1,180), "I", "blue", font, align='center', anchor='mm')
  draw.text((85+170*2,180), "N", "lime", font, align='center', anchor='mm')
  draw.text((85+170*3,180), "G", "purple", font, align='center', anchor='mm')
  draw.text((85+170*4,180), "O", "orange", font, align='center', anchor='mm')

  font = ImageFont.truetype("Montserrat-Black.ttf", 60)
  draw.text((425,60), "Let's Play BINGO!", 'black', font, align='center', anchor='mm')

  #FOR EVERY COLUMN
  for i in range(0,5):

    #ALREADY SELECTED
    drawn_list = []

    #FOR EVERY ROW
    for j in range(0,5):

      #DRAW THE BOX
      box = (0+i*170, 250+j*170, 170+i*170,420+j*170)
      draw.rectangle((box[0],box[1],box[2],box[3]), fill=(255,255,255), outline=(0,0,0), width=5)

      temp_color = 'black'

      #IF NOT FREE SPACE
      if(not (i == 2) or not (j == 2)):

        #SELECT A WORD
        selection = random.randrange(0,len(word_list[i]))
        while(selection in drawn_list):
          selection = random.randrange(0,len(word_list[i]))
        drawn_list.append(selection)
        text = word_list[i][selection]

      #FREE SPACE
      else:

        #REPLACE HERE
        text = "FREE\nSPACE"
        temp_color = 'magenta'

      font = ImageFont.truetype("Montserrat-Black.ttf", 20)
      draw.multiline_text((box[0]+85,box[1]+85), text, temp_color, font,align='center',anchor='mm')
  i = 0
  im.save('board_' + str(num) + ".jpg", quality=100)
