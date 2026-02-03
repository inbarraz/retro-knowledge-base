# Generic Kit Computers / Homebrew Systems

This file documents knowledge about kit computers, homebrew systems, and DIY construction techniques from the 1970s-1980s era that don't belong to a specific commercial vendor.

## Construction Techniques

### Hand-Wired Boards
- Enamel-coated copper wire used for hand wiring - very thin, almost like transformer wire - Source: [_muHEAJ7dko]
- Wire-wrap construction common on perf boards - Source: [_muHEAJ7dko]
- Solder wick sometimes used as ground lead reinforcement on PCB traces - Source: [_muHEAJ7dko]
- Hand-bent IC pins indicate manual modifications or connections to other boards - Source: [_muHEAJ7dko]

### Board Identification
- Look for "Made in USA" markings on hobbyist/kit boards - Source: [_muHEAJ7dko]
- Bus connector pin markings (e.g., "A through R" and "S through E") help identify bus type - Source: [_muHEAJ7dko]
- Quarter-turn fasteners (like IKEA furniture) used on some enclosures - Source: [_muHEAJ7dko]
- Posts on bus connectors make troubleshooting easy - can clip logic probes directly - Source: [_muHEAJ7dko]

### Riser/Extender Cards
- Riser cards allow working on cards outside chassis while powered - Source: [_muHEAJ7dko]
- Used for troubleshooting - raise card up for oscilloscope/logic probe access - Source: [_muHEAJ7dko]

## Power Supply Design

### Local Voltage Regulation
- Cards needing -5V often use 7905 regulators locally - Source: [_muHEAJ7dko]
- Main backplane may only provide +5V, +12V, -12V - Source: [_muHEAJ7dko]
- Individual cards convert rails as needed (e.g., -12V input to -5V locally) - Source: [_muHEAJ7dko]
- Linear regulators common, often mounted on heatsinks - Source: [_muHEAJ7dko]

### Power Supply Components
- Large Tektronix transformers used in some homebrew supplies - Source: [_muHEAJ7dko]
- Bridge rectifier and large filter capacitors for DC conversion - Source: [_muHEAJ7dko]
- Homemade power supplies can be "scary" - may have modifications - Source: [_muHEAJ7dko]

## Z80-Based Systems

### Common Support Chips
- Z80 PIO: Parallel I/O chip - Source: [_muHEAJ7dko]
- Z80 SIO: Serial I/O chip - Source: [_muHEAJ7dko]
- Z80 CTC: Counter/Timer Circuit (for programmable timers, NOT real-time clock) - Source: [_muHEAJ7dko]
- MOS Technology MK3850: Found in some Z80 systems - Source: [_muHEAJ7dko]
- MOS Technology MK9007/MK9004: Support chips - Source: [_muHEAJ7dko]

### Serial Communications
- Intersil IM6402: UART (asynchronous receiver/transmitter) - Source: [_muHEAJ7dko]
- MC14411: Motorola baud rate generator (also used in Color Computer) - Source: [_muHEAJ7dko]
- Terminal-based operation common (no built-in video controller) - Source: [_muHEAJ7dko]
- Multiple serial cards possible in one system - Source: [_muHEAJ7dko]

### CP/M Configuration
- Typical to have 64K of RAM - Source: [_muHEAJ7dko]
- ROMs get bank-switched out during operation - Source: [_muHEAJ7dko]
- Boot ROMs may have limited bootstrap capability - Source: [_muHEAJ7dko]
- Without boot disks, getting CP/M machines running is very difficult - Source: [_muHEAJ7dko]

## Floppy Controller

### NEC 765
- Very common floppy controller chip - Source: [_muHEAJ7dko]
- PC compatible for double density use - Source: [_muHEAJ7dko]
- Used on PC Junior and many IBM PCs - Source: [_muHEAJ7dko]
- Floppy controller boards often include RAM (64K HM4864A common) - Source: [_muHEAJ7dko]
- 8-inch disk drives used on some CP/M systems - Source: [_muHEAJ7dko]

## Memory

### RAM Chips
- TMS4051: 8K RAM chips (less common than 4116/4164) - Source: [_muHEAJ7dko]
- 8 TMS4051 chips = 8K total RAM - Source: [_muHEAJ7dko]
- HM4864A-12: 64K RAM chips - Source: [_muHEAJ7dko]
- Sony CXK58100P: SRAM chip (found on 1986-era expansion) - Source: [_muHEAJ7dko]

### EPROM Chips
- 2708 EPROMs: Require +5V, -5V, AND +12V to read - Source: [_muHEAJ7dko]
- 2764 EPROMs: Sometimes found in white ceramic packages - Source: [_muHEAJ7dko]
- Standard programmers like TL866II Plus cannot read 2708s without bias voltages - Source: [_muHEAJ7dko]
- Retro Chip Tester Pro can potentially read/write 2708s with correct add-on board - Source: [_muHEAJ7dko]

### Socket Types
- Press-fit sockets: Slightly larger PCB holes, socket on bottom, pins on top appear larger - Source: [_muHEAJ7dko]
- Chips push into these non-standard looking sockets - Source: [_muHEAJ7dko]

## Clock/RTC Boards

### Components
- MM58167AN: Clock chip - Source: [_muHEAJ7dko]
- 32.768 kHz crystal paired with clock chip - Source: [_muHEAJ7dko]

### Battery Issues
- NiCad batteries (e.g., SAFT brand) common for clock backup - Source: [_muHEAJ7dko]
- NiCad leakage causes visible corrosion around battery area - Source: [_muHEAJ7dko]
- Battery damage can affect nearby components on same board - Source: [_muHEAJ7dko]

## EPROM Programmer Boards

