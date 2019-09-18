#External Softwares/Websites used:
- Photoshop CC
- Audacity
- Photopea: https://www.photopea.com/
- EZGIFCOM: https://ezgif.com/split


#Images/Sounds Credits

ALL Narrations: Text-to-Speech with https://www.naturalreaders.com/

Start Menu Background: Image in https://phys.org/news/2015-09-scientists-successfully-genes-dengue-fever.html
Start Menu Song: World of Warcraft - Legends of Azeroth
Start Menu Button Sound: https://www.youtube.com/watch?v=HCqRNkiE0lI 00:00 - 00:02

Opening Door Sound: http://www.orangefreesounds.com/wooden-door-opening-sound-effect/
Opening Door Gif: https://gfycat.com/gifs/detail/gentleclearcutcockatiel

Win Menu Song: Xenoblade Chronicles 2 - Tiger! Tiger! Level D
Win Menu Reward/Coin Sound: https://freesound.org/people/sharesynth/sounds/344520/

Lose Menu Sound: Bomberman NES - Game Over
Lose Menu Image: https://www.pinterest.com/pin/235805730460819010/

Mosquito Sprites Taken from "Dark Wolf"
Heart Icon : https://www.heypoorplayer.com/2014/06/20/pixilated-heart-emotional-impact-video-games/
Mosquito Hunt Background: https: //www.wallpapermaiden.com/wallpaper/8635/dark-forest-path-trees-leaves-mist-plants/download/1280x720

Main Menu Background : https://www.unrealengine.com/marketplace/medieval-tavern
Main Menu NPC/Human Sprites Taken from http://nn.ai4rei.net/dev/npclist/?qq=8
Main Menu Soldier/Fighter Sound Taken from - Blizzard's Hearthstone - Silver Hand Recruit

Shop Menu Backgronund: https://wallpaperscraft.com/download/boards_wooden_surface_background_texture_50684/1280x720

Hand Smack Sound : http://soundbible.com/441-Smack.html

Coin Image: http://www.psdgraphics.com/psd-icons/psd-gold-coin-icon/
Mosquito on coin: https://clip2art.com/explore/Shadow%20clipart%20mosquito/
Arrow button: https://www.iconfinder.com/icons/49816/arrow_left_icon
Money bag: https://www.iconfinder.com/icons/1543380/bank_game_money_moneybag_pouch_purse_sack_icon
Chest: https://www.123rf.com/photo_84064130_stock-vector-video-game-treasure-chest-with-many-gold-vector-illustration.html
Stopwatch PowerUp: https://www.vectorstock.com/royalty-free-vector/the-5-seconds-minutes-stopwatch-icon-clock-and-vector-11400734
Slow PowerUp: http://hurleylibrary.org/snowflake-png-5/

Hand Image: http://worldartsme.com/neutral-hand-clipart.html#gal_post_76120_neutral-hand-clipart-1.jpg
Flame hand: https://www.canstockphoto.com/fire-hand-6922583.html
Green Hand: http://worldartsme.com/green-hand-clipart.html#gal_post_54331_green-hand-clipart-1.jpg

Black ticket: https://www.iconsdb.com/black-icons/ticket-icon.html
Lock Image: https://pngtree.com/free-png-vectors/chain-lock
Evil cat: https://techflourish.com/categories/evil-dog-clipart.html
Boss transition: https://tenor.com/search/sharingan-kamui-gifs

Sound when not enough cash: https://www.youtube.com/watch?v=lSlTdQFYLA4
Sound when item purchased: https://www.youtube.com/watch?v=WOLmd0ZIPBY
Fire sound: https://www.youtube.com/watch?v=1BdIaaH5VnQ

Battle music: Final Fantaasy IV DS - Battle Theme
Main Menu: Chrono Trigger - Wind Place
Poison Gas Sound: https://www.youtube.com/watch?v=WNveatekvd0
Boss Music: Chrono Trigger - Boss Battle 2

Boss Ship: "Epoch" Taken from Chrono Trigger
#References:

https://www.pygame.org/docs/
https://www.reddit.com/r/pygame/comments/42ydpg/python_how_to_create_a_simple_text_animation/
https://stackoverflow.com/questions/40899850/pygame-lag-when-blitting-background
https://stackoverflow.com/questions/8205807/how-to-convert-a-text-file-into-a-list-in-python

#Project Report

Oct 4 - Created the initial mosquito class and sprite, including its random movement and background.

Oct 6 - Made the mosquito clickable, and sets a win message and stops the game if successfully clicked.

Oct 9 - Created the start menu for the game.

Oct 20 - Created the Hand class and "created" a custom cursor by making the actual cursor invisible.

Oct 23 - Wanted to find out how to blit letter by letter to the screen.
	 https://www.reddit.com/r/pygame/comments/42ydpg/python_how_to_create_a_simple_text_animation/


Oct 24 - Focused mainly on creating sound effects for all the menus Have done thus far, reworked the starting menu
	 and created set sprites for the main menu.

Oct 25 - Started creation and completed the stage select menu.

Oct 26 - Had an issue with lag while blitting multiple items to the screen
	 https://stackoverflow.com/questions/40899850/pygame-lag-when-blitting-background

	 A comment on the page suggested ".convert_alpha", which converts pixels in the image to the proper	
	 format for easier blitting.

Oct 27 - Finished in creating the mosquito health icon and the timer for the "Hunting" session of the game.


Oct 29 - Started creating functions to check if it is the user's first time by creating a text file for Saved Data.
	
	 Wanted to convert the text file into the list.

         https://stackoverflow.com/questions/8205807/how-to-convert-a-text-file-into-a-list-in-python
	
	 A comment on the post had an easy way of creating it into not exactly a list, but a 2D array instead.
	 Successfully made the damage on the mosquito dependent on the hand power.
	 Finished the gold system, and updating the data instantly on the txt file.


Oct 30 - Started creating the initial merchant menu to access the inventory and shop.
	 
	 Added an arrow button on the stage select and merchant menu to return back to the main menu.	

Nov 4 - Created the icons for the shop feature and the inventory feature, started creation of the shop menu

	Finished creating the icons for all the purchasable/upgradable items/hands.

Nov 5 -  Added the boss ticket icon into the shop.
	 
	 Completed the shop system.	
	 Completed the shop menu and created a purchase confirmation screen, displaying details of purchase.
	 Started creation of inventory system.

Nov 6 -  Finished creating the inventory, user can now change to the desired Hand when clicking on it.
	 Inventory displays the number of powerups the user has.
	 Successfully implemented the power up uses into the mosquito hunt battle.

Nov 7 -  Successfully created and completed abilities for both the "Flame Hand" and the "Toxic Hand.
	 Added sounds to a merchant click.

Nov 9 -  Created and completed the "Invader" mode for the boss battle.

Nov 10 - Successfully mixed the Mosquito hunt and "Invader" mode together.
	 
	 Successfully linked a character in the main menu to the boss battle.

Nov 13 - Changed the colours in the purchase confirmation screen.
	 
	 Made the code for the mosquito hunt and the shop functions more efficient to reduce lag in the screen 
	 during the functions running.
	 
	 Remade the main menu screen to make the menu less laggy and made it easier for new users to identify
	 the different menus.


Nov 15 - Looked for and added necessary sound effects into the game.

Nov 16 - Looked for and added music into the main menu, mosquito hunt and boss battle.
	 