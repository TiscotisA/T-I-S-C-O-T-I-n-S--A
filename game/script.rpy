# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    


define dm = Character ("DM")

label start:
    
    scene mob_image
    
    show wizard dm
    
    play sound "Wild_Battle_Crowd_Approach.mp3"
    
    dm "The Party found themselves at Ari's fort, ready to storm in."
   
    play sound "Fart_Long_through_Door.mp3"
    
    dm "They found a Thug which they fought and eventually subjected to a gruesome execution... by buttocks."
    
    dm "Following the Thug was a man called Francois, who was also subjected to a painful groin attack, courtesy of Albert."
    
    play sound "Magic_Chime.mp3"
    
    dm "However, Ari proceeded to intervene, (annoyingly) stunning the entire party."
    
    stop music fadeout 1.0  #"Wild_Battle_Crowd_Approach.mp3" fadeout 
    
    
    
    dm "He thusly lead the party into his own personal room before assigning them a quest and teleporting them into the catacombs of a neighbouring warlord's fort."
    
    scene bg room
    with dissolve
    
    
    return 

