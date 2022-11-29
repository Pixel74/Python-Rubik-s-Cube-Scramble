# rubikpy
A basic Rubik's cube scrambler, visualizer and chronometer made in Python. It can be use through a GUI or executed as a script in the terminal.

## Project status

The project is currently in development. Things to be added included:
-load_csv function.
-Improvements in GUI.
-Optimization (proposal explained below)
-Support for 2x2 and 4x4 cubes, as well as custom title colors.
-Executable file.
-Requirements file.

## Screenshots

## Installation and Setup

Clone down this repository. The program can run in a GUI or terminal. However, the chronometer and image visualization is limited to the GUI execution.

###GUI:

1. Navigate to the package folder and execute *app.py*.

###Terminal:

The different components of the project can be used independently. Provided proper input/output, you are able to use the following scripts:

-*main.py* will run the main program in the terminal.
-*scramble_generator.py* will generate random scrambles with length as a parameter.
-*test_input.py* and *test_from_file.py* will test the scrambler against a known pair of input and output.
-*benchmark.py* will run the profiler through the tests. 

#### To run main.py

1. Navigate to the package folder and execute *main.py*.

##### Giving input to main.py

When running *main.py* as a script, you can input an algorithm as follows:

-Type an algorithm to scramble the cube according common rubik's cube notation ***(Ex. "L R U2 B' F")***.
-Type "auto" followed by an integer which represents the length of the algorithm to be generated ***(Ex. "auto 20")***. This will use *scramble_generator.py* to generate and algorithm with the given amount of movements.  

#### To run scramble_generator.py

1. Navigate to the package folder and execute *scramble_generator.py*.

This will give as ouput a string containing the specified amount of movements. This is generated used the random function from the standard library.

#### To run test_input.py and test_from_file.py

1. Navigate to the package folder and execute *test_input.py* or *test_from_file.py*.

##### Test limitations

-Note that there are 6 tests delivered with the package (1 test input and 5 part of test file).

-For test_input.py, the input is given as a variable in the code, this can be changed directly. Or it is possible to pass another pytest.fixture as a parameter to the test, which would result in a new evaluation. However, keep in mind that if the test input is changed, the expected output must also be changed accordingly.

-For test_from_file.py, the inputs to test can be found in the inputs.txt file. As with test_input.py, the expected outputs must also be change accordingly.

-There is no limit for the input test length.

#### To run benchmark.py

1. Navigate to the package folder and execute *benchmark.py*.

Please refer to the [cProfile Documentation](https://docs.python.org/3/library/profile.html) to understand the use of sort_stats() and a more powerful use of cProfile. *benchmark.py* runs the same test structure as *test_input.py* and *test_from_file.py*. Although, it is independent from them, this means that you must change the inputs and expected outputs if there is conflict between the tests and benchmark scenarios.

## Further details

I developed this as a side project to practice my Python skills, the original code was developed over the course of a couple of days. It was written some years ago, however, due to my lack of git and github knowledge it is only now that I upload a somewhat well documented repository.  

Originally, my plan when revisiting the project was to improve the performance. This included developing tests and benchmark scripts to allow me to properly measure any improvements in performance, as well as updating to a better folder tree. Although the improvement in performance turned out to be not feasible (further explanation below), trying to understand and improve old code, as well as trying to come up with a performance solution, were great experiences overall.

## Optimization proposal
