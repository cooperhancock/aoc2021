
pub fn sonar_sweep_part_1(input: &Vec<String>) -> i32 {
    let data: Vec<i32> = input.into_iter().map(|x| x.parse::<i32>().unwrap()).collect();
    // Vec<i32> -> iter (i32, i32)
    let iter = data.windows(2);
    return iter.fold(0, |sum, n| 
        match n {
            &[x, y] => if y > x {sum + 1} else {sum},
            _ => sum
        });
}

