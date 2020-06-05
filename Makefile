data/raw.csv: config/config_file.yaml
	python3 run.py acquire --config=config/config_file.yaml --output=data/raw.csv

data/features.csv: data/raw.csv config/config_file.yaml
	python3 run.py featurize --input=data/raw.csv --config=config/config_file.yaml --output=data/features.csv

data/model_results.csv: data/features.csv config/config_file.yaml
	python3 run.py build_models --input=data/features.csv --config=config/config_file.yaml --output=data/model_results.csv

tests:
	python3 run.py test --config=test/config_test.yaml

clean:
	rm test/test_dr/*

all: data/raw.csv data/features.csv data/model_results.csv

.PHONY: tests clean all
