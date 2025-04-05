# via-swap.py

This python script is used to flip VIA keyboard layouts. ie. layouts saved by the (https://usevia.app/)[VIA program].

It is intended to be used with split keyboards, such as the lily58 keyboard, which have micro-controllers on both halves of the keyboard.

Those keyboards often treat the micro-controller which is plugged into the USB port of your computer as the "left" half, regardless of which side of the keyboard it really is. So if you plug in the right micro-controller, the layout ends up being reversed.

This program corrects that by flipping the layout file around.

The process is:
- connect the left half of your keyboard
- use via to configure the left half of the keyboard
- save your layout to a *.layout.json file
- use this program to flip the layout in that file
- disconnect the left half of your keyboard
- connect the right half of your keyboard
- load the flipped layout file in via

## Usage

This program requires a single argument: the input file name/path.

For example:

`python3 swap.py lily58.layout.json`

Or with the file path:

`python3 swap.py /home/user/lily58.layout.json`

## Output

The output file will be placed in the same directory as the input file.

It will be given the same name as the input file, but with `layout` replaced with `flipped`.

For example, running:

`python3 swap.py /home/user/lily58.layout.json`

would result in `/home/user/lily58.flipped.json` being created.