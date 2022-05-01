sh start_qemu.sh & > /dev/null
gdb-multiarch -q target/thumbv7m-none-eabi/debug/d5-rust-qemu-eval -x test/unit_tests_gdb.py
