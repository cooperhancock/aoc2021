mod day_1;
use day_1::*;
mod day_2;
use day_2::*;

fn main() {
    println!("part 1 solution: {}", sonar_sweep_part_1(&input_data()));
    // let (h, d) = dive_part_1(&input_data());
    // println!("part 1 solution: {}", h * d);
    // let (h, d, _a) = dive_part_2(&input_data());
    // println!("part 1 solution: {}", h * d);
}

fn input_data() -> Vec<String> {
    let chonky_input = include_str!("..\\..\\1.txt");
    return chonky_input.lines().map(|x| x.to_string()).collect();
}

