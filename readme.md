Before use
=======
1 - this program doesn't have any signiture, so If the antivirus program blocks the program, please allow it.

2 - this program will require internet connection.(DB download and Log upload)

3 - you can upload log to internet. This method is similar to hugslib.

you can see log at https://gist.github.com/RAMSlog

log will collect:
- compare your local/workshop mod with DB, and record which is not on the DB.
*******
HOW-TO-USE
=======
always use latest version!
0. Always read terminal log
1. pop-up will ask you to select ModConfig.xml file
you can find it in "your USERNAME\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Config" (default path)
2. another pop-up will ask you to select Rimworld Local mod folder
select 'Mods' folder located in your Rimworld folder
3. type Y or N to load workshop mod, or not(for DRM-free version)
4. if you press Y, and another pop-up will show, and ask you to select rimworld Workshop mod folder
you should select folder named '294100' in your steam/steamapps/workshop/content
5. follow terminal
*********
Screenshots
========

temporary removed

HOW-TO use DB updater(temporary removed)
=============

I included DB updating tool if the user wants to contribute to DB.

you can found folder named "template updater"

run  "Launch template_updater.bat" (don't run tetmplate_updater.exe)

after you run it, terminal will ask you to type Y or N (if screen freezed, press enter few times.)

type Y to start work, type N to exit program.


a window will pop up asking you to locate "Rimworld64Win.exe"

find rimworld64win.exe and it will download DB from github, and show your all mods from workshop and local.

and remove overlapping mods from list.


then you'll see, you need to input number one of 1 to 20.

if you type P, you can pass that mod if you can't sure. press X to stop the program and save.


*****

important : this number support Prime number. you can use it!

0 to 1. Mod manager, MOD-E, BetterLoading and other mods that should be loaded before Core.
1. Core

2.Hugslib only

2.xx. RuntimeGC

3~6. other mod's Core, framework, library mod
(example: giddy up! core, alien race framework 2.0, advanced animal framework)

7~8 hugslib mod
mod that need hugslib.


9~12 Large-scale mod and sub mod of that mod

example : Rimsennal, EPOE
explain : Hospitality is a large-scale mod, but it hugslib-require mod. so it will go to 7~8.

Race add mod : go to 9~12 if it have any dependency relation. go to 13 if it doesn't have any.

13. Hair/trait/story teller/faction add

14~15. item/terrain/object/simple mod like add animals.
15. simple mod or mods that don't modify mod many.

15~16. mod that affact AI behavior
example: haul to stack, while you're up

17. interface / user convenience

18~ always load last
*****

I'll show you an example.

if you're trying to add mod "Megafuana", what you should do?
first. always read steam mod dscription page unless you know very well about the mod.
(if the mod is very simple, or don't modify game too much, you can just guess it. like 'simple stockpile presets', or 'simple bulk cooking'.)

https://steamcommunity.com/sharedfiles/filedetails/?id=1055485938&searchtext=megafauna

the description says:

>Megafauna will automatically detect and patch both A Dog Said... by >SpoonShortage (so you can cure old wounds of your animals and >install bionic parts on them) and Giddy-up! by Roolo (which means >that you can ride your animals!), so make sure to make it load after >those mods.


nothing refer to mod conflict, and no hugslib require. and always put mod under 'A dog said...' and 'Giddy up! core'
'A dog said...' is the Core mod in other mod. so it will be in 3 to 6.
and also giddy-up! core is the Core mod. so it will be in 3 to 6.
so finally, this mod add lots of animals, but it doesn't modify game too much. so 'Megafuana' will get 14 to 15.

if you have trobule when you add sub mod. you can use PRIME NUMBER to add it.
example:
Rimsenal is a huge mod, so it will be in 9 to 12. (it is core mod so It should be set close to 9.)
"rimsenal : federation", "rimsenal : feral" is a sub-mod of Rimsenal Core.
so it will go to 9.1, 9.2, 9.xx or 10.(It is actually in 10.)

if you adding mod that requires hugslib. read this
let's say A is a hugslib-require mod that doesn't need other mods. B is also a hugslib-require mod but it needs other mods.(sub-mod).
and X is the core mod that B needs it.
currently X is assigned to '10.0'

first, choosing number for A. ignore other considerations and put it to 8. unless it needs to go to specific order.
second, B is also hugslib so it should go to 7 or 8. but it needs X and it is on 10.
so you should assign B to 10.xx or 11to.

after you finished, or saved, you can test your order by using 'mod sorter by local.bat'







