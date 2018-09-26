player = { 
  "name": "p1", 
}

rooms = {
  "room1" : "open ocean",
  "room2" : "ship",
  "room3" : "East Australian Current"
}                                                                                       
  
def printGraphic(name):
  if (name == "shark"):


    print "                            ######### "
    print "                          ##XXXX#XX####                    ######### "
    print "                          ###############          ##################### "
    print "                            ###XXXXXXXXX### ########XXXXXXXXXXXXXXXXXX## "
    print "                              #X#XXXXXXX#X#####XX#XXXXXXX XXXXXXX XX### "
    print "                               #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX### "
    print "                               ##XXXXXXXXX##XXXXXXXXXXXXXXXXXXXXXXXXX## "
    print "                                #XXXXXXXX##XXXXXXXXXXXXXXXXXXXXXXXXX### "
    print "                                ##XXXX###XXXXXXXXXXXXXXXXXXXXXXXX##### "
    print "                              ####XXX##XXXXXXXXXXXXXXXXXXXXXXX####### "
    print "                             ##X##XX#XXXXXXXXXXXXXXXXXXXXXXXX####### "
    print "                        #####XXX#XXXXXXXXXXXXXXXXXXXXXXXX########## "
    print "               ##########X##XXXXXXXXXXXXXXXXXXXXXXXXXXX###XXX##### "
    print "         #######XXXXXXXXX##XXXXXXXXXXXXXXXXXXXXXXXXXX###XXX####### "
    print "      ####XXXXXXXXXXXXXX##XXXXXXXXXXXXXXXXXXXXXXXXX###XXXX##XXXXX##### "
    print "      ##XX###############XXXXXXXXXXXXXXXXXXXXXXX###XXXXXX##XXXXXXXXXX##### "
    print "      #####            ##XXXXXXXXXXXXXXXXXXXXX###XXXXXXX##XXXXXXXXXXXXXXX### "
    print "                      ##XXXXXXXXXXXXXXXXXXXX###XXXXXXXX##XXXXXXXXXXXXXXXXXXX### "
    print "                     ##XXXXXXXXXXXXXXXXXXX###XXXXXXXX#######XXXXXXXXXXXXXXXXXX### "
    print "                    ##XXXXXXXXXXXXXXXX#####XXXXXXXX###     ############XXXXXXXXX### "
    print "                   ##XXXXXXXXXXXXX#####XXXXXXXXX###                   ######XXXXXX# "
    print "                   #XXXXXXXXXXX####XXXXXXXXXX####                          ######X# "
    print "                  ##XXXXXXXXX###XXXXXXXXXX####                                  ### "
    print "                 ##XXXXXXXXX##XXXXXXXX##### "
    print "                 #XXXX#XXXX##XXXXXX####                ##### "
    print "                ##XXXXXXXX##XXXXX#####              ####XXX# "
    print "                #XXXXXXXXX#XXXX###XX#             ###XXXX## "
    print "                #XXXXXXXX##XX###XXXX#          ####XXXXXX# "
    print "                #XXXXXXXX#X######XXX#        ###XXXXXXXX## "
    print "                #XXXXXXXX#X#    #####      ###XXXXXXXXXX# "
    print "                #XXXXXXX###        ##    ###XXXXXXXXXXX## "
    print "                #XXXXXXX#X#            ###XXXXXXXXX##### "
    print "                #XXXXXXX###          ###XXXXXXX##### "
    print "                ##XXXXX#X##        ###XXXXXXX### "
    print "                 #XXXXX####   #####XXXXXXXX## "
    print "                 ##XXXXXX######XXXXXXXXXX### "
    print "                 ###XXXXXXXXXXXXXXXXXXX### "
    print "                 #X##XXXXXXXXXXXXXXXXX## "
    print "                ##X####XXXXXXXXXXXXXX## "
    print "                ####  ###XXXXXXXXXXX## "
    print "                ##      ###XXXXXXXX## "
    print "                          #XXXXXXXX# "
    print "                           #XXXXXX## "
    print "                           #XXXXXX# "
    print "                           ##XXXXX# "
    print "                            #XXXXX# "
    print "                            #XXXXX# "
    print "                             #XXXX# "
    print "                             ##XXX# "
    print "                              #XXXX# "
    print "                              ##XXX# "
    print "                               ##XX## "
    print "                                ##XX## "
    print "                                 ##XX# "
    print "                                   ##### "
    print "                                      ##### "
    print "                                        ### "

