use std::fs;
use std::collections::HashSet;

#[derive(PartialEq, Hash, Eq, Copy, Clone)]
pub struct Coord {
    x: i32,
    y: i32
}

fn simulate_route(contents: &str, without_robo: bool) -> usize {
    let mut hm: HashSet<Coord> = HashSet::new();
    let mut coord_santa = Coord {x: 0, y: 0};
    let mut coord_robo_santa = Coord {x: 0, y: 0};

    hm.insert(coord_santa);

    let mut coord_ptr;
    for (i, c) in contents.chars().enumerate() {
        if i % 2 == 0 || without_robo {
            coord_ptr = &mut coord_santa;
        } else {
            coord_ptr = &mut coord_robo_santa;
        }

        if c == '^' {
            (*coord_ptr).y += 1;
        } else if c == 'v' {
            (*coord_ptr).y -= 1;
        } else if c == '<' {
            (*coord_ptr).x -= 1;
        } else {
            (*coord_ptr).x += 1;
        }

        hm.insert(*(coord_ptr));
    }
    
    hm.len()
}

fn main() {
    let contents = fs::read_to_string("../input/day3.txt").unwrap();

    println!("partOne = {}", simulate_route(&contents, true));
    println!("partTwo = {}", simulate_route(&contents, false));
}