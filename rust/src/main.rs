fn main() {
    let (h, d) = dive_part_1(&input_data());
    println!("part 1 solution: {}", h * d);
    let (h, d, a) = dive_part_2(&input_data());
    println!("part 1 solution: {}", h * d);
}

fn input_data() -> Vec<String> {
    let chonky_input = include_str!("..\\..\\2_dive_input.txt");
    return chonky_input.lines().map(|x| x.to_string()).collect();
}

// string -> (string, i32)
fn split(s: &String) -> (&str, i32) {
    let mut command = s.split_whitespace();
    return (command.next().unwrap(), command.next().unwrap().parse::<i32>().unwrap());
}

fn dive_part_1(input: &Vec<String>) -> (i32, i32) {
    let commands: Vec<(&str, i32)> = input.into_iter().map(split).collect();
    // string, i32, i32 -> i32, i32
    fn process((h, d): (i32, i32), c: (&str, i32)) -> (i32, i32){
        match c {
            ("forward", x) => (h + x, d),
            ("down", x) => (h, d + x),
            ("up", x) => (h, d - x),
            _ => panic!("oopsie woopsie the pattern doesnt match uwu")
        }
    }
    return commands.into_iter().fold((0, 0), process);
}

fn dive_part_2(input: &Vec<String>) -> (i32, i32, i32) {
    let commands: Vec<(&str, i32)> = input.into_iter().map(split).collect();
    // horizontal, depth, aim
    fn process((h, d, a): (i32, i32, i32), c: (&str, i32)) -> (i32, i32, i32){
        match c {
            ("forward", x) => (h + x, d + a*x, a),
            ("down", x) => (h, d, a + x),
            ("up", x) => (h, d, a - x),
            _ => panic!("oopsie woopsie the pattern doesnt match uwu")
        }
    }
    return commands.into_iter().fold((0, 0, 0), process);
}