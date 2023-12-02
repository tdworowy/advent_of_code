use std::{collections::HashMap, fs::read_to_string};

fn sum_calibration_values(input: Vec<String>) -> i32 {
    let mut sum: i32 = 0;
    for s in input {
        let digits: String = s.chars().filter(|c| c.is_digit(10)).collect();
        let mut temp: String = "".to_owned();
        temp.push(digits.chars().nth(0).unwrap());
        temp.push(digits.chars().last().unwrap());
        sum += temp.parse::<i32>().unwrap();
    }
    sum
}

fn sum_calibration_values2(input: Vec<String>) -> i32 {
    let mumber_map = HashMap::from([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);

    let mut sum: i32 = 0;
    let mut temp: String = "".to_owned();
    let mut result: Vec<String> = Vec::new();

    for s in input {
        temp = "".to_owned();
        for char in s.chars() {
            temp.push(char);
            for key in mumber_map.keys() {
                if temp.contains(key) {
                    result.push(key.to_string());
                    temp = temp.chars().last().unwrap().to_string();
                }
            }
            if char.is_digit(10) {
                result.push(char.to_string());
            }
        }

        let first = result[0].clone();
        let last = result.last().unwrap();

        let first_number = if mumber_map.contains_key(first.as_str()) {
            *mumber_map.get(first.as_str()).unwrap()
        } else {
            &first
        };

        let last_number = if mumber_map.contains_key(last.as_str()) {
            *mumber_map.get(last.as_str()).unwrap()
        } else {
            last
        };
        //println!("{:?}", s);
        let two_digits: String = format!("{}{}", first_number, last_number);
        //println!("{}", two_digits);
        sum += two_digits.parse::<i32>().unwrap();

        result = Vec::new();
    }
    sum
}

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn main() {
    let input = read_lines("input.txt");
    let sum1 = sum_calibration_values(input.clone());
    let sum2 = sum_calibration_values2(input.clone());
    println!("Part1: {}", sum1);
    println!("Part2: {}", sum2);
}
