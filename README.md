#About Docker

Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allow you to run many containers simultaneously on a given host. ... You can even run Docker containers within host machines that are actually virtual machines!


# Assignment 3 AVC (Reproducibility)

In this assignment following things have been done:
* Code has been modularised
* Config files have been created
* A pipeline has been made using Makefile
* Testing of the code written

In order to run this utility please follow the following steps

## Step 1 : Build the docker image

```
 docker build -t repro .
```

## Step 2: Acquiring the raw data

```
docker run --mount type=bind,source="$(pwd)",target=/app/ repro data/raw.csv
```

## Step 3: Building the features

```
docker run --mount type=bind,source="$(pwd)",target=/app/ repro data/features.csv
```

## Step 4: Building the model

```
docker run --mount type=bind,source="$(pwd)",target=/app/ repro data/model_results.csv
```


## Step 5: Performing tests

```
docker run --mount type=bind,source="$(pwd)",target=/app/ repro tests
```



