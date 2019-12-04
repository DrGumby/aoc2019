pub fn ex7f() -> u64 {
    let start = 147981;
    let end = 691423;
    return ex7fcalc(start, end) as u64;
    //return 0
}

fn ex7fcalc(start:u32, end:u32) -> u32{
    let mut sum = 0;
    for n in start..end {
        if !ex7_length_csr(n) {
            continue;
        }

        if !ex7_double_digit_csr(n) {
            continue;
        }

        if !ex7_never_decrease_csr(n) {
            continue;
        }

        sum = sum + 1;
    }
    return sum;
}

fn ex7_double_digit_csr(n:u32) -> bool {
    let n_string = n.to_string();
    let alphabet = "0123456789";
    for d in alphabet.chars() {
        if n_string.matches(d).count() >= 2 {
            return true;
        }
    }
    return false;   
}

fn ex7_never_decrease_csr(n:u32) -> bool {
    let n_string_char_vec: Vec<char> = n.to_string().chars().collect();
    for i in 0..n_string_char_vec.len()-1 {
        if n_string_char_vec[i+1].to_digit(10) < n_string_char_vec[i].to_digit(10) {
            return false;
        }
    }

    return true;
}

fn ex7_length_csr(n:u32) -> bool {
    return n.to_string().len() == 6;
}

#[test]
fn ex7_double_digit_csr_test1() {
    assert_eq!(ex7_double_digit_csr(111111), true);
}

#[test]
fn ex7_double_digit_csr_test2() {
    assert_eq!(ex7_double_digit_csr(122345), true);
}

#[test]
fn ex7_double_digit_csr_test3() {
    assert_eq!(ex7_double_digit_csr(123789), false);
}

#[test]
fn ex7_length_csr_test1() {
    assert_eq!(ex7_length_csr(123789), true);
}

#[test]
fn ex7_length_csr_test2() {
    assert_eq!(ex7_length_csr(13789), false);
}

#[test]
fn ex7_never_decrease_csr_test1() {
    assert_eq!(ex7_never_decrease_csr(223450), false);
}

#[test]
fn ex7_never_decrease_csr_test2() {
    assert_eq!(ex7_never_decrease_csr(223456), true);
}