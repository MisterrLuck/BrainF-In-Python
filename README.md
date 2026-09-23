# BrainF In Python

I remade the BrainF*** Esolang in Python

You can find the original code on [GitHub](https://github.com/fabianishere/brainfuck).

## Prerequisites

You only need to have python installed.

The installation will only work linux, but you can use without installing on any OS.

## Installation

Navigate to the build/Linux/ directory. Run build.sh.

You shouldn't have to open a new terminal as the program is added to the local bin directory which is already on the path.

```bash
cd build/Linux/
chmod +x build.sh
./build.sh

brain # This runs the shell
brain ../../examples/hello.bf # This runs the hello world example program
```
You shouldn't need to do exact file paths to run a program.

## Usage without Installation

To use the BrainF interpreter without installing, navigate to the src/ directory.

There are two possible modes. Shell and File.

To run a file, specify the name of the file after the python program. You may have to be very exact with the file path.

To run as a shell, you can just run the python program.

```bash
cd src/
python main.py # This runs the shell
python main.py ../examples/hello.bf # This runs the hello world example program
```

