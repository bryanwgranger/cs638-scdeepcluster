##!/bin/bash


gammas="0.5 1 3 5 7 9"

cd /Users/bryanwgranger/Documents/sandbox/cs638/scdeepcluster

mkdir output/pbmc-256-64

mkdir output/pbmc-256-64/model_PBMC_gamma_0.1
python run_scDeepCluster.py \
	--data_file data/hg19/ \
	--gamma 0.1 \
	--conv_sizes 256,64 \
	--save_dir output/pbmc-256-64/model_PBMC_gamma_0.1 \

mv AE_weights.pth.tar output/pbmc-256-64

for gamma in $gammas
do
	mkdir output/pbmc-256-64/model_PBMC_gamma_$gamma
	echo "Training gamma = "$gamma
	python run_scDeepCluster.py \
	--data_file data/hg19/ \
	--gamma $gamma \
	--conv_sizes 256,64 \
	--save_dir output/pbmc-256-64/model_PBMC_gamma_$gamma \
	--ae_weights /Users/bryanwgranger/Documents/sandbox/cs638/scdeepcluster/output/pbmc-256-64/AE_weights.pth.tar
done

mkdir output/pmbc-500-500-2000

mkdir output/pmbc-500-500-2000/model_PBMC_gamma_0.1
python run_scDeepCluster.py \
	--data_file data/hg19 \
	--gamma 0.1 \
	--conv_sizes 500,500,2000 \
	--save_dir output/pbmc-500-500-2000/model_PBMC_gamma_0.1 \

mv AE_weights.pth.tar output/pbmc-500-500-2000

for gamma in $gammas
do
	mkdir output/pbmc-500-500-2000/model_PBMC_gamma_$gamma
	echo "Training gamma = "$gamma
	python run_scDeepCluster.py \
	--data_file data/hg19/ \
	--gamma $gamma \
	--conv_sizes 500,500,2000 \
	--save_dir output/pbmc-500-500-2000/model_PBMC_gamma_$gamma \
	--ae_weights /Users/bryanwgranger/Documents/sandbox/cs638/scdeepcluster/output/pbmc-500-500-2000/AE_weights.pth.tar
done

