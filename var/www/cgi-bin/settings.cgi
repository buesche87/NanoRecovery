#!/bin/sh
echo "Content-type: text/html\n"

# read in our parameters
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

# our html header
echo "<html>"
echo "<head><meta name='viewport' content='width=device-width, initial-scale=1' /><title>NanoHome Recovery Mode</title> <link rel='stylesheet' type='text/css' href='style.css'></head>"
echo "<body>"
echo "<div style='text-align: center;'>"
echo "<div style='display: inline-block; text-align: left;'>"

if [ $CMD ]
then
  case "$CMD" in

    Backup)
      echo "<center>System-Backup<hr></center><pre>"
	  sudo system-backup
      echo "</pre>"
	  echo "This can take up to 30 minutes and more..."
    ;;

    Restore)
	  echo "<center>System-Restore<hr></center><pre>"
      sudo system-restore
      echo "</pre>"
	  echo "This can take up to 30 minutes and more..."
    ;;

    Check)
	  echo "<center>Check Backup<hr></center><pre>"
      sudo check_backup web
      echo "</pre>"
    ;;

    Mount)
	  echo "<center>Mount emmc<hr></center><pre>"
      sudo mount_emmc root
      echo "</pre>"
    ;;

    Unmount)
	  echo "<center>Unmount emmc<hr></center><pre>"
      sudo mount_emmc unmount
      echo "</pre>"
    ;;

    Update)
	  echo "<center>Update NanoHome<hr></center><pre>"
      sudo nanohome_update
      echo "</pre>"
    ;;

    Logfile)
	  echo "<center>Check Update<hr></center><pre>"
      sudo cat /boot/update/nhupd.log
      echo "</pre>"
    ;;

    Reboot)
      echo "<center>Reboot...</center>"
      sudo systemctl reboot
      echo "</pre>"
    ;;

    Shutdown)
      echo "<center>Shutdown...</center>"
      sudo shutdown -h now
    ;;

     *)
       echo "<center>Unknown command $CMD<br></center>"
       ;;
      esac
    fi

    echo "</div>"
    echo "<hr>"
    echo "</div>"


    # print out the form

    # page body

	echo "<center>"
	echo "NanoHome Backup & Restore"
	echo "<p>"

    echo "<form method=get>"
    echo "<p>"
    echo "<input type=submit name=cmd style='background-color: #c0fcb1; color: black;' value='Check'>"
    echo "<input type=submit name=cmd style='background-color: #fff4bd; color: black;' value='Backup'>"
    echo "<input type=submit name=cmd style='background-color: #ffbdbd; color: black;' value='Restore'>"
    echo "</form>"

    echo "<form method=get action='/cgi-bin/nanohome_backup.img'>"
    echo "<p>"
    echo "<input type=submit name=cmd style='background-color: #c0fcb1; color: black;' value='Download'>"
    echo "</form>"
    echo "<hr>"

	echo "Update NanoHome"
	echo "<p>"

    echo "<form method=get>"
    echo "<p>"
    echo "<input type=submit name=cmd style='background-color: #ffbdbd; color: black;' value='Update'>"
    echo "<input type=submit name=cmd style='background-color: #c0fcb1; color: black;' value='Logfile'>"
    echo "</form>"
    echo "<hr>"

	echo "Mount emmc"
	echo "<p>"

    echo "<form method=get>"
    echo "<p>"
    echo "<input type=submit name=cmd style='background-color: #ffbdbd; color: black;' value='Mount'>"
    echo "<input type=submit name=cmd style='background-color: #fff4bd; color: black;' value='Unmount'>"
    echo "</form>"
    echo "<hr>"

	echo "Power"
	echo "<p>"

    echo "<form method=get>"
    echo "<p>"
    echo "<input type=submit name=cmd style='background-color: #fff4bd; color: black;' value='Reboot'>"
    echo "<input type=submit name=cmd style='background-color: #ffbdbd; color: black;' value='Shutdown'>"
    echo "</form>"

	echo "</center>"
    echo "</body>"
    echo "</html>"

