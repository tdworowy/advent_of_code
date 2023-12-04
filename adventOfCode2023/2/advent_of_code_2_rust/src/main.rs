use std::{collections::HashMap, fs::read_to_string};

// remove word game
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

fn part1(input: &Vec<String>) -> usize {
    let mut sum: usize = 0;

    for s in input {
        // println!("{:?}", s);
        let chunks: Vec<&str> = s.split(":").collect();
        // println!("{:?}", chunks[0]);

        let id = chunks[0].trim();
        let mut possible_set: bool = true;
        for set in chunks[1].split(";") {
            let data: Vec<&str> = set.split(",").collect();
            let mut value_map: HashMap<&str, usize> =
                HashMap::from([("red", 0), ("blue", 0), ("green", 0)]);

            for d in data {
                let temp: Vec<&str> = d.split(" ").collect();
                // println!("{:?} {:?}",id, temp);
                let v: &str = &temp[1];
                let t: &str = &temp[2];
                *value_map.get_mut(t).unwrap() += v.parse::<usize>().unwrap();
            }
            if !check(value_map) {
                possible_set = false;
                break;
            }
        }
        if possible_set {
            // println!("{:?}",id);
            sum += id.parse::<usize>().unwrap();
        }
    }

    sum
}

fn part2(input: &Vec<String>) -> usize {
    let mut sum: usize = 0;

    for s in input {
        // println!("{:?}", s);
        let chunks: Vec<&str> = s.split(":").collect();
        // println!("{:?}", chunks[0]);
        let mut value_map: HashMap<&str, usize> =
            HashMap::from([("red", 0), ("blue", 0), ("green", 0)]);
        for set in chunks[1].split(";") {
            let data: Vec<&str> = set.split(",").collect();

            for d in data {
                let temp: Vec<&str> = d.split(" ").collect();
                // println!("{:?} {:?}",id, temp);
                let v: &str = &temp[1];
                let t: &str = &temp[2];
                let mut v_int = v.parse::<usize>().unwrap();
                if value_map.get_mut(t).unwrap() < &mut v_int {
                    *value_map.get_mut(t).unwrap() = v_int;
                }
            }
        }
        sum += value_map.get("red").unwrap()
            * value_map.get("blue").unwrap()
            * value_map.get("green").unwrap();
    }

    sum
}

fn main() {
    let input = read_lines("input.txt");
    let sum1 = part1(&input);
    println!("Part1: {}", sum1);

    let sum2 = part2(&input);
    println!("Part2: {}", sum2);
}
//part1: 2720
//part2: 71535