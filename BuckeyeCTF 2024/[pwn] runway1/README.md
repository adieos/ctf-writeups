# Description

Starting to ramp up!

# Approach

The source code indicates a classic `ret2win` problem where we are tasked to call a `win()` function in order to obtain the flag.
Upon inspecting the file security with `checksec`, we found this:

![image](https://github.com/user-attachments/assets/871f2c63-ffe4-400e-8cca-af0f068ea719)

Since the PIE and stack canary protection are not enabled, we can overflow the buffer and overwrite the return address with the
fixed `win()` address. But first, we need to determine the offset. We can use this string to do it:

`aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaaa`

using `gdb` to run it, we get the following:

![image](https://github.com/user-attachments/assets/baaea648-5217-4638-83d9-392cd5413438)

`SIGSEGV` (Signal 11) occurs when the program tries to access an invalid memory location. We can speculate that we have overwritten
something to cause the program to crash. Next, we can check the registers with `info registers`.

![image](https://github.com/user-attachments/assets/13db9b67-94cd-4ab6-8c1b-4650f9d6ec6b)

Take a look at the special register `eip`. It is a register used in 32-bit architecture systems that holds the address of the next
instruction. Since `0x61616174` corresponds to `aaat`, we know that the `taaa` part in our payload overwrote the `eip`, thus now we know
where to put the address of `win()` to call it.

With the help of `pwntools`, a python library, we can send our crafted payload to the remote server and call the `win()` function.

![image](https://github.com/user-attachments/assets/3fe6cd86-7e9f-45f5-bff4-34586966e44b)

# Flag

`bctf{I_34t_fl4GS_4_bR34kf4st_7c639e33ffcfe8c2}`
