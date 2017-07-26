#! bin/bash
cd "$(dirname "$0")"

# events to be traced
# cycles                    - number of cycles needed
# instructions              - instructions per cycle
# stalled-cycles-frontend   - cycles waiting for cache to fill
# stalled-cycles-backend    - cycles waiting for an instruction to happen
# task-clock                - clock speed
# page-faults               - lazy memory allocation events
# minor-faults              - memory allocation event
# major-fault               - allocation from external device
# cache-references          - reference data in cache
# cache-misses              - referenced data not in cache
# context-switches          - program was halted by OS
# migrations                - CPU-migration, program resumed on differen CPU
# branches                  - execution flow changes
#branch-misses              - mispredicted branches
perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,task-clock,page-faults,minor-faults,major-faults,cache-references,cache-misses,context-switches,migrations,branches,branch-misses -r 3 python diff2d/diffusion.py input.png 0.7 0.1 100