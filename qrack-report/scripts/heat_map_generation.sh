for t in {1..10}; do
    for wroot in {6..8}; do
        w=$(( $wroot * $wroot ))
        for ((d=1; d<=$w; ++d)); do
            for s in {1..80}; do
                python3 heat_map_generation.py --trial=$t --width=$w --depth=$d --sdrp=$s
            done
        done
    done
done
