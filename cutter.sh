#!/bin/bash
# $ ls
#   so_intimate_40_small.png
# $ cutter.sh so_intimate_40_small
# .......
# $ Done
# $ ls out/


for i in 0 1 2 3 4 5 6 7 8 9; do
    for j in 0 1 2 3 4 5 6 7 8 9; do
        let x=$((i * 100))
        let y=$((j * 100))
        name="out/$1""_""$i""_""$j.png"
        echo "created "$name
	      convert $1'.png[100x100+'+$y+'+'+$x+']' $name
    done
done

echo "Done."
