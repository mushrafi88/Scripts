#!/bin/bash


cd /mnt/study/Second_year
curr_choose=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
[[ -z $curr_choose ]] && exit

if [[ -d $curr_choose ]]; then
	cd "$curr_choose"
	new1=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
	[[ -z $new1 ]] && exit
	if [[ -d $new1 ]]; then
		cd "$new1"
		new2=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
		[[ -z $new2 ]] && exit
		if [[ -d $new2 ]]; then
			cd "$new2"
			new3=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
			[[ -z $new3 ]] && exit
			if [[ -d $new3 ]]; then
				cd "new3"
				new4=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
				[[ -z $new4 ]] && exit
				if [[ -d $new4 ]]; then
					cd "$new4"
					new5=$(ls -d */ *.pdf | rofi -dmenu -p "Bookmarks:")
					[[ -z $new5 ]] && exit
					if [[ -d $new5 ]]; then
						exit
					else
						okular "$new5"
					fi
				else
					okular "$new4"
				fi
			else 
				okular "$new3"
			fi
		else
			okular "$new2"
		fi
	else
	    okular "$new1"	
	fi
else
	okular "$curr_choose"
fi	