# Description

If you've never done a CTF before, this runway should help!

# Approach

![image](https://github.com/user-attachments/assets/1f0ee8cf-ccc6-4e24-ad72-069357ca3b85)

The program takes an input from the user and wraps it with double quotes ("). Then, the result is directly concatenated with the
terminal command "cowsay". We can manually wrap our input with our own double quotes and run an arbitrary command afterwards, including
spawning a shell. By simply ending our input with `"; /bin/sh`, we can spawn a shell and retrieve the flag.

![image](https://github.com/user-attachments/assets/7db60a7c-5530-431e-b1f8-456a6310b1e6)

# Flag

`bctf{0v3rfl0w_th3_M00m0ry_2d310e3de286658e}`
