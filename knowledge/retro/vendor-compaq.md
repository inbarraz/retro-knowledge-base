# Compaq

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Portable III | Luggable Computer | [gNbM0UzWrnQ] |
| Luggable II | Luggable Computer | [gNbM0UzWrnQ] |
| Presario 425 | Desktop Computer | [WgxFL0zSW-w] |

## Platform-Specific Knowledge

### Compaq Portable III

#### Overview
- 286 processor at 12MHz - Source: [gNbM0UzWrnQ]
- Orange gas plasma display (built-in) - Source: [gNbM0UzWrnQ]
- ISA expansion slots inside chassis - Source: [gNbM0UzWrnQ]
- Heavy "luggable" portable form factor - Source: [gNbM0UzWrnQ]
- Evolution of the original Compaq Portable line - Source: [gNbM0UzWrnQ]

#### Comparison to Portable II
- Faster processor (12MHz vs 8MHz) - Source: [gNbM0UzWrnQ]
- Similar form factor and display technology - Source: [gNbM0UzWrnQ]
- Compatible with standard ISA cards internally - Source: [gNbM0UzWrnQ]

### Compaq Luggable II

#### Overview
- Mentioned alongside Portable III - Source: [gNbM0UzWrnQ]
- Early luggable portable computer - Source: [gNbM0UzWrnQ]
- Gas plasma display technology - Source: [gNbM0UzWrnQ]

### Compaq Presario 425

#### Overview
- 486 class desktop computer - Source: [WgxFL0zSW-w]
- Originally 25MHz, upgradeable to 33MHz - Source: [WgxFL0zSW-w]
- Has integrated 486SX on motherboard - Source: [WgxFL0zSW-w]
- No L2 cache on motherboard (limits performance) - Source: [WgxFL0zSW-w]
- Can take standard CPUs in 487SX coprocessor socket - Source: [WgxFL0zSW-w]
- Has jumper to disable onboard 486SX when upgrade installed - Source: [WgxFL0zSW-w]

#### CPU Upgrade Options

##### Intel Overdrive DX4 100MHz
- Runs at 3.3V (motherboard supplies 5V, has onboard voltage regulator) - Source: [WgxFL0zSW-w]
- 3x multiplier on 33MHz bus = 100MHz - Source: [WgxFL0zSW-w]
- Has integrated heatsink (no fan needed) - Source: [WgxFL0zSW-w]
- Increases L1 cache from 8KB to 16KB - Source: [WgxFL0zSW-w]
- Voltage regulator mounted under heatsink on CPU - Source: [WgxFL0zSW-w]

##### ODPR vs ODP Variants
- ODP (OverDrive Processor): Has extra pin towards middle of CPU - Source: [WgxFL0zSW-w]
- ODPR (OverDrive Processor Replacement): No extra pin, more versatile - Source: [WgxFL0zSW-w]
- Extra pin makes chip PGA-169 vs standard PGA-168 - Source: [WgxFL0zSW-w]
- Some motherboard sockets have that position blanked out - Source: [WgxFL0zSW-w]
- ODPR works in any socket, ODP needs socket with hole for extra pin - Source: [WgxFL0zSW-w]
- Extra pin just disables onboard CPU (same as jumper does) - Source: [WgxFL0zSW-w]
- "R" in ODPR = Replacement - Source: [WgxFL0zSW-w]

##### Voltage Considerations
- DX2-66 and slower 486s run at 5V - Source: [WgxFL0zSW-w]
- DX4 and faster 486s run at 3.3V - Source: [WgxFL0zSW-w]
- Cannot put regular DX4 in 5V socket - will damage chip - Source: [WgxFL0zSW-w]
- Overdrive chips have built-in voltage regulation - Source: [WgxFL0zSW-w]
- AMD 80MHz 486 also 3.3V - not compatible without voltage adapter - Source: [WgxFL0zSW-w]

#### Performance Notes
- L1 cache speed matches CPU clock (102MB/s at 100MHz) - Source: [WgxFL0zSW-w]
- Main memory limited by 33MHz bus speed - Source: [WgxFL0zSW-w]
- Lack of L2 cache significantly limits performance - Source: [WgxFL0zSW-w]
- 100MHz DX4 still struggles with demanding MOD files (many channels) - Source: [WgxFL0zSW-w]
- 4-channel MODs play perfectly, 16+ channel struggle - Source: [WgxFL0zSW-w]

## Sound Card Troubleshooting

### OPL Hanging Note Problem

#### The Problem
- Ctrl+Alt+Delete to reboot during AdLib/OPL music leaves note playing - Source: [WgxFL0zSW-w]
- Happens with Sound Blaster cards and original AdLib cards - Source: [WgxFL0zSW-w]
- Note continues playing through reboot until cleared - Source: [WgxFL0zSW-w]
- Annoying problem that existed since original Sound Blaster era - Source: [WgxFL0zSW-w]

#### Fix: RESETOPL Utility
- GitHub: github.com/stargo/resetopl - Source: [WgxFL0zSW-w]
- Small utility that resets OPL chips on sound card - Source: [WgxFL0zSW-w]
- Run from AUTOEXEC.BAT or command line - Source: [WgxFL0zSW-w]
- Clears hanging notes on boot - Source: [WgxFL0zSW-w]
- Recommended for any DOS PC with OPL-based sound card - Source: [WgxFL0zSW-w]
