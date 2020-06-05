
# Documenting your workflow with a `Makefile`

## Build the image 

```bash
 docker build -t make-example .
```

## Make the raw data 

We are mounting this entire directory so that make wll see changes to the configuration files as well as be able to read and write to the data folder. 

```bash
docker run --mount type=bind,source="$(pwd)",target=/app/ make-example data/raw.csv
```

## Make the features

Notice that running `make data/features.csv` first makes `data/clean.csv` because `data/features.csv` requires it and it doesn't exist. If you were to delete `data/raw.csv`, it would create it as well. 

```bash
docker run --mount type=bind,source="$(pwd)",target=/app/ make-example data/features.csv
```

## Run reproducibility tests 

```bash
docker run --mount type=bind,source="$(pwd)",target=/app/ make-example tests
```

## Clean up reproducibility tests

```bash
docker run --mount type=bind,source="$(pwd)",target=/app/ make-example clean
```

# Documenting your workflow with a bash script 

## Build the image 

```bash
 docker build -f Dockerfile_bash -t bash-example .
```

## Execute the pipeline 

Note: we only mount the data folder here because if we were to mount the current directory, the container would access our local version of `run-pipeline.sh`, which on Windows computers, will not be formatted correctly. Also, it would require `chmod +x run-pipeline.sh` to be run locally. 

```bash
docker run --mount type=bind,source="$(pwd)/data",target=/app/data/ bash-example run-pipeline.sh
```

## Run tests

```bash
docker run --mount type=bind,source="$(pwd)/data",target=/app/data/ bash-example run-reproducibility-tests.sh
``` 
