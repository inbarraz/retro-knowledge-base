# Tyan

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| S1562D Tomcat II | Motherboard | [Li2xFBGbzZQ] |

## Platform-Specific Knowledge

### Tyan S1562D Tomcat II

#### Overview
- Dual Pentium Socket 5 motherboard - Source: [Li2xFBGbzZQ]
- Designed for dual-processor workstation/server use - Source: [Li2xFBGbzZQ]
- Common platform for early Windows NT and Unix workstations - Source: [Li2xFBGbzZQ]
- Supports Intel Pentium processors up to 133MHz - Source: [Li2xFBGbzZQ]

#### Socket Configuration
- Two Socket 5 CPU sockets - Source: [Li2xFBGbzZQ]
- Can run with single CPU (second socket empty) - Source: [Li2xFBGbzZQ]
- Both CPUs must be same speed for dual operation - Source: [Li2xFBGbzZQ]
- VRM (Voltage Regulator Module) required for each CPU - Source: [Li2xFBGbzZQ]

#### RAM Configuration
- Uses 72-pin SIMMs - Source: [Li2xFBGbzZQ]
- Multiple SIMM banks - Source: [Li2xFBGbzZQ]
- Supports both Fast Page and EDO RAM - Source: [Li2xFBGbzZQ]
- Mixed RAM types can cause strange behavior - Source: [Li2xFBGbzZQ]

#### Known Issues

##### Dallas RTC Chip Dead
- Uses Dallas DS1287 integrated RTC - Source: [Li2xFBGbzZQ]
- Internal battery fails after ~20 years - Source: [Li2xFBGbzZQ]
- Symptoms: CMOS checksum error, clock resets - Source: [Li2xFBGbzZQ]
- Replace with NecroWare Dallas replacement module - Source: [Li2xFBGbzZQ]

##### RAM Compatibility Issues
- Bad or mismatched RAM causes strange crashes - Source: [Li2xFBGbzZQ]
- System may boot but crash randomly during use - Source: [Li2xFBGbzZQ]
- Test each SIMM individually in different banks - Source: [Li2xFBGbzZQ]
- Mix of EDO and FP may work but not recommended - Source: [Li2xFBGbzZQ]

##### Symptoms of Bad RAM
- Random crashes during memory-intensive operations - Source: [Li2xFBGbzZQ]
- Blue screen errors in Windows - Source: [Li2xFBGbzZQ]
- Corruption in file operations - Source: [Li2xFBGbzZQ]
- May pass quick RAM tests but fail extended tests - Source: [Li2xFBGbzZQ]

#### Testing Recommendations
- Run extended memory tests (HIMEM, CheckIt, etc.) - Source: [Li2xFBGbzZQ]
- Test with single CPU first to isolate issues - Source: [Li2xFBGbzZQ]
- Verify all SIMMs are same type and speed - Source: [Li2xFBGbzZQ]
- Check VRM modules for proper voltage output - Source: [Li2xFBGbzZQ]

#### BIOS
- Award BIOS typical for this era - Source: [Li2xFBGbzZQ]
- Settings for cache, shadow, CPU configuration - Source: [Li2xFBGbzZQ]
- May need BIOS update for some Pentium revisions - Source: [Li2xFBGbzZQ]

## Dual Pentium Motherboard Notes

### Single vs Dual CPU Operation
- DOS doesn't use second CPU (single-threaded OS) - Source: [Li2xFBGbzZQ]
- Windows NT and Unix can use both CPUs - Source: [Li2xFBGbzZQ]
- Second CPU useful for running multiple DOS sessions under Windows - Source: [Li2xFBGbzZQ]
- Can run with single CPU for troubleshooting - Source: [Li2xFBGbzZQ]

### Socket 5 CPU Compatibility
- Pentium 60-133MHz supported - Source: [Li2xFBGbzZQ]
- Overdrive processors may work - Source: [Li2xFBGbzZQ]
- Socket 7 CPUs (MMX Pentium) NOT compatible - Source: [Li2xFBGbzZQ]
- Check voltage requirements - early Pentiums used different voltages - Source: [Li2xFBGbzZQ]
