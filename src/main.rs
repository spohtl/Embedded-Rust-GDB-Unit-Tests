#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics

use cortex_m::asm;
use cortex_m_rt::entry;
use cortex_m_semihosting::{debug, hprintln};

#[entry]
fn main() -> ! {
    hprintln!("Hello, world!").unwrap();
    let b_is_5_prime = is_prime(5);
    hprintln!("is_prime(5) == {}",b_is_5_prime).expect("error printing");

    debug::exit(debug::EXIT_SUCCESS); // for QEMU only

    loop {
    }
}

fn is_prime(n_prime_candidate: i32) -> bool {
    // special case handling to fix the faulty one-liner below. Comment out to break CI
    if n_prime_candidate == 1 {
        return false;
    }
    
    //attribution: several solutions posted here https://exercism.org/tracks/rust/exercises/nth-prime/solutions?page=1
    !(2..(n_prime_candidate/2 + 1)).any(|n_possible_divisor| (n_prime_candidate % n_possible_divisor) == 0)
}
