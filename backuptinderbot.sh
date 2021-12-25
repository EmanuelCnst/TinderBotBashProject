#!/usr/bin/bash

# =========================================================
#                      Backup Tinder Bot 
# =========================================================
#  Progam       : /home/constanti/Workspace/TinderBotEmanuel
#  Autor        : Emanuel Constanti Robin Zweifel
#
#  Created      : 25.12.2021
#
#  Description  : Backup Tinder Bot Script via SMTP and start via Cron Job
#
#  Arguments    : 
#
#  Startup      : /home/constanti/Workspace/TinderBotEmanuel 
#
#  -----------------------------------------------------------------------------------------------------
#
#  History
#  *******
#
#  Release  Date        Modification     User
#  """""""  """"        """"""""""""     """"
#  0.1      25.12.2021   Created         EC RZ
#
#
# ======================================================================================================
#-----------------------------------------------------------------
# Anzahl Argumente pruefen
#-----------------------------------------------------------------
#-----------------------------------------------------------------
# Environment und Variablen
#-----------------------------------------------------------------

DATUM=`date +%d%m%y%n`
ZEIT=`date +%H%M%S`
AN="constanti_99@hotmail.com"
LOGFILE=/home/constanti/Backup/Log/backup.log


RC=0

echo "Start Tinder bot Backup `hostname` `date`"
echo "-----------------------------------------------------------------"
echo " Report Backup "
echo "-----------------------------------------------------------------"

for line in $(find /home/constanti/Workspace/TinderBotEmanuel -mtime -1 -type f)

do
cp $line /home/constanti/Backup
echo " file copied: " $line
done

RC=$? 


#-----------------------------------------------------------------
# Kontrolle Backup und Alarmierung
#-----------------------------------------------------------------

if test $RC -ne 0

then
        echo "Return-Code: $RC"
        echo "ERROR Failed to backup tinderbot on `hostname` `date`"
        mailx -s "Warning: ERROR Tinder Backup Failed on `hostname` `date`" $AN < $LOGFILE 
else
        echo "Return-Code: $RC"
        echo "Successful Backup on Tinder Bot on `hostname` `date`"
        mailx -s "Successful Backup on Tinder Bot on `hostname` `date`" $AN < $LOGFILE 
fi

#-----------------------------------------------------------------
# Logfile kopieren
#-----------------------------------------------------------------

if [ -f $LOGFILE ] ; then
        cp -p $LOGFILE $LOGFILE.$DATUM.$ZEIT
fi
