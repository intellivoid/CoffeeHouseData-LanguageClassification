# Language Classification 

This is the source code for the Langdetect model used in
CoffeeHouse Language Detection module. This model currently
supports 106 languages and allows for additional data to be
generated using Googe Tanslate.

The translations do not need to be accuracte, but rather
accurate enough to allow the model to tell the difference
between the characteristics of the many languges.


## Building The Model

Builiding the model requires CoffeeHouse-DLTC and
CoffeeHouse-NLPFR to be installed on the system, you can build
the model in the foreground or background by running one of
these commands

```sh
# Build the model in the foreground (Normal)
make build

# Build the model in the background (Requires screen)
make background_build
```


## Testing the model

You can run an interactive Commandline Interface test to predict
the output of the model's predictions by running the DLTC tester.

```sh
make test
```


## Adding more data

Simply add a bunch of English sentences to a file named input.txt
and run the generate_dat command

```sh
make generate_data
```

Once the data is generated, it's reccomended to clean the and
organize the new data that was generated.

```sh
make clean
```