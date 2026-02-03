# Seagate

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| ST-225 | MFM Hard Drive (20MB) | [CpQ2j2J6wL0] |
| ST-251 | MFM Hard Drive | [CpQ2j2J6wL0] |
| ST-271 | SCSI Hard Drive | [-9Ae-Lbz8AA] |
| ST-277 | SCSI Hard Drive | [-9Ae-Lbz8AA] |
| ST-225R | RLL Hard Drive | [36NPrsEcNww] |

## Platform-Specific Knowledge

### ST-225 (20MB MFM)

#### Specifications
- 20 megabyte capacity, Type 2 drive - Source: [CpQ2j2J6wL0]
- 615/650 cylinders, 4 heads, 17 sectors per track - Source: [CpQ2j2J6wL0]
- Stepper motor actuator (not voice coil) - Source: [CpQ2j2J6wL0]
- Stepper motor turned 90 degrees, uses rack and pinion system - Source: [CpQ2j2J6wL0]
- Requires manual head parking (no auto-park like ST-251) - Source: [CpQ2j2J6wL0]

#### BIOS Configuration
- Type 2 in BIOS: 615 cylinders, 4 heads, 17 sectors - Source: [CpQ2j2J6wL0]
- Pre-compensation value: 128 (not 300) - Source: [CpQ2j2J6wL0]
- Type 2 is safe default for most half-height MFM drives - Source: [CpQ2j2J6wL0]

#### Common Faults
- Head assembly corrosion: Glue used on head ribbon cable becomes corrosive over decades - Source: [CpQ2j2J6wL0]
- Corrosion visible as brown crustiness on head wires - Source: [CpQ2j2J6wL0]
- Corroded head wires break, causing total drive failure - Source: [CpQ2j2J6wL0]
- Drive spins but doesn't assert ready signal - Source: [CpQ2j2J6wL0]
- Clicking/seeking noises but no response to controller - Source: [CpQ2j2J6wL0]

#### Controller Board
- Controller is "dumb" - contains read/write amplifiers and motor control only - Source: [CpQ2j2J6wL0]
- Controllers are interchangeable between same model drives - Source: [CpQ2j2J6wL0]
- Controller swap is valid diagnostic: if problem follows controller, controller is bad - Source: [CpQ2j2J6wL0]
- If problem stays with drive after swap, mechanical/head issue - Source: [CpQ2j2J6wL0]
- Three screws hold controller PCB to drive - Source: [CpQ2j2J6wL0]
- Must disconnect: thin ribbon cable (head data), spindle motor cable, stepper motor cable - Source: [CpQ2j2J6wL0]
- Solder mask removed at screw points for grounding - Source: [CpQ2j2J6wL0]

#### Diagnostic Approaches
- Watch stepper motor behavior during power-on - Source: [CpQ2j2J6wL0]
- Normal behavior: Hits bump stop, then rotates several times quickly with high-pitched sound - Source: [CpQ2j2J6wL0]
- Failed behavior: Hits bump stop, moves slightly, gives flash error code - Source: [CpQ2j2J6wL0]
- Check for track zero sensor - ST-225 has very simplistic design with no track zero sensor - Source: [CpQ2j2J6wL0]
- Open drive to inspect head assembly for corrosion - Source: [CpQ2j2J6wL0]

#### Repair Techniques
- Controller board swap between same model drives - Source: [CpQ2j2J6wL0]
- Keep working controller as spare for future repairs - Source: [CpQ2j2J6wL0]
- Head assembly corrosion is usually not repairable - Source: [CpQ2j2J6wL0]

#### Transfer Speeds
- ~300 KB/sec transfer rate (limited by MFM interface) - Source: [CpQ2j2J6wL0]
- Seek time: 78ms max, 17.5ms track-to-track (slower than voice coil drives) - Source: [CpQ2j2J6wL0]

### ST-251

#### Specifications
- Auto-parking heads (unlike ST-225) - Source: [CpQ2j2J6wL0]
- No manual park required before power off - Source: [CpQ2j2J6wL0]

### General MFM Drive Notes

#### Stepper Motor Drives
- Stepper motors control head positioning - Source: [CpQ2j2J6wL0]
- Slower seeking than voice coil drives due to heavy assembly mass - Source: [CpQ2j2J6wL0]
- Stepper motor visible outside sealed area on some drives - Source: [CpQ2j2J6wL0]

#### Head Parking
- Always park heads before power off on non-auto-parking drives - Source: [CpQ2j2J6wL0]
- Un-parked heads audibly bump into stop when power cut - Source: [CpQ2j2J6wL0]
- Parked drive is silent when powered off - Source: [CpQ2j2J6wL0]
