pub struct Ex {
    pub name: String,
    pub f: fn() -> u64
}

pub trait Run {
    fn run(&self) -> u64;
}

pub trait Name {
    fn name(&self) -> String;
}

impl Run for Ex {
    fn run(&self) -> u64 {
        return (self.f)();
    }
}