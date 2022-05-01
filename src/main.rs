#![no_std]
#![no_main]

// pick a panicking behavior
use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
// use panic_abort as _; // requires nightly
// use panic_itm as _; // logs messages over ITM; requires ITM support
// use panic_semihosting as _; // logs messages to the host stderr; requires a debugger

use cortex_m::asm;
use cortex_m_rt::entry;
use cortex_m_semihosting::{debug, hprintln};

#[entry]
fn main() -> ! {
    asm::nop(); // To not have main optimize to abort in release mode, remove when you add code
    hprintln!("Hello, world!").unwrap();
    let b_is_5_prime = is_prime(5);
    hprintln!("is_prime(5) == {}",b_is_5_prime);

    debug::exit(debug::EXIT_SUCCESS);

    loop {
        // your code goes here
    }
}

fn is_prime(n_prime_candidate: i32) -> bool {
    if n_prime_candidate == 1 {
        return false;
    }
    //attribution: several solutions posted here https://exercism.org/tracks/rust/exercises/nth-prime/solutions?page=1
    !(2..(n_prime_candidate/2 + 1)).any(|n_possible_divisor| (n_prime_candidate % n_possible_divisor) == 0)
}
