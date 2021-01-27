// check.cue
min?: *0 | number    // 0 if undefined
max?: number & >min  // must be strictly greater than min if defined.
