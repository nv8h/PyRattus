#!/bin/sh

MAINFILE="./base/script/main.py"
BACKUPFILE="./base/script/main.py.bak"

backup()
{
    echo "Create Backup..."
    cp $MAINFILE $BACKUPFILE
}


case $1 in
    "") echo "For information type ratmain --help";;
    "edit")
        backup()
        mcedit ${MAINFILE}
    ;;
    "diff")
        diff $MAINFILE $BACKUPFILE
    ;;
    "restore")
        cp $BACKUPFILE $MAINFILE
    ;;
    "add")
        case $2 in
            "") echo "Usage: ratmain add (mode,def) (name Of mode)";;
            "mode")
                backup()
                echo "    " >> $MAINFILE
                echo "    def ${3}Action(self):" >> $MAINFILE
                echo "        print(\"Welcome to the '${3}' mode!\")" >> $MAINFILE
                echo "        " >> $MAINFILE
                echo "        # return with Error Message" >> $MAINFILE
                echo "        return None" >> $MAINFILE
                echo "${3} mode added to the main.py file"
            ;;
            "def")
                backup()
                echo "    " >> $MAINFILE
                echo "    def ${3}(self):" >> $MAINFILE
                echo "        return None" >> $MAINFILE
                echo "${3} definition added to the main.py file"
            ;;
        esac
        ;;
    "--help")
        echo "ratmain.sh"
        echo "Writed by Schoffhauzer István"
        echo "-------------------------------------------------"
        echo ""
        echo "Edit main: ratmain.sh edit"
        echo "Add mode: ratmain.sh add mode name"
        echo "Add def: ratmain.sh add def name"
        echo "Restore main: ratmain.sh restore"
        echo "Diff main: ratmain.sh diff"
    ;;
esac


