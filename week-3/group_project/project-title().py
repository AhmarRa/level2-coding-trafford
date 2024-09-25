import time
import os

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_large_title(title):
    # Define a simple ASCII art for the game title
    ascii_art = r"""

  ###    ##   ##  #######   #####   ########           #####   #######           ########  ##  ##  #######           
 ## ##   ##   ##   ##   #  ##   ##  ## ## ##          ### ###   ##   #           ## ## ##  ##  ##   ##   #           
##   ##  ##   ##   ##      ##          ##             ##   ##   ##                  ##     ##  ##   ##               
##   ##  ##   ##   ####     #####      ##             ##   ##   ####                ##     ######   ####             
##   ##  ##   ##   ##           ##     ##             ##   ##   ##                  ##     ##  ##   ##               
 ## ##   ##   ##   ##   #  ##   ##     ##             ### ###   ##                  ##     ##  ##   ##   #           
  ####    #####   #######   #####     ####             #####   ####                ####    ##  ##  #######           
     ##                                                                                                              
####      #####    #####   ########          ### ###   ######  ##   ##   #####   #####     #####   ##   ##   #####   
 ##      ### ###  ##   ##  ## ## ##           ## ##      ##    ###  ##  ##   ##   ## ##   ### ###  ### ###  ##   ##  
 ##      ##   ##  ##          ##              ####       ##    #### ##  ##        ##  ##  ##   ##  #######  ##       
 ##      ##   ##   #####      ##              ###        ##    #######  ## ####   ##  ##  ##   ##  ## # ##   #####   
 ##      ##   ##       ##     ##              ####       ##    ## ####  ##   ##   ##  ##  ##   ##  ##   ##       ##  
 ##  ##  ### ###  ##   ##     ##              ## ##      ##    ##  ###  ##   ##   ## ##   ### ###  ##   ##  ##   ##  
#######   #####    #####     ####            ### ###   ######  ##   ##   #####   #####     #####   ### ###   #####

    """
    print(ascii_art)
    time.sleep(5)  # Display the title for 5 seconds

def print_story():
    story_lines = [
        "Oh heroes of the Kingdom of Gdom, you have been summoned by the King.",
        "Your quest is to defeat the Evil Sorcerer who threatens our way of life.",
        "",
        "You must go to the North World and recover the Amulet of Light.",
        "You must go to the South World and recover the Sword of Destiny.",
        "You must go to the East World and recover the Shield of Hope.",
        "And you must go to the West World and recover the Helm of Power.",
        "Only then should you proceed to the Centre World where you must face the Evil Sorcerer.",
        "It is only with these powerful relics will you have the necessary tools that can defeat Evil.",
        "",
        "Our fate rests in your hands", 
        "Do not fail us."
    ]
    
    for line in story_lines:
        print(line)
        time.sleep(3)  # Wait for 3 second before printing the next line

# Directly call the main function
clear_screen()
print_large_title("Quest of the Lost Kingdoms")
print_story()
clear_screen()
