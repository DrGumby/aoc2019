use std::fs;

pub fn ex1f() -> u64 {
    let contents = fs::read_to_string("src/day1/input")
        .expect("Something went wrong");
    let lns = contents.lines();
    let mut sum = 0;
    for line in lns {
        sum += ex1fcalc(line.parse::<u64>().unwrap());
    }
    return sum;
}

fn ex1fcalc(val: u64) -> u64 {
    return val / 3 -2;
}

pub fn ex2f() -> u64 {
    let contents = fs::read_to_string("src/day1/input")
       .expect("Something went wrong");
    let lns = contents.lines();
    let mut sum = 0;
    for line in lns {
        sum += ex2fcalcwrap(line.parse::<i64>().unwrap()) as u64;
    }
    return sum;
}
fn ex2fcalcwrap(x: i64) -> i64 {
    let y = x / 3 - 2;
    return ex2fcalc(y);
}
fn ex2fcalc(x: i64) -> i64 {
    if x < 0 {
        return 0;
    } else {
        return x + ex2fcalc(x / 3 -2);
    }
}

#[test]
fn ex1f_test1() {
    assert_eq!(ex1fcalc(1969), 654);
}

#[test]
fn ex1f_test2() {
    assert_eq!(ex1fcalc(100756), 33583);
}

#[test]
fn ex2f_test1() {
    assert_eq!(ex2fcalcwrap(1969), 966);
}

#[test]
fn ex2f_test2() {
    assert_eq!(ex2fcalcwrap(100756), 50346);
}
