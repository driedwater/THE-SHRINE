[prof cane]

1ai) cant be assed. jpg got JFIF header

1iii)

solve w the following script:

```
data = open('testfile1_Sep2024', 'rb').read()

for char in data:
    print(chr(char & 0b01111111), end='')
```

1bi) test2 is float test3 is decimal repr
bii) 
for 2nd test file (float reprs), 8 seconds is represented by 32 bytes, so 1 second is represented by 4 bytes

seconds in a 10 hr flight = 10hr * 60min/hr * 60sec/min
                          = 36 000 secs

filesize of 2nd testfile = 36 000 secs * 4bytes/sec
                         = 144 000 bytes
                         = 140.625 Kb //

for 3rd file (decimal reprs), 8 seconds is represented by 98 bytes, so 1 second is represented by 12.25 bytes

filesize of 2ndtesfile = 36 000 secs * 12.25bytes/sec
                        = 441 000 bytes
                        = 430.66 Kb //

1c)

```
[-(zen's icebox)-[~/…/the-shrine/inf1001/inf1001_lab/cane_lab1]
[-$ head -c 256 testfile4_Sep2024 | xxd
00000000: 5249 4646 46f0 e400 5741 5645 666d 7420  RIFFF...WAVEfmt 
00000010: 1000 0000 0100 0200 44ac 0000 10b1 0200  ........D.......
00000020: 0400 1000 4c49 5354 1a00 0000 494e 464f  ....LIST....INFO
00000030: 4953 4654 0d00 0000 4c61 7666 3631 2e35  ISFT....Lavf61.5
00000040: 2e31 3031 0000 6461 7461 00f0 e400 0000  .101..data......
```

magic bytes `riff` and `wave` indicate that this is a .wav file
```
[-(zen's icebox)-[~/…/the-shrine/inf1001/inf1001_lab/cane_lab1]
[-$ head -c 256 testfile5_Sep2024 | xxd
00000000: 0000 0018 6674 7970 6d70 3432 0000 0000  ....ftypmp42....
00000010: 6d70 3432 6973 6f6d 0000 0018 6265 616d  mp42isom....beam
00000020: 0100 0000 0100 0000 0000 0000 0200 0000  ................
00000030: 0000 0d57 6d6f 6f76 0000 006c 6d76 6864  ...Wmoov...lmvhd
00000040: 0000 0000 0000 0000 0000 0000 0000 bb80  ................
00000050: 0003 e400 0001 0000 0100 0000 0000 0000  ................
00000060: 0000 0000 0001 0000 0000 0000 0000 0000  ................
00000070: 0000 0000 0001 0000 0000 0000 0000 0000  ................
00000080: 0000 0000 4000 0000 0000 0000 0000 0000  ....@...........
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000a0: 0000 0003 0000 06c6 7472 616b 0000 005c  ........trak...\
000000b0: 746b 6864 0000 0007 0000 0000 0000 0000  tkhd............
000000c0: 0000 0001 0000 0000 0003 e468 0000 0000  ...........h....
000000d0: 0000 0000 0000 0000 0100 0000 0001 0000  ................
000000e0: 0000 0000 0000 0000 0000 0000 0001 0000  ................
000000f0: 0000 0000 0000 0000 0000 0000 4000 0000  ............@...
```

magic bytes `ftymp42` say its an mp4 file
