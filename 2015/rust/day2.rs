use std::fs;
use std::cmp;

fn main() {
    let contents = fs::read_to_string("../input/day2.txt").unwrap();
    let mut dims: [i32; 3] = [0; 3];
    let mut surface_area = 0;
    let mut scrap = 0;
    let mut ribbon = 0;

    for gift in contents.lines() {
        for (i, elem) in gift.split('x').enumerate() {
            dims[i] = elem.parse().unwrap();
        }

        surface_area += (2 * dims[0] * dims[1]) + (2 * dims[1] * dims[2]) + (2 * dims[0] * dims[2]);
        scrap += cmp::min(cmp::min(dims[0] * dims[1], dims[0] * dims[2]), dims[1] * dims[2]);

        ribbon += dims[0]*2 + dims[1]*2 + dims[2]*2;
        ribbon -= cmp::max(cmp::max(dims[0]*2, dims[1]*2), dims[2]*2);
        ribbon += dims[0] * dims[1] * dims[2];
    }

    println!("partOne = {}", surface_area + scrap);
    println!("partTwo = {}", ribbon);
}