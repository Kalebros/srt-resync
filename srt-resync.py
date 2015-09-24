#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from datetime import timedelta

#Process a timeline to obtain a timedelta
def processTimeLine(timeLine):
    timeList=timeLine.split(':')
    seconds=timeList[-1].split(',')[0]
    microseconds=timeList[-1].split(',')[-1]
    deltaRes=timedelta(hours=int(timeList[0]),minutes=int(timeList[1]),seconds=int(seconds),microseconds=int(microseconds))
    return deltaRes

def formatTimeLine(timeLine):
    mSeconds=timeLine.microseconds
    compensateTime=timeLine-timedelta(microseconds=mSeconds)
    srtLine=str(compensateTime)
    srtLine='0'+srtLine
    sMSeconds=str(mSeconds)
    if len(sMSeconds) > 3:
        sMSeconds=sMSeconds[:3]
    srtLine+=(','+sMSeconds)
    return srtLine

#Read a file
if len(sys.argv) < 4:
    print 'ERROR: Missing arguments'
    print '------------------'
    print 'USAGE: '+sys.argv[0]+' <SRT file> <SRT dest file> <resync>'
    print '--'
    print 'SRT file: SRT file to resync'
    print 'SRT dest file: SRT file resynced'
    print "resync: Time (in seconds and float format) we need to add (or rest) to the subtitles's timestamps; can be a negative value"
    sys.exit()

srtFile=open(sys.argv[1])
srtDestiny=open(sys.argv[2],'w')

for srt in srtFile:
    if '-->' in srt:
        #Process timedelta
        times=srt.split('-->')
        initialTime=processTimeLine(times[0])+timedelta(seconds=float(sys.argv[3]))
        lastTime=processTimeLine(times[-1])+timedelta(seconds=float(sys.argv[3]))
        srtDestiny.write(formatTimeLine(initialTime)+' --> '+formatTimeLine(lastTime)+'\n')
    else:
        srtDestiny.write(srt)

print "Srt RESYNC!"
