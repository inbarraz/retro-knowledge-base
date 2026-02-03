# Memory and Processor Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Memory](#memory)
- [CPU Overclocking (Vintage Systems)](#cpu-overclocking-vintage-systems)
- [TTL Logic Compatibility](#ttl-logic-compatibility)
- [XT/AT RAM Testing](#xtat-ram-testing)
- [Intel Pentium Overdrive Processors](#intel-pentium-overdrive-processors)
- [ISA Memory Expansion Cards](#isa-memory-expansion-cards)

## Memory

### SIMM Adapters (SIMMverters)
- 30-pin to 72-pin SIMM adapters allow reusing old RAM in newer motherboards - Source: [-9Ae-Lbz8AA]
- Each 30-pin SIMM is 8-bit wide; 72-pin is 32-bit wide - Source: [-9Ae-Lbz8AA]
- Need 4x 30-pin SIMMs per adapter to fill 32-bit width - Source: [-9Ae-Lbz8AA]
- Pentium (64-bit data path) needs 2 adapters (8x 30-pin SIMMs) - Source: [-9Ae-Lbz8AA]
- 486 can use single adapter - Source: [-9Ae-Lbz8AA]
- Adapters are staggered/tiered to fit side-by-side in close SIMM sockets - Source: [-9Ae-Lbz8AA]
- Completely passive - no active components - Source: [-9Ae-Lbz8AA]
- Metal clip SIMM sockets preferred over plastic - Source: [-9Ae-Lbz8AA]

### SIMM Sense Pins
- 72-pin SIMMs have sense pins to tell motherboard RAM type/speed - Source: [-9Ae-Lbz8AA]
- Four pads configurable as Short (S) or Open (O) - Source: [-9Ae-Lbz8AA]
- Configuration depends on RAM size and speed (60ns, 70ns, 80ns) - Source: [-9Ae-Lbz8AA]
- Example: S-S-O-S = 80ns 4MB, O-O-O-O = 60ns 8MB - Source: [-9Ae-Lbz8AA]
- Use small wire to ground to set "short" configuration - Source: [-9Ae-Lbz8AA]

## Soviet CPU Clones

### KP1810BM88 (Soviet 8088 Clone)
- Soviet clone of Intel 8088 processor - Source: [TuDZK110nbw]
- Beautiful plastic package with distinctive Soviet styling - Source: [TuDZK110nbw]
- Functionally identical to Intel 8088 at 4.77MHz - Source: [TuDZK110nbw]
- Benchmarks exactly 1.0 on CheckIt XT scale (same as Intel) - Source: [TuDZK110nbw]
- Date codes from 1993 seen on NOS units - Source: [TuDZK110nbw]
- Runs warm during operation (may have cooling holes) - Source: [TuDZK110nbw]
- Legs may be splayed out on NOS units - form to DIP40 before insertion - Source: [TuDZK110nbw]
- Very reliable - Soviet chips built to military/government standards - Source: [TuDZK110nbw]

### Soviet Chip Quality
- Computers were rare in USSR - not sold to civilian population - Source: [TuDZK110nbw]
- Used for military, accounting centers, "fancy schools" - Source: [TuDZK110nbw]
- Built to very high standards for long-term reliability - Source: [TuDZK110nbw]
- Other Soviet clones: Z80, 8086, 2114 SRAM, 82S100 PLH - Source: [TuDZK110nbw]
- All report very high reliability in testing - Source: [TuDZK110nbw]

### Testing Soviet CPUs
- Use XT clone motherboard (must be 8088, not 8086) - Source: [TuDZK110nbw]
- 8086 and 8088 are NOT interchangeable despite same pin count - Source: [TuDZK110nbw]
- If BIOS initializes video, CPU works - Source: [TuDZK110nbw]
- CheckIt benchmark confirms speed and functionality - Source: [TuDZK110nbw]
- PC Turbo ROM useful for testing - Source: [TuDZK110nbw]

## CPU Overclocking (Vintage Systems)

### Crystal Oscillator Swapping
- Many vintage systems have socketed crystal oscillators - Source: [81ezGc1Eb1M]
- CPU speed often = crystal frequency / 2 - Source: [81ezGc1Eb1M]
- PAL crystals (17.7MHz) readily available and useful for overclocking - Source: [81ezGc1Eb1M]
- Test incrementally: if system won't POST, go back to slower crystal - Source: [81ezGc1Eb1M]

### CPU Socket Adapter Trick
- PLCC socket can be pushed into existing DIP socket without soldering - Source: [81ezGc1Eb1M]
- Allows using faster-rated CPU without permanent modification - Source: [81ezGc1Eb1M]
- Harris 286 chips run cooler than AMD at same speed - Source: [81ezGc1Eb1M]

### Stability Testing
- Run software loops (demos, games, memory tests) for hours - Source: [81ezGc1Eb1M]
- Intermittent errors indicate "ragged edge" of stability - Source: [81ezGc1Eb1M]
- Power cycling sometimes clears errors that appear after warmup - Source: [81ezGc1Eb1M]
- Landmark Speed Test useful for verifying actual CPU speed - Source: [81ezGc1Eb1M]

### Thermal Management
- Add heatsinks to CPU, DMA controller, interrupt controllers - Source: [81ezGc1Eb1M]
- Heatsinks need airflow to be effective (use case fan) - Source: [81ezGc1Eb1M]
- Monitor chip temperatures during extended operation - Source: [81ezGc1Eb1M]
- Lower RAM banks run hotter (more memory access there) - Source: [81ezGc1Eb1M]

## TTL Logic Compatibility

### HCT vs LS Chips
- 74HCT chips designed to be TTL compatible but may cause issues - Source: [81ezGc1Eb1M]
- Threshold voltage levels differ from original LS parts - Source: [81ezGc1Eb1M]
- Replace 74HCT245 with 74LS245N if experiencing compatibility problems - Source: [81ezGc1Eb1M]
- Especially important on faster AT-class machines - Source: [81ezGc1Eb1M]

## XT/AT RAM Testing

### XTRAMTEST Diagnostic ROM

#### Overview
- Open source March RAM test for XT and compatible machines - Source: [ehwtjy6skw4]
- GitHub: github.com/ki3v/xtramtest - Source: [ehwtjy6skw4]
- Replaces system BIOS ROM to run comprehensive memory test - Source: [ehwtjy6skw4]
- Can test all 640K conventional memory - Source: [ehwtjy6skw4]
- Works even with NO working motherboard RAM - Source: [ehwtjy6skw4]

#### Video Initialization
- Uses CGA or MDA video card RAM for stack pointer - Source: [ehwtjy6skw4]
- CGA: Memory at B8000h - Source: [ehwtjy6skw4]
- MDA: Memory at B0000h - Source: [ehwtjy6skw4]
- Cannot initialize EGA/VGA directly (needs BIOS calls) - Source: [ehwtjy6skw4]

#### Version 0.04 Features
- Can run as option ROM (not just BIOS replacement) - Source: [ehwtjy6skw4]
- Option ROM mode works with VGA/EGA cards - Source: [ehwtjy6skw4]
- Press T at boot prompt to start test - Source: [ehwtjy6skw4]
- Shows "SS" indicator for stack segment location - Source: [ehwtjy6skw4]
- Can be combined with XT-IDE on same ROM chip - Source: [ehwtjy6skw4]

#### Option ROM Limitations
- Requires system to POST far enough to count RAM - Source: [ehwtjy6skw4]
- Won't help if system crashes before option ROM execution - Source: [ehwtjy6skw4]
- Useful as stress test on working systems - Source: [ehwtjy6skw4]
- Good for testing expansion RAM cards - Source: [ehwtjy6skw4]

#### Test Methodology
- Uses March test algorithm - Source: [ehwtjy6skw4], [ksimpQeU3QA]
- Detects stuck bits, cross-affect errors, page errors - Source: [ehwtjy6skw4]
- Superior to basic RAM tests for detecting address line failures - Source: [ksimpQeU3QA]
- Writes and reads in specific march pattern to catch memory aliasing - Source: [ksimpQeU3QA]
- Takes longer to run but catches more subtle failures - Source: [ksimpQeU3QA]
- Errors flagged permanently (won't clear on retry) - Source: [ehwtjy6skw4]
- Good for overnight stress testing - Source: [ehwtjy6skw4]
- Also works on 286 (first 640K only) - Source: [ehwtjy6skw4]
- Same algorithm used in TRS-80 diagnostic ROM - Source: [ksimpQeU3QA]

#### Future Plans
- May combine with stripped-down open source XT BIOS - Source: [ehwtjy6skw4]
- Would allow VGA/EGA initialization before test runs - Source: [ehwtjy6skw4]
- Would still need working first 16K of RAM - Source: [ehwtjy6skw4]

### Harris vs AMD CPU Heat
- AMD 8088 CPUs run very hot - Source: [ehwtjy6skw4]
- Harris 8088 CPUs run cool (no heatsink needed) - Source: [ehwtjy6skw4]
- Heat sink on AMD can conflict with long ISA cards - Source: [ehwtjy6skw4]
- Consider Harris CPU swap if heat is a problem - Source: [ehwtjy6skw4]

### CR2032 Battery Replacement for NiCad
- Can replace rechargeable NiCad with CR2032 - Source: [ehwtjy6skw4]
- Must remove charging resistor and diode from circuit - Source: [ehwtjy6skw4]
- Different for every motherboard - trace the charging circuit - Source: [ehwtjy6skw4]
- Prevents leakage damage from old NiCad batteries - Source: [ehwtjy6skw4]

## Intel Pentium Overdrive Processors

### Overview
- Upgrades 486 motherboards to Pentium core - Source: [uXUCgOprlu0]
- 83MHz version most common (33MHz FSB × 2.5) - Source: [uXUCgOprlu0]
- Has built-in voltage regulation - runs from 5V 486 socket - Source: [uXUCgOprlu0]
- No external voltage regulator needed unlike DX4 CPUs - Source: [uXUCgOprlu0]
- Has integrated CPU fan powered from chip itself (no cable) - Source: [uXUCgOprlu0]
- Has more pins than standard 486 DX, but fits same socket - Source: [uXUCgOprlu0]

### Thermal Protection
- Built-in thermal throttling - Source: [uXUCgOprlu0]
- If fan stops, CPU automatically downclocks to prevent damage - Source: [uXUCgOprlu0]
- Fan monitor utility included with overdrive (FANMON.EXE) - Source: [uXUCgOprlu0]
- Stopping fan causes system to slow dramatically (~33MHz) - Source: [uXUCgOprlu0]
- Power cycle required to restore full speed after fan failure - Source: [uXUCgOprlu0]

### L1 Cache Compatibility Issues
- Some 486 chipsets don't properly enable Pentium's L1 cache - Source: [uXUCgOprlu0]
- Contact chipset motherboards known to have this issue - Source: [uXUCgOprlu0]
- Symptom: Much slower than expected performance - Source: [uXUCgOprlu0]
- CacheCheck utility shows only L2 (motherboard) cache working - Source: [uXUCgOprlu0]
- SETMOLE utility may help enable L1 cache on some boards - Source: [uXUCgOprlu0]
- Mr BIOS has cache enable options but may not help all boards - Source: [uXUCgOprlu0]
- Performance is terrible without L1 cache enabled - Source: [uXUCgOprlu0]
- Math speed still improved due to Pentium FPU even without L1 - Source: [uXUCgOprlu0]

### Performance Expectations
- With L1 cache: Significant improvement over 486 DX2/66 - Source: [uXUCgOprlu0]
- Without L1 cache: May be SLOWER than standard 486 DX2/66 for integer - Source: [uXUCgOprlu0]
- FPU performance always improved (Pentium FPU much faster) - Source: [uXUCgOprlu0]
- Good for Quake and other FPU-heavy games - Source: [uXUCgOprlu0]

### Foam Degradation on Pins
- Pentium Overdrive 83MHz (and similar) used foam packaging - Source: [nn76UCUIo3Q]
- Foam decomposes over decades, becomes sticky/corrosive - Source: [nn76UCUIo3Q]
- Residue on gold pins prevents good contact - Source: [nn76UCUIo3Q]
- Symptoms: CPU not recognized, random failures - Source: [nn76UCUIo3Q]

### Pin Cleaning Procedure
- Use IPA (isopropyl alcohol) and soft brush - Source: [nn76UCUIo3Q]
- Cotton swab for individual pins - Source: [nn76UCUIo3Q]
- Multiple cleaning passes may be needed - Source: [nn76UCUIo3Q]
- Inspect pins under magnification for residue - Source: [nn76UCUIo3Q]
- Clean socket contacts as well - Source: [nn76UCUIo3Q]

### General CPU Pin Care
- Never touch gold pins with bare fingers (oils) - Source: [nn76UCUIo3Q]
- Store CPUs in anti-static foam, NOT original foam packaging - Source: [nn76UCUIo3Q]
- Check any "new old stock" CPUs for foam residue - Source: [nn76UCUIo3Q]

## ISA Memory Expansion Cards

### DFI Megalith Plus Memory Card
- 8MB EMS/XMS RAM expansion via ISA slot - Source: [nn76UCUIo3Q]
- Works with 286 and 386 systems - Source: [nn76UCUIo3Q]
- Provides expanded memory for DOS applications - Source: [nn76UCUIo3Q]
- Uses EMS 4.0 specification for compatibility - Source: [nn76UCUIo3Q]
- Requires driver to use memory as extended (XMS) - Source: [nn76UCUIo3Q]
- Alternative to motherboard RAM upgrade - Source: [nn76UCUIo3Q]

### Why ISA RAM Cards
- Some motherboards have limited onboard RAM capacity - Source: [nn76UCUIo3Q]
- Cheaper than finding compatible SIMMs - Source: [nn76UCUIo3Q]
- EMS memory useful for DOS games and applications - Source: [nn76UCUIo3Q]
- Can supplement motherboard RAM rather than replace - Source: [nn76UCUIo3Q]
