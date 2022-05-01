qemu-system-arm -cpu cortex-m3 -machine lm3s6965evb -nographic -semihosting-config enable=on,target=native -gdb tcp::3333 -S -kernel target/thumbv7m-none-eabi/debug/d5-rust-qemu-eval
