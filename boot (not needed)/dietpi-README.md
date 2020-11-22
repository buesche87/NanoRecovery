<html>
    <p align="center">
        <img src="https://dietpi.com/images/dietpi-logo_150.png">
    </p>
    <h1 align="center">DietPi</h1>
    <p align="center">
        <b>Lightweight justice for your single-board computer!</b>
        <br>
        <br>
        optimised • simplified • for everyone
        <br>
        <br>
        <a href="https://dietpi.com">find out more</a>
        •
        <a href="https://dietpi.com/#download">download image</a>
        <hr>
    </p>
    <p align="center">
        Optional "ready to run" optimised software choices with <b>dietpi-software</b>.
        <br>
        Feature rich configuration tool for your device with <b>dietpi-config</b>.
        <hr>
    </p>
    <p align="center">
        <img src="https://dietpi.com/images/mvs_logo_150.jpg">
        <br>
        <br>
        DietPi's web hosting is powered by
        <a href="https://www.myvirtualserver.com">myVirtualServer</a>.
        <br>
        <br>
        A wide range of SBCs and VMs are supported. <a href="https://dietpi.com/#download">Click here</a> for the full list.
        <br>
        <br>
    </p>
</html>

## Introduction

DietPi is an extremely lightweight Debian-based OS. With images starting at 400MB, that's 3x lighter than 'Raspbian Lite'. It is highly optimized for minimal CPU and RAM resource usage, ensuring your SBC always runs at its maximum potential. The programs use lightweight Whiptail menus. You'll spend less time staring at the command line, and more time enjoying DietPi.

Use `dietpi-software` to quickly and easily install popular software that's "Ready to run" and optimized for your system. Only the software you need is installed. Use `dietpi-process_tool` to control which installed software has higher or lower priority levels (nice, affinity, policy scheduler).

`dietpi-update` automatically checks for updates and informs you when they are available. Update instantly, without having to write a new image. `dietpi-automation` Allows you to completely automate a DietPi installation with no user input, simply by configuring dietpi.txt before powering on.


## The DietPi Project Team

### Lead

**Daniel Knight (Fourdee)**

Creator, programmer and project lead of DietPi.

---

### Current Contributors

#### MichaIng

_Joined Q3 2017_

Source code contributor, bug fixes, software improvements, DietPi forum co-administrator.

#### JohnVick

_Joined 2016-06-08_

DietPi forum co-administrator, management, support, testing and valuable feedback.

#### K-Plan

_Joined 2016-01-01_

Contributions to the DietPi in general, in-depth testing, bug finding and valuable feedback, forum moderator.

#### ZombieVirus

_Joined 2016-03-20_

DietPi forum moderator and version history maintainer on forums.

---

### Collaborations

#### DietPi + AmiBerry

_02/09/2016_

Joint venture to bring you the ultimate Amiga experience on your SBC, running lightweight and optimised DietPi at its core:
https://github.com/Fourdee/DietPi/issues/474

---

### Previous/Inactive Contributors

#### Rhkean

_Joined 2018-03-01_

Contributions to the DietPi in general, including source code, testing, new devices, forum moderator.

#### Pilovali

_Joined 2015-10-10_

Provided DietPi.com web hosting for 1 year until April 17th 2016. Additionally: forum moderator, testing, bug reporting.

#### xenfomation

_Joined 2016-04-01_

Contributions to the DietPi in general, including source code and VirtualBox image creation/conversion.

#### AWL29

_Joined 2016-10-01_

Created the DietPi image for NanoPi M3/T3.

---

### Honourable Mentions/Thanks

A personal thanks to **Pilovali** for helping DietPi during our early days with desperately needed web hosting.

---

## Contributing

