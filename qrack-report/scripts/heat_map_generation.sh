for t in {1..10}; do
    for w in {2..28}; do
        for ((d=1; d<=$w; ++d)); do
            # for s in {0..80}; do
            python3 heat_map_generation.py --trial=$t --width=$w --depth=$d --sdrp=0
            # done
        done
    done
done
