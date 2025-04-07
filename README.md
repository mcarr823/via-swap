# via-swap.py

This python script is used to flip (https://usevia.app/)[VIA] (or (https://get.vial.today/)[VIAL]) keyboard layouts.

It is intended to be used with split keyboards, such as the lily58 keyboard, which have micro-controllers on both halves of the keyboard.

## The problem

Split keyboards identify which "side" of the keyboard is plugged in based on the firmware installed on the micro-controller.

If both micro-controllers have been flashed with the same firmware, then they will both think they're the "left" side of the keyboard.

This works fine if you connect the left side to your computer. But if you connect the right side to your computer instead, then this will result in the layout being reversed.

## The solution

One solution to that problem is to recompile and reflash the firmware on the right micro-controller, so that it knows it's the right side instead of the left.

An alternative solution which doesn't require code compilation or flashing is to flip the keymap around instead. So the right side of the keyboard still thinks it's the left side, but the keys have been rearranged to work around it.

This program facilitates the second approach.

## How does it work?

The process is:
- connect the left half of your keyboard
- use via(l) to configure the left half of the keyboard
- save your layout to a *.layout.json or *.vil file
- use this program to flip the layout in that file
- disconnect the left half of your keyboard
- connect the right half of your keyboard
- load the flipped layout file in via(l)

## Usage

This program requires a single argument: the input file name/path.

For example:

`python3 via-swap.py lily58.layout.json`

Or with the file path:

`python3 via-swap.py /home/user/lily58.layout.json`

VIAL files are the same, except you should use `vial-swap.py` and `*.vil` files instead. eg.

`python3 vial-swap.py lily58.vil`

## Output

The output file will be placed in the same directory as the input file.

It will be given the same name as the input file, but with `layout` replaced with `flipped` for VIA files.

Or with `flipped` added to the name for VIAL files.

For example, running:

`python3 via-swap.py /home/user/lily58.layout.json`

would result in `/home/user/lily58.flipped.json` being created.

Similarly, running:

`python3 vial-swap.py /home/user/lily58.vil`

would result in `/home/user/lily58.flipped.vil` being created.