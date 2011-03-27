rm -r nbody/out
time bin/hadoop jar contrib/streaming/hadoop-0.20.2-streaming.jar -file nbody/mapper.py -mapper nbody/mapper.py -file nbody/reducer.py -reducer nbody/reducer.py -input nbody/sim.txt -output nbody/out

