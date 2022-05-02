# Embedded Rust GDB Unit Tests

## About

This is a tiny proof-of-concept sample running Embedded Rust on QEMU with a CI setup using GitHub Actions.
The catch is that the unit tests used in CI are not running on the emulated hardware, but rather scripted through GDB's Python API.

The application itself is the QEMU demo described in [The Embedded Rust Book](https://docs.rust-embedded.org/book/start/qemu.html),
running on an emulated LM3S6965 development board.

## Why

This approach removes the need to bloat the target app with a test harness, which has the potential to be destructive in a resource-constrained environment.
It is the approach taken by commercial programs like [testIDEA](https://www.isystem.com/products/software/testidea.html).
I wanted to see how easy it was to get close to the functionality such programs provide by using only freely available open-source tools.

I found out that, for very simple parameter-outcome unit tests, GDB with the Python API and Python's `unittest` module gives a reasonably good user experience.
Result ("return value") parsing is an area where I anticipate the most complications if this were to be expanded into general use.
A wrapper library for this use case would therefore probably be a good idea if this approach is to be evaluated further.

## Prerequisites

In addition to `cargo` and `rustc`, you will need:

- ARM Cortex-M3 cross-compilation support
  - `rustup target add thumbv7m-none-eabi`
- gdb-multiarch, QEMU and openocd
  - `sudo apt install gdb-multiarch openocd qemu-system-arm`
- Python3 with the `unittest` module (included in most Python3 installations)

## Development

To build the project, run `cargo build`

To run the project, run `cargo run`

To debug the project, open two terminals. Run `./start_qemu.sh` in one and `./start_gdb.sh` in the other.
QEMU is set to stop at the first instruction so it should produce no output. To run the app, run `continue` in the GDB terminal.

## Testing

To run tests, run `./run_tests.sh`.

The script will first start QEMU, then invoke the Python script located in `test/`. The script will connect to QEMU through GDB, set a breakpoint at `main`,
then run all the unit tests, resetting the target to `Reset` and letting it run back to `main` between each test. It will exit with a status of 0 if all tests pass and 1 if there was a failure.
Despite my best efforts to keep GDB output to a minimum, there will be some unhelpful log messages printed by GDB as it runs through the tests.

## License

- MIT license (http://opensource.org/licenses/MIT)
