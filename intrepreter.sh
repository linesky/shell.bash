tmps2=$1 $2 $3 $4 $5 $6 $7 $8 $9
while IFS= read -r l1
do
$l1
done < "$tmps2"
