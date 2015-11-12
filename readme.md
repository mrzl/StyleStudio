a collection of some tools to use the style transfer from
https://github.com/jcjohnson/neural-style/ on a remote host.

due to memory problems, content and style images need to be
cut into tiles in order to process them after another.

### cutter.py
cuts image into pieces

```
# $ ls
#   so_intimate_40_small.png
# $ cutter.sh so_intimate_40_small
# .......
# $ Done
# $ ls out/
```

### generator.sh
takes cut pieces and creates a massive torch batch

### get.py
loads done images from the server

### up.py / up_many.py
sends single images or multiple images to the host

### stitch.sh
stitching tiles back together
