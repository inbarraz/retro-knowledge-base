# Sun Microsystems

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| SPARCstation IPC | Unix Workstation | [nY38YvAMEFg] |

## Platform-Specific Knowledge

### SPARCstation IPC

#### Overview
- Compact Unix workstation - Source: [nY38YvAMEFg]
- Runs Solaris operating system - Source: [nY38YvAMEFg]
- Very small desktop form factor - Source: [nY38YvAMEFg]
- Multi-voltage power supply (100-240V) - Source: [nY38YvAMEFg]
- Made in USA - Source: [nY38YvAMEFg]

#### Connectors

##### Video Output
- 13W3 video connector - Source: [nY38YvAMEFg]
- Different pinout from SGI 13W3 - Source: [nY38YvAMEFg]
- Adapters available for VGA conversion - Source: [nY38YvAMEFg]

##### Peripherals
- Proprietary keyboard connector (mini-DIN style) - Source: [nY38YvAMEFg]
- Keyboard and mouse connectors appear same but different protocol than PS/2 - Source: [nY38YvAMEFg]
- Sun keyboards required (no PS/2 compatibility like SGI) - Source: [nY38YvAMEFg]
- AUI ethernet connector (needs transceiver adapter for 10BASE-T) - Source: [nY38YvAMEFg]
- External SCSI connector for hard drives - Source: [nY38YvAMEFg]
- Two serial ports - Source: [nY38YvAMEFg]

##### Internal
- Internal SCSI connector for hard drive (removed on example unit) - Source: [nY38YvAMEFg]
- Sony floppy drive (same connector style as Macintosh) - Source: [nY38YvAMEFg]
- RAM expansion slots - Source: [nY38YvAMEFg]
- Option card slot (example had 9-pin connector card) - Source: [nY38YvAMEFg]

#### Known Issues

##### Power Supply Capacitor Leakage
- **CRITICAL FAILURE MODE** - PSU capacitors leak severely - Source: [nY38YvAMEFg]
- Sony-manufactured internal power supply - Source: [nY38YvAMEFg]
- Electrolytic caps from 1990s are prone to failure - Source: [nY38YvAMEFg]
- Leakage causes corrosion on PCB traces and components - Source: [nY38YvAMEFg]
- If left unchecked, can destroy PSU board entirely - Source: [nY38YvAMEFg]
- Hot glue on caps makes removal difficult - Source: [nY38YvAMEFg]

##### Symptoms of PSU Failure
- No fan spin on power-up - Source: [nY38YvAMEFg]
- No voltage output despite power LED click - Source: [nY38YvAMEFg]
- Visible rust/corrosion around capacitors - Source: [nY38YvAMEFg]

##### Repair
- Must use skinny tall cylindrical caps (caps are close together) - Source: [nY38YvAMEFg]
- Scrub board to remove corrosion - Source: [nY38YvAMEFg]
- May need Dremel to remove corroded solder mask - Source: [nY38YvAMEFg]
- Replace all electrolytic caps preventatively - Source: [nY38YvAMEFg]
- Reference: users.glitchwrks.com/~glitch/2017/07/24/ipc-recap - Source: [nY38YvAMEFg]

#### Case Design
- Top cover releases with buttons on both sides - Source: [nY38YvAMEFg]
- Cover lifts off to reveal motherboard - Source: [nY38YvAMEFg]
- Hard drive mounting plate can come loose inside case - Source: [nY38YvAMEFg]
- External CD-ROM option available (sits on top, same footprint) - Source: [nY38YvAMEFg]

#### Usage Without Keyboard
- Possible to boot to serial console - Source: [nY38YvAMEFg]
- Solaris GUI requires keyboard and mouse though - Source: [nY38YvAMEFg]
- Sun keyboards/mice difficult to source - Source: [nY38YvAMEFg]

## General Notes

### 13W3 Connector Differences
- Sun 13W3 pinout differs from SGI 13W3 - Source: [nY38YvAMEFg]
- Cannot interchange cables between Sun and SGI machines - Source: [nY38YvAMEFg]
- Reference: ps-2.kev009.com/rs6000/13w3/13w3_pinout.html - Source: [nY38YvAMEFg]

### 1990s Capacitor Quality
- Capacitors from 1990s are notorious for failure - Source: [nY38YvAMEFg]
- 1980s caps (name brand) generally more reliable - Source: [nY38YvAMEFg]
- Many 1990s devices require preventative recapping - Source: [nY38YvAMEFg]
