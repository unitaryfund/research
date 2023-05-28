for wroot in {5..8}; do
    w=$(( wroot * wroot ))
    for ((d=1; d<=$w; ++d)); do
        for t in {0..9}; do
            for ((s=80; s>=0; s--)); do
                python3 heat_map_generation.py --trial=$t --width=$w --depth=$d --sdrp=$s
                if [ $? -ne 0 ]; then
                    break
                fi
            done
        done
    done
done
