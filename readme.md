a collection of some tools to use the style transfer from
https://github.com/jcjohnson/neural-style/ on a remote host.

due to memory problems, content and style images need to be
cut into tiles in order to process them after another.

### cutter.sh
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

### get_from_server.sh
loads done images from the server

### send_to_server.sh
sends cut images to the server

### stitch.sh
stitching tiles back together