Git coders, please use the active development branch: [`dev`](https://github.com/Fourdee/DietPi/tree/dev)

* [How to add new software installation options to DietPi-Software](https://github.com/Fourdee/DietPi/issues/490#issuecomment-244416570)

Are you able to:

* Provide feedback and/or test areas of DietPi, to improve the user experience?
* Report bugs?
* Improve/add more features to the [DietPi website](https://dietpi.com)?
* Compile software for Odroid C1 and RPi systems?
* Contribute to DietPi with programming on GitHub?
* Suggest new software that we can add to the `dietpi-software` install system?

If so, let us know!
We are always looking for talented people who believe in the DietPi project, and, wish to contribute in any way you can.

* Send me an Email: daniel.knight@dietpi.com
* Join our forums: https://dietpi.com/phpbb
* GitHub: https://github.com/Fourdee/DietPi

## License

DietPi Copyright (C) 2016 Daniel Knight
* Email daniel.knight@dietpi.com
* Web https://dietpi.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/

## Links

### DietPi Source

- Source: https://github.com/Fourdee/DietPi
- Build: Not applicable (as DietPi currently uses Bash scripts, no building or compiling is required).

### DietPi file list


- All files located in `/DietPi/dietpi` (recursive)
- `/DietPi/dietpi.txt`
- `/DietPi/config.txt`
- `/DietPi/boot.ini`

> The above GPLv2 documentation also applies to all mentioned files!

### Additional Software

Links to additional software used in DietPi and their source and build instructions (where applicable):

- [Raspberry Pi](https://github.com/raspberrypi)
- [Odroid](https://github.com/hardkernel?tab=repositories)
- [FriendlyARM](https://github.com/friendlyarm?tab=repositories)
- [LXDE](https://github.com/LXDE)
- [Kodi / Xbmc](https://github.com/xbmc/xbmc)
- [Transmission](https://transmissionbt.com/download/)
- [Nextcloud](https://github.com/nextcloud/server)
- [ownCloud](https://github.com/owncloud/core)
- [MiniDLNA](https://sourceforge.net/p/minidlna/git/ci/master/tree/)
- [MPD](https://github.com/MusicPlayerDaemon/MPD)
- [YMPD](https://github.com/notandy/ympd)
- [PHPBB](https://github.com/phpbb/phpbb)
- [Apache2](https://github.com/apache)
- [MariaDB](https://github.com/MariaDB)
- [PHP](https://git.php.net/)
- [PhpMyAdmin](https://github.com/phpmyadmin)
- [Proftpd](https://github.com/proftpd)
- [Samba](https://wiki.samba.org/index.php/Using_Git_for_Samba_Development)
- [NoIp2 Client Binary](https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client/)
- [RetroPie Setup Script](https://github.com/petrockblog/RetroPie-Setup)
- [PiVPN VPN Server](https://github.com/pivpn/pivpn)
- [OpenTyrian](https://bitbucket.org/opentyrian/opentyrian/wiki/Home)
- [DietPiCam](https://github.com/Fourdee/RPi_Cam_Web_Interface)
- [PHP OPcache GUI](https://github.com/amnuts/opcache-gui)
- [Nginx](https://hg.nginx.org/nginx/)
- [Deluge](https://dev.deluge-torrent.org/wiki/Development#SourceCode)
- [Grasshopper](https://sourceforge.net/projects/grasshopperwebapp/Grasshopper)
- [Pi-hole](https://github.com/pi-hole/pi-hole)
- [SubSonic](https://sourceforge.net/projects/subsonic/)
- [SqueezeBox](https://github.com/Logitech/slimserver)
- [Ampache](https://github.com/ampache/ampache)
- [FFmpeg](https://github.com/FFmpeg/FFmpeg)
- [CertBot](https://github.com/certbot/certbot)
- [Shairport-Sync](https://github.com/mikebrady/shairport-sync)
- [OpenVPN](https://github.com/OpenVPN)
- [FreshRSS](https://github.com/FreshRSS/FreshRSS)
- [Folding@Home](https://github.com/FoldingAtHome)
- [OpenBazaar](https://github.com/OpenBazaar/openbazaar-go)
