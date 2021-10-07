#!/usr/bin/bash

#change to appropriate direectory
location="/home/naman/Pictures/wallpapers"

function get_photo()
{
    val=( "$location"/* )
    echo "${val[RANDOM % ${#val[*]}]}"
}

function set_wallpaper()
{
    wallpaper="$*"
    echo "setting background to $wallpaper"
    gsettings set org.gnome.desktop.background picture-uri "file://$wallpaper"
}

while true
do
    wp=$(get_photo)
    set_wallpaper $wp
    sleep 10 #change to needed time
done