def gameOver():
  print "Just keep swimming to safety."
  return

def wompWomp():
  print "Where's your sense of adventure?!"
  return

def surfsUp():
  print " You've found your way to the EAC. Time to surf the current with the turtles "

def shipWreck():
  print "You swim toward a wrecked ship that you see in the distance."
  print "You find an open porthole and enter into the dark belly of the ship."
  raw_input("press enter >")

  print "You look around and consider your options."
  print "options: [ look left, look right ]"

  pcmd = raw_input(">")

  if (pcmd == "look left"): 
    print "You see a sign that looks like it says ESCAPE!"
    print "Do you want to escape?"
    print "options: [ yes, no]"
    pcmd = raw_input(">")

    if (pcmd == "yes"): 
      print "You swim out of the exit hatch."
      gameOver()

    else :
      print "options: [ look right, look back]"
      pcmd = raw_input(">")

      if (pcmd == "look right"):
        print "You see a shark!"
        sharkEncounter()
        
      else :
        print "That won't work, there's no exit."
        print "options: [ look right, give up]"
        pcmd = raw_input(">")

        if (pcmd == "look right"):
          print "You see a shark!"
          sharkEncounter()

        else :
          print "Womp Womp"
          wompWomp ()

  else :
    print "You see a shark!"
    sharkEncounter()

            

def sharkEncounter():
  printGraphic ("shark")

  print "Oh no you've accidentally swum into a shark cave"
  print "There is the unmistakable shadow of a shark swimming in the near distance"
  raw_input("press enter >")
  print "options: [ ask for directions, swim away ]"

  pcmd = raw_input(">")

  if (pcmd == "ask for directions"): 
    print "The shark bares its teeth and says..."
    raw_input("press enter >")
    print "Oh Sydney! Of course - you take the EAC straight on into the harbor"
    surfsUp ()

  else :
    print "You swim back to where you entered"
    print "options: [look left, look back]"
    pcmd = raw_input(">")

    if (pcmd == "look left"): 
      print "You see a sign that looks like it says ESCAPE!"
      print "Do you want to escape?"
      print "options: [ yes, no]"

      pcmd = raw_input(">")
                
      if (pcmd == "yes"): 
        print "You swim out of the exit hatch."
        gameOver()

      else :
        print "options: [ look back, give up]"
        pcmd = raw_input(">")
        
        if (pcmd == "look back"):
          print "That won't work, there's no exit."
          wompWomp()

        else :
          print "Womp Womp"
          wompWomp ()

    else :
      print "That won't work, there's no exit"
      wompWomp ()


def introStory():
  # let's introduce them to our world
  print "Welome to the great blue Pacific Ocean"
  print "You're on a journey to save your son, Nemo"
  player["name"] = raw_input("Please enter your name >")

  # intro story, quick and dirty (think star wars style)
  print "You've been swimming for days and come across a big shadow in the distance "
  print "As you swim closer you notice it's actually a giant shipwreck"
  print "Do you want to explore the shipwreck?"

  pcmd = raw_input("please choose yes or no >")

  # the player can choose yes or no
  if (pcmd == "yes"):
      raw_input("press enter >")
      shipWreck()

  else :
      gameOver ()


# main! most programs start with this.
def main():
  printGraphic("title") # call the function to print an image
  introStory() # start the intro

main() # this is the first thing that happens