### Identification
- ZIF (Zero Insertion Force) socket indicates programmer - Source: [_muHEAJ7dko]
- "Programming" LED indicator - Source: [_muHEAJ7dko]
- Address lines and data lines labeled on board - Source: [_muHEAJ7dko]
- Separate voltage regulation for programming voltages - Source: [_muHEAJ7dko]

## Bus Standards

### S-100 vs Other Buses
- S-100 cards do NOT have a center notch in the edge connector - Source: [_muHEAJ7dko]
- S-100 cards are physically larger than some other standards - Source: [_muHEAJ7dko]
- Altair and MITS machines used S-100 with standardized voltage rails - Source: [_muHEAJ7dko]
- Non-S-100 custom backplanes make machine identification difficult - Source: [_muHEAJ7dko]
- Cards with center notch in edge connector are NOT S-100 - Source: [_muHEAJ7dko]

### Unknown Bus Challenges
- Without pinout documentation, powering unknown systems is risky - Source: [_muHEAJ7dko]
- Community knowledge often needed to identify obscure bus standards - Source: [_muHEAJ7dko]

## Diagnostic Approach for Unknown Systems

1. Identify bus type by card edge connector shape and pin labels - Source: [_muHEAJ7dko]
2. Look for date codes on chips to estimate system age - Source: [_muHEAJ7dko]
3. Identify CPU and support chips to determine architecture - Source: [_muHEAJ7dko]
4. Look for serial ports (likely terminal-based if no video controller found) - Source: [_muHEAJ7dko]
5. Check for boot ROM labels (e.g., "CPM BOOT BOOT ROM") - Source: [_muHEAJ7dko]
6. Document all boards with high-resolution photos for community help - Source: [_muHEAJ7dko]
7. Post to online communities for identification assistance - Source: [_muHEAJ7dko]

## Modern Replica Computers

### IMSAI 8080 Replica (The High Nibble)

#### Overview
- ESP32-based IMSAI 8080 front panel simulation - Source: [zLVlD6ELhNE]
- Created by David at thehighnibble.com (Australia) - Source: [zLVlD6ELhNE]
- Price: $280 USD (plus shipping from Australia) - Source: [zLVlD6ELhNE]
- Kit form, requires assembly - Source: [zLVlD6ELhNE]
- First batches shipped 2019 - Source: [zLVlD6ELhNE]
- Low volume, handmade by creator - Source: [zLVlD6ELhNE]

#### Hardware Components
- ESP32 dual-core CPU with 4MB flash - Source: [zLVlD6ELhNE]
- 16GB micro SD card included - Source: [zLVlD6ELhNE]
- Authentic-looking front panel (cut acrylic with printed graphics) - Source: [zLVlD6ELhNE]
- Real toggle switches (up/down) for front panel - Source: [zLVlD6ELhNE]
- LEDs behind red window panels - Source: [zLVlD6ELhNE]
- Metal case (shallow depth, fits on shelf) - Source: [zLVlD6ELhNE]
- Hat PCB plugs onto ESP32 - Source: [zLVlD6ELhNE]
- DB9 connectors for serial ports - Source: [zLVlD6ELhNE]
- 74HC595 shift registers for I/O - Source: [zLVlD6ELhNE]

#### Kit Quality
- Excellent packaging with cardboard cutouts for parts - Source: [zLVlD6ELhNE]
- Switches fit perfectly in cardboard holder - Source: [zLVlD6ELhNE]
- Warning labels about sharp acrylic edges and small parts - Source: [zLVlD6ELhNE]

#### Software Features (imsaisim)
- Full IMSAI 8080 simulation - Source: [zLVlD6ELhNE]
- CP/M 2.2 included - Source: [zLVlD6ELhNE]
- Four simulated 8-inch floppy drives - Source: [zLVlD6ELhNE]
- Boot ROM emulation - Source: [zLVlD6ELhNE]
- Hard disk emulation - Source: [zLVlD6ELhNE]
- Virtual modem over TCP/IP - Source: [zLVlD6ELhNE]
- Serial port for real terminal connection - Source: [zLVlD6ELhNE]

#### Web Interface
- Full control via web browser - Source: [zLVlD6ELhNE]
- Multiple terminal emulation modes (TTY, CRT look) - Source: [zLVlD6ELhNE]
- Virtual front panel switches in UI - Source: [zLVlD6ELhNE]
- Load floppy disk images - Source: [zLVlD6ELhNE]
- Simulated printer output (line printer with bar paper graphics) - Source: [zLVlD6ELhNE]
- Dazzler graphics output emulation - Source: [zLVlD6ELhNE]
- Full screen mode hides browser chrome - Source: [zLVlD6ELhNE]

#### Physical Design
- Authentic front panel appearance - Source: [zLVlD6ELhNE]
- Shallow case depth (much less than original IMSAI) - Source: [zLVlD6ELhNE]
- LEDs blink during code execution - Source: [zLVlD6ELhNE]
- Can enter programs from physical front panel - Source: [zLVlD6ELhNE]
- Great for shelf display or Zoom background - Source: [zLVlD6ELhNE]

#### Advantages Over Original IMSAI
- Very reliable (won't break down like vintage hardware) - Source: [zLVlD6ELhNE]
- Low power consumption - Source: [zLVlD6ELhNE]
- Web browser access from any device - Source: [zLVlD6ELhNE]
- Compact size fits easily on shelf - Source: [zLVlD6ELhNE]
- Software regularly updated with new features - Source: [zLVlD6ELhNE]

#### Ordering
- Contact: info@thehighnibble.com - Source: [zLVlD6ELhNE]
- Website: thehighnibble.com/imsai8080 - Source: [zLVlD6ELhNE]
- GitHub: github.com/thehighnibble - Source: [zLVlD6ELhNE]
