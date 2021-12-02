use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() {
    let f = File::open("../input/day1.txt").expect("Error opening file");
    let my_list = BufReader::new(f);

    let mut last1: i64 = -1;
    let mut last2: i64 = -1;
    let mut last3: i64 = -1;

    let mut last_sum: i64 = -1;
    let mut new_sum: i64;

    let mut part_one: i64 = 0;
    let mut part_two: i64 = 0;
    
    for item in my_list.lines() {
        if last1 == -1 {
            last1 = item.unwrap().parse::<i64>().unwrap();
        } else if last2 == -1 {
            last2 = item.unwrap().parse::<i64>().unwrap();
        } else if last3 == -1 {
            last3 = item.unwrap().parse::<i64>().unwrap();
        } else {
            last1 = last2;
            last2 = last3;
            last3 = item.unwrap().parse::<i64>().unwrap();
            new_sum = last1 + last2 + last3;
            if new_sum > last_sum {
                part_two += 1;
            }
            last_sum = new_sum;
        }

        if last2 != -1 {
            if last2 > last1 {
                part_one += 1;
            }
        }
    }

    println!("part_one = {}", part_one);
    println!("part_two = {}", part_two);
}

// $ rustc day1.rs
// $ ./day1
// part_one = 1316
// part_two = 1344