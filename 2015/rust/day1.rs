use std::fs;

fn main() {
    let mut floor = 0;
    let mut basement_index = 0;

    let contents = fs::read_to_string("../input/day1.txt").unwrap();
    
    for (i, c) in contents.chars().enumerate() {
        if c == '(' {
            floor += 1;
        } else {
            floor -= 1;
        }

        if floor == -1 && basement_index == 0 {
            basement_index = i + 1;
        }
    }

    println!("partOne = {}\npartTwo = {}", floor, basement_index);
}