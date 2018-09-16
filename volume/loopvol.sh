for pdbid in $*
do
	#bash clean.sh
	bash myquickstart $pdbid > mybuffer
	val=$(tail -n 1 mybuffer | awk '{print $3 " "  $4 " " $6}'|cut -d '-' -f 1)
	echo $val >> volumeinfo.txt
done
