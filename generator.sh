#!/bin/bash

# old line
# th neural_style.lua -gpu -0 -image_size 1000 -optimizer adam -backend cudnn -num_iterations 2000 -content_image in/comp12_inv.jpg -style_image in/so_intimate_40_small.jpg -output_image out/comp12_inv_sointimate40_.png
for i in 0 1 2 3 4 5 6 7 8 9; do
    for j in 0 1 2 3 4 5 6 7 8 9; do
        let x=$((i))
        let y=$((j))
        comp5="in/comp5_081_$x""_""$y.png"
        echo $comp5
        sointimate="in/so_intimate_40_small_$x""_""$y.png"
        echo $sointimate
        outname="out/comp5_so_intimate_40_small_$x""_""$y.png"
        th neural_style.lua -gpu -0 -image_size 100 -optimizer adam -backend cudnn -num_iterations 1000 -content_image $comp5 -style_image $sointimate -output_image $outname
    done
done
#th neural_style.lua -gpu -0 -image_size 500 -optimizer adam -backend cudnn -num_iterations 2000 -content_image in/comp5_081.jpg -style_image in/so_intimate_40_small.jpg -output_image out/comp12_inv_sointimate40_.png
