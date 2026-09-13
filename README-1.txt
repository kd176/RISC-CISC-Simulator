RISC VS CISC SIMULATION TOOL
=============================

1. PROJECT TITLE
----------------
Comparative Study of RISC vs CISC Architectures

2. PROJECT DESCRIPTION
----------------------
This project is a simple simulation tool developed using Python
and Tkinter.

The purpose of this tool is to compare how the same assembly
instructions can be represented in RISC and CISC architectures.

The user enters assembly instructions such as ADD, SUB, MUL and MOV.
The program then converts them into a simplified RISC and CISC
execution sequence.

The simulator displays:
- RISC instructions
- CISC instructions
- Number of instructions
- Estimated clock cycles
- Clock cycle comparison
- Faster architecture for the given input


3. OBJECTIVE
------------
The main objective of this project is to understand the basic
difference between RISC and CISC architectures through simulation.

It helps to visualize how:
- RISC uses more simple instructions.
- CISC can perform operations using more complex instructions.
- The number of instructions and estimated clock cycles can differ.


4. TECHNOLOGIES USED
--------------------
Programming Language : Python
GUI Library          : Tkinter
Additional Library   : ttk
IDE                  : Visual Studio Code


5. REQUIREMENTS
---------------
Software Requirements:
- Python 3.x
- Visual Studio Code or any Python IDE
- Tkinter library

No external Python packages are required.


6. HOW TO RUN THE PROJECT
-------------------------
Step 1:
Install Python 3.x on the computer.

Step 2:
Open the project folder in Visual Studio Code.

Step 3:
Open the file:

risc_cisc_simulator.py

Step 4:
Run the Python file.

Step 5:
The RISC vs CISC Simulator window will open.


7. HOW TO USE THE SOFTWARE
---------------------------
1. Enter assembly instructions in the input box.

Example:

ADD R1,R2
SUB R3,R4
MUL R5,R6
MOV R1,R2

2. Click "RUN SIMULATION".

3. The software generates a simplified execution sequence
   for both RISC and CISC.

4. The result is displayed in two sections:
   - RISC EXECUTION
   - CISC EXECUTION

5. The software also displays:
   - Total instructions
   - Estimated clock cycles
   - Clock cycle comparison
   - Performance result


8. AVAILABLE BUTTONS
--------------------
RUN SIMULATION
--------------
Starts the simulation and calculates the instruction count
and estimated clock cycles.

LOAD EXAMPLE
------------
Loads a predefined assembly program into the input box.

CLEAR
-----
Clears the input and previous simulation results.


9. SIMULATION LOGIC
-------------------
The simulator uses a simple predefined model.

For ADD:

RISC:
LOAD -> ADD -> STORE
Estimated cycles = 3

CISC:
ADD
Estimated cycles = 2


For SUB:

RISC:
LOAD -> SUB -> STORE
Estimated cycles = 3

CISC:
SUB
Estimated cycles = 2


For MUL:

RISC:
LOAD -> MUL -> STORE
Estimated cycles = 3

CISC:
MUL
Estimated cycles = 3


For MOV:

RISC:
LOAD -> STORE
Estimated cycles = 2

CISC:
MOV
Estimated cycles = 2


10. OUTPUT
----------
The software provides a visual comparison between RISC and CISC.

It shows:
- Instruction count
- Estimated clock cycles
- Execution sequence
- Progress bars for cycle comparison

The software also displays which architecture has fewer
estimated cycles for the given input.


11. IMPORTANT NOTE
------------------
This is an educational simulation and not a real processor
emulator.

The clock cycles used in this project are estimated values
defined by the simulation model.

Actual RISC and CISC processors can have different instruction
sets, pipelines, memory operations and execution times.


12. ADVANTAGES
--------------
- Simple and beginner-friendly.
- Easy to understand RISC and CISC concepts.
- Provides visual comparison.
- Shows instruction execution sequences.
- Shows estimated clock cycle comparison.
- Does not require external Python packages.


13. LIMITATIONS
---------------
- It uses a simplified RISC and CISC model.
- It supports only a small set of instructions.
- It does not simulate a real CPU.
- It does not model cache, pipeline, registers or memory in detail.
- Clock cycle values are predefined estimates.


14. FUTURE SCOPE
----------------
The project can be improved by adding:
- More assembly instructions.
- Register visualization.
- Memory simulation.
- Pipeline visualization.
- More detailed performance analysis.
- Instruction-by-instruction animation.


15. CONCLUSION
--------------
This project demonstrates the basic difference between RISC
and CISC architectures using a simple simulation tool.

The same input instructions are converted into different
execution sequences and their instruction counts and estimated
clock cycles are compared.

The project provides an easy way to understand the fundamental
concept of RISC vs CISC architecture.