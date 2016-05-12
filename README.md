<p align="center">
  <b> [MATERIAL *NIX](https://github.com/material-nix)</b><br>
  <a href="#">[Rollo](https://github.com/material-nix/rollo)</a> |
  <a href="#">[Munchy](https://github.com/material-nix/munchy)</a> |
  <a href="#">[Burst](https://github.com/material-nix/burst)</a>
  <br><br>
  <img src="https://github.com/MATERIAL-NIX/Resources/blob/master/Images/MaterialNix-Logo-Circle.png">

### About
<b>(Rollo)</b> Material Design inspired Icon theme for Linux from the [Material*Nix project](https://github.com/material-nix). This readme provides information on installation, icon requests and hardcoded icons. Licensed under the GPL-3.0+

### Installation
##### Building from Source

You can build and install the Material*Nix icon theme from source:

    ./autogen.sh
    make
    sudo make install

This procedure requires ```autotools``` on your system.

##### Installing using Script

Alternatively you may install Rollo with the provided installation script:

    ./install-icon-theme.sh
    

#####Manually

 - Navigate to the directory which contains the icon pack and extract it. 
  <b>Example:</b> /home/user/downloads/material-nix/rollo.tar.gz.
 - Move the extracted folder containing the icons to either ~/.icons or ~/.local/share/icons (user only) or to /usr/share/icons (systemwide).
 - Optional: run gtk-update-icon-cache -f -t ~/.icons/<theme_name> to update the icon cache.
 - Select the icon theme using the appropriate configuration tool for your desktop environment or window manager.

### Icon Requests
When filing an icon request or reporting a missing icon, please take care in providing the following useful information: 

 - A screenshot of your issue or an image of the original icon you are requesting to be themed
 - The file name for the missing icon or the requested icon, for example `gimp.png` or `system-shutdown.svg`
 - A short description of the application or software that you are requesting an icon for.
 - For normal applications follow [this usefull tutorial](https://plus.google.com/+NumixprojectOrg/posts/DkRmhFZuWez)
 - For Steam games follow [this usefull tutorial](https://www.youtube.com/watch?v=BuUy4CzCoXc)
 - For Chrome apps just post a link to the webstore page. 

<b>Note:</b> Please be respectful, patient, and remember that development is done solely by myself.

### Hardcoded Icons
<b>Note:</b> Some software ships hardcoded icons, meaning when you install icons are not placed in the system-wide directory `/usr/share/icons` which makes them unthemeable.

To deal with hardcoded application icons Material*Nix uses the [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) script. A list of the applications supported by the script can be found [here](https://github.com/Foggalong/hardcode-fixer/wiki/App-Support).

### Credits
Theme inspired By and aiming to adhere to Google's Material Design product icon [guidlines](https://www.google.com/design/spec/style/icons.html#).

Icons are designed and developed by Adam Harley

All Scripts are forks of [Paper](https://github.com/snwh/paper-icon-theme) Icon theme By [Sam Hewitt](https://github.com/snwh)

Official webpage: OnMyToDoList...com

### Links
  * [Deviantart](http://le-3.deviantart.com/)
  * [Google+](https://plus.google.com/u/0/communities/103720848213793037553)

===================
