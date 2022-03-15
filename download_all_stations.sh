#!/bin/bash

# Old stations
# "20002" "20003" "20043" "20047" "20049" "20101" "20102" "20252" "20253" "20262" "20299" "20301" "20302" "20303" "20333" "20412" "20423" "20566" "20567" "20676" "21009" "21011" "21058" "21138" "21191" "22009" "22058" "22059" "22121" "22122" "22331" "22333" "22598" "22599" "23126" "23128" "23132" "23259" "23289" "23293" "23322" "24006" "24007" "24018" "24032" "24053" 

declare -a StringArray=("24122" "24125" "24123" "24124" "24132" "24328" "24342" "24343" "24344" "24353" "25137" "25147" "25149" "25343" "25344" "25346" "25347" "26088" "26089" "26136" "26137" "26143" "26144" "26239" "26346" "26359" "26361" "26457" "26459" "26473" "26474" "27000" "27014" "27084" "28003" "28004" "28068" "28086" "28087" "28198" "28199" "28234" "28366" "28367" "28397" "28398" "28548" "29002" "29006" "29014" "29038" "29039" "29141" "29393" "29394" "30017" "30042" "30106" "30112" "30119" "30121" "30129" "30202" "30203" "30336" "30357" "30361" "30363" "30396" "30407" "30409" "30478" "30479" "31063" "31171" "31172" "31243" "31244" "31342" "31343" "31417" "31418" "31463" "31473" "31478" "31493" "31494" "31573" "31616" "32048" "32096" "32098")

#parallel -j4 'echo python3 "{}"' ::: "${StringArray[@]}"	

for station in  ${StringArray[@]}; do
	echo $station
	python3 water_level.py "$station" 01-01-1990 01-01-2019	
done