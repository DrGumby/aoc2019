mod ex;
mod day1;
mod day4;
use crate::ex::Run;

fn main() {
    let ex1 = ex::Ex {
        name: String::from("D1E1"),
        f: day1::ex1f
    };
    let ex2 = ex::Ex {
        name: String::from("D1E2"),
        f: day1::ex2f
    };
    let ex7 = ex::Ex {
        name: String::from("D4E1"),
        f: day4::ex7f
    };

    let exs: Vec<&ex::Ex> = vec![&ex1, &ex2, &ex7];

    for ex in exs {
        println!("Name: {0}\nValue: {1}",ex.name, ex.run());
    }
}

