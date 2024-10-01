# Description

Now with a twist!

# Approach

This problem is very similar to [runway1](https://github.com/adieos/ctf-writeups/tree/main/BuckeyeCTF%202024/%5Bpwn%5D%20runway1), just with a little addition. We are asked
to call the `win()` function as well as to pass additional parameters with predefined values. 

The approach is similar. After we specify our `win()` function address in our payload, we need to specify the return address directly after the `win()` address. Afterwards, we
can specify the values of the function's parameters. Keep in mind that this approach will not work in 64-bit systems.

![image](https://github.com/user-attachments/assets/3c45dcf8-0952-462c-b69a-49c37c59f845)

# Flag

`bctf{I_m1sS_4r1thm3t1c_qu1ZZ3s_2349adb53baa2955}`
