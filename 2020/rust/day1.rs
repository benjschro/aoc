use std::fs::File;
use std::io::{BufRead, BufReader};
use std::str;

fn load_file_to_int_vector(file_name: &str) -> Result<Vec<i64>, String> {
    let file = match File::open(file_name) {
        Ok(v) => (v),
        Err(e) => return Err(e.to_string()),
    };

    let reader = BufReader::new(file);
    let mut integer_vector = Vec::<i64>::new();

    for line in reader.lines() {
        match line.unwrap().parse::<i64>() {
            Ok(v) => integer_vector.push(v),
            Err(e) => return Err(e.to_string()),
        }
    }

    return Ok(integer_vector)
}

fn multiply_two_entries_that_sum_to_2020(integer_vector: &Vec<i64>) -> Result<i64, String> {
    for i in 0..integer_vector.len() {
        for j in i+1..integer_vector.len()-1 {
            if integer_vector[i] + integer_vector[j] == 2020 {
                return Ok(integer_vector[i] * integer_vector[j]);
            }
        }        
    }

    return Err("Could not find 2 numbers that sum to 2020".to_string())
}

fn multiply_three_entries_that_sum_to_2020(integer_vector: &Vec<i64>) -> Result<i64, String> {
    for i in 0..integer_vector.len() {
        for j in i+1..integer_vector.len()-1 {
            for k in i+1..integer_vector.len()-2 {
                if integer_vector[i] + integer_vector[j] + integer_vector[k] == 2020 {
                    return Ok(integer_vector[i] * integer_vector[j] * integer_vector[k]);
                }
            }
        }        
    }

    return Err("Could not find 2 numbers that sum to 2020".to_string())
}

fn aoc2020_day1(file_name: &str) -> Result<[i64; 2], String> {
    let integer_vector = match load_file_to_int_vector(file_name) {
        Ok(v) => (v),
        Err(e) => return Err(e)
    };

    let part_one = multiply_two_entries_that_sum_to_2020(&integer_vector);

    let part_two = multiply_three_entries_that_sum_to_2020(&integer_vector);

    return Ok([part_one.unwrap(), part_two.unwrap()])
}

fn main() {
    let aoc2020_day1_results = aoc2020_day1("day1.txt");
    println!("day1 results:");
    match aoc2020_day1_results {
        Ok(v) => println!("  part_one = {}\n  part_two = {}", v[0], v[1]),
        Err(e) => println!("{}", e)
    }

}