#FINAL SUBMISSION NOTES
- This project was developed by Deniz and Kertu 
- The aim of the project was to reproduce a game inspired by Chicken Crossing using Pythong and Processing.py 
  - For that purpose we created our own code as well as designed the graphics for the game (including animated sprites) 
  - All the details can be found from the folders uploaded to this repository, the to-do list and progress can be seen from our commit history and the list further below 
  - Since there was trouble in running the soundfiles using the os.getwd() function, then right now the soundfiles are direted to a specific locaation in a specific computer and hence commented out for the purpose of the code working globally.
  - The aim of the game is to collect lions without colliding with constantly speed-increasing cars and cross the roads safely. 
  - Screenshots of how the game is supposed to look while running have been added to the 'Screenshot folder' 



# Deniz-Kertu-Final-Project
PLAN
- Create the game using basic geometric shapes without the pictures in order to get the general logic 
  - Class for the Creatures /DONE 
  - Making the Player move /DONE 
  - Making the obstacles move /DONE 
  - Continuous generation of cars /DONE
    - Making their speed dependent on score /DONE 
    - Figure out a suitable increasing function to make the game playable for an adequate amount of time/DONE
  - Creating the reappearing food/wamrs /DONE  
  - Collosion /DONE
    - Different outcomes with Food or Cars/DONE
    - Disabling it for the duration of 'fly-back' when the player dies and has to return to the initial position/NO NEED, PROGRAM DOES AUTOMATICALLY 
  - Deleting things that exit the screen to avoid memory overlaod /DONE
  - Creating a scoring system /DONE
  - Creating a lives system /DONE
    - Maybe creating an opportunity to earn extra lives, appearing heart shapes from time to time/IN PROGRESS - future addition 
- Create the framework for the game/DONE
  - Initial screen /DONE
    - Play button /DONE
      - "Please eneter you name: " /NO 
    - Character choice /NO
  - Pause screen /DONE
  - Game over screen/DONE
    - replay option /DONE 
 
- Adding the graphics 
  - Spritesheet for the chicken /FOUND, did not use 
    - Self-made spritesheet for the player from all angles /DONE
  - General Background /DONE, SELF-MADE 
  - Warms and cars/ DONE, self-made 
  
 - Adding audio 
  - Finding soundfiles /DONE 
    - coding the global audio /DOESNT WORK
    - looping the soundfile /DOESNT WORK
