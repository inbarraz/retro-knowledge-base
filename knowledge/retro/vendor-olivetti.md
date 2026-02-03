# Olivetti

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| M24 | Desktop Computer (8086) | [3DbmGtHJ-Wc] |
| M280 | Desktop Computer (286) | [3DbmGtHJ-Wc] |
| PC1 | All-in-One Computer | [3DbmGtHJ-Wc] |

## Platform-Specific Knowledge

### Olivetti M24 / AT&T PC6300

#### Overview
- 8086-based PC from 1984 - Source: [3DbmGtHJ-Wc]
- Sold in US as AT&T PC6300 (rebranded) - Source: [3DbmGtHJ-Wc]
- Made in Italy - Source: [3DbmGtHJ-Wc]
- Used in schools in Italy - Source: [3DbmGtHJ-Wc]

#### Architecture
- 8086 processor (full 16-bit external bus) - Source: [3DbmGtHJ-Wc]
- Standard 8-bit ISA slots PLUS proprietary 16-bit extension connector - Source: [3DbmGtHJ-Wc]
- Extension connector brings extra data lines for 16-bit performance - Source: [3DbmGtHJ-Wc]
- Main motherboard on BOTTOM of case - Source: [3DbmGtHJ-Wc]
- Backplane on TOP connects via ribbon cables/risers to motherboard - Source: [3DbmGtHJ-Wc]

#### Memory
- 512K + 128K on motherboard = 640K total - Source: [3DbmGtHJ-Wc]
- 16-bit RAM expansion boards available (use proprietary extension) - Source: [3DbmGtHJ-Wc]
- RAM expansion board holds up to 384KB (64K DRAM chips + parity) - Source: [3DbmGtHJ-Wc]

#### Video
- Dedicated 16-bit video board - Source: [3DbmGtHJ-Wc]
- 6545 CRT controller chip - Source: [3DbmGtHJ-Wc]
- 32KB video RAM (41416 chips) - Source: [3DbmGtHJ-Wc]
- 25-pin monitor connector (proprietary, not standard DE-9) - Source: [3DbmGtHJ-Wc]
- 24kHz video output - Source: [3DbmGtHJ-Wc]

#### Known Issues
- NiCad battery leakage - battery WILL leak and corrode traces - Source: [3DbmGtHJ-Wc]
- Remove battery and neutralize corrosion ASAP - Source: [3DbmGtHJ-Wc]
- Trace repair may be needed in battery area - Source: [3DbmGtHJ-Wc]

#### Keyboard
- Uses 9-pin connector (not standard DIN) - Source: [3DbmGtHJ-Wc]

### Olivetti M280

#### Overview
- 286 (12MHz) version of M24 architecture - Source: [3DbmGtHJ-Wc]
- Unknown if sold in US by AT&T - Source: [3DbmGtHJ-Wc]
- Gray color scheme vs beige M24 - Source: [3DbmGtHJ-Wc]

#### Architecture
- Has 16-bit ISA slots AND old M24 16-bit extension slots - Source: [3DbmGtHJ-Wc]
- Some backplane revisions have different connector configurations - Source: [3DbmGtHJ-Wc]
- Uses standard VGA cards (no proprietary video board needed) - Source: [3DbmGtHJ-Wc]
- Still uses 9-pin keyboard connector - Source: [3DbmGtHJ-Wc]

#### Case Design
- Front panel hinges down - Source: [3DbmGtHJ-Wc]
- Screw holes on top lid for mounting monitor directly - Source: [3DbmGtHJ-Wc]
- Drive bay uses A/C labeling for floppy/hard drive configuration - Source: [3DbmGtHJ-Wc]

### Olivetti Prodest PC1

#### Overview
- Wedge-type all-in-one XT clone with keyboard and floppy drive - Source: [3DbmGtHJ-Wc], [6YU9IUAsIrE]
- Never sold in US (as far as known) - Source: [3DbmGtHJ-Wc]
- Italian design - Source: [6YU9IUAsIrE]
- 220V power supply (failing caps common issue) - Source: [6YU9IUAsIrE]
- Ports: Mouse (proprietary), Serial, Parallel, Sound output, Video DIN - Source: [6YU9IUAsIrE]
- Volume slider inside case - Source: [6YU9IUAsIrE]
- One or two floppy drives (pop-up style), or hard drive option - Source: [6YU9IUAsIrE]

#### Video Chip (Yamaha V6355D)
- Hidden 16-color graphics capability using 512-color palette - Source: [6YU9IUAsIrE]
- Similar to PC Junior special modes - Source: [6YU9IUAsIrE]
- Can output analog RGB via SCART cable (not just TTL RGBI) - Source: [6YU9IUAsIrE]
- 9-bit RGB palette (like MSX) - Source: [6YU9IUAsIrE]
- Italian enthusiasts made EGA-like demos unlocking these features - Source: [6YU9IUAsIrE]
- 16KB video RAM limits to 160x200 at 16 colors - Source: [6YU9IUAsIrE]
- Chip capable of 640x200 but requires external circuits and more VRAM - Source: [6YU9IUAsIrE]
- Same chip used on some CGA cards - Source: [6YU9IUAsIrE]

#### ISA Riser Card
- Available aftermarket riser (ISA riser v1.3) - Source: [6YU9IUAsIrE]
- Hackaday.io project: spark2K06 - Source: [6YU9IUAsIrE]
- Allows two ISA cards perpendicular to computer - Source: [6YU9IUAsIrE]
- Good for PicoMEM, PicoGUS, XT-IDE - Source: [6YU9IUAsIrE]

### Olivetti PC1 Mouse

#### Mouse Type
- Logitech OEM mouse for PC1 - Source: [3XApa-s1nhc]
- Yellow buttons match PC1 function key colors - Source: [3XApa-s1nhc]
- Same case as regular Logitech serial mouse (different circuitry) - Source: [3XApa-s1nhc]

#### Interface
- Not a standard serial mouse - Source: [3XApa-s1nhc]
- Interfaces directly to video chip which handles mouse - Source: [3XApa-s1nhc]
- Uses quadrature encoding (like Atari ST, Amiga mice) - Source: [3XApa-s1nhc]
- Simple adapter could convert Atari/Amiga mouse to work - Source: [3XApa-s1nhc]
- AT&T 6300 uses same quadrature bus mouse - Source: [3XApa-s1nhc]

#### Historical Note
- One of three Logitech founders was former Olivetti engineer - Source: [3XApa-s1nhc]
- Olivetti and HP were Logitech's first big OEM mouse contracts - Source: [3XApa-s1nhc]

## Repair Notes

### Board Quality
- Italian manufacturing with mix of chip sources (Siemens/SAB, SGS Italian chips) - Source: [3DbmGtHJ-Wc]
- Some boards have surface mount passives on back (unusual for era) - Source: [3DbmGtHJ-Wc]
- Many boards have bodge wires (typical for production revisions) - Source: [3DbmGtHJ-Wc]

### Power Distribution
- Power carried via large lugs between backplane boards and motherboard - Source: [3DbmGtHJ-Wc]
- Video board may carry power from PSU to motherboard via lugs - Source: [3DbmGtHJ-Wc]
