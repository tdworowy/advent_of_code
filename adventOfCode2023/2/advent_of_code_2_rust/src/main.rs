use std::{collections::HashMap, fs::read_to_string};

// and remove word game
const RED: usize = 12;
const GREEN: usize = 13;
const BLUE: usize = 14;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn check(value_map: HashMap<&str, usize>) -> bool {
    value_map.get("red").unwrap() <= &RED
        && value_map.get("blue").unwrap() <= &BLUE
        && value_map.get("green").unwrap() <= &GREEN
}

fn sum_ids(input: Vec<String>) -> usize {
    let mut sum: usize = 0;

    for s in input {
        // println!("{:?}", s);
        let chunks: Vec<&str> = s.split(":").collect();
        // println!("{:?}", chunks[0]);

        let id =chunks[0].trim();
        let data: Vec<&str> = chunks[1].split(",").collect();
        let mut value_map: HashMap<&str, usize> =
            HashMap::from([("red", 0), ("blue", 0), ("green", 0)]);

        // TODO hadnle sets separator -> ;    
        for d in data {
            let temp: Vec<&str> = d.split(" ").collect();
            // println!("{:?} {:?}",id, temp);
            let v: &str = &temp[1];
            let t: &str = &temp[2];
            *value_map.get_mut(t).unwrap() += v.parse::<usize>().unwrap();
        }
        if check(value_map) {
            sum += id.parse::<usize>().unwrap();
        }
    }

    sum
}

fn main() {
    let input = read_lines("input.txt");
    let sum = sum_ids(input);
    println!("Part1: {}", sum);
}
