# OMTI (Scientific Micro Systems)

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| OMTI 5200 | MFM-to-SCSI Converter | [FwrSnNjrmsM] |

## Platform-Specific Knowledge

### OMTI 5200 MFM-to-SCSI Converter

#### Overview
- Converts MFM hard drives (ST-506/ST-412) to SCSI interface - Source: [FwrSnNjrmsM]
- Also supports 34-pin floppy drives - Source: [FwrSnNjrmsM]
- Made in Hong Kong - Source: [FwrSnNjrmsM]
- Manual dated August 1985 - Source: [FwrSnNjrmsM]
- Very expensive when new (essentially a complete Z80 computer) - Source: [FwrSnNjrmsM]
- Manual available at bitsavers.org/pdf/sms/3001206_OMTI_5000_Series_Reference_Aug85.pdf - Source: [FwrSnNjrmsM]

#### Hardware
- Zilog Z8 microprocessor (Z80 variant, romless version) - Source: [FwrSnNjrmsM]
- Standard PC floppy controller chip (same as PC Junior) - Source: [FwrSnNjrmsM]
- SCSI controller chip - Source: [FwrSnNjrmsM]
- EEPROM for firmware - Source: [FwrSnNjrmsM]
- 8K RAM and 2K RAM - Source: [FwrSnNjrmsM]
- Sequencer and buffer chips - Source: [FwrSnNjrmsM]
- Encoder/decoder chip - Source: [FwrSnNjrmsM]
- Built-in SCSI terminator (220/330 ohm pack) - Source: [FwrSnNjrmsM]
- No silk-screened pin 1 marker - look for square pad vs round pads - Source: [FwrSnNjrmsM]

#### Connectors
- J1: 50-pin SCSI host connector - Source: [FwrSnNjrmsM]
- J2: 34-pin floppy drive ribbon connector (supports 2 drives) - Source: [FwrSnNjrmsM]
- J3: First Winchester (MFM) drive - Source: [FwrSnNjrmsM]
- J4: Second Winchester (MFM) drive - Source: [FwrSnNjrmsM]
- J7: Floppy drive connector - Source: [FwrSnNjrmsM]
- Standard Molex power connector - Source: [FwrSnNjrmsM]
- Designed to mount on bottom of hard drive with standoffs - Source: [FwrSnNjrmsM]

#### Capabilities
- Supports two hard drives and two floppy drives simultaneously - Source: [FwrSnNjrmsM]
- Each drive assigned different SCSI LUN based on jumpers - Source: [FwrSnNjrmsM]
- Jumpers 0-7 select SCSI ID - Source: [FwrSnNjrmsM]
- Heads and cylinders configurable via SCSI commands (not fixed) - Source: [FwrSnNjrmsM]
- Supports 5.25" and 8" floppy drives - Source: [FwrSnNjrmsM]
- 8" drives need adapter cable - Source: [FwrSnNjrmsM]
- OMTI 5300 variant supports tape drives - Source: [FwrSnNjrmsM]

#### Configuration
- SCSI ID 0 has four LUNs: 2 hard drives + 2 floppy drives - Source: [FwrSnNjrmsM]
- LUN assignment configurable via jumpers - Source: [FwrSnNjrmsM]
- Floppy drives don't need cable twist - use jumpers on drive - Source: [FwrSnNjrmsM]
- Settings NOT saved in EEPROM - resets to defaults on power loss - Source: [FwrSnNjrmsM]
- Default configuration shows as ~5MB hard drive - Source: [FwrSnNjrmsM]

#### Macintosh Compatibility Testing

##### What Works
- Mac Classic II detects OMTI 5200 as SCSI device - Source: [FwrSnNjrmsM]
- Shows as "SCSI Disc" in SCSI Probe (displays just a dot for model name) - Source: [FwrSnNjrmsM]
- Silver Lining can format MFM drives through this controller - Source: [FwrSnNjrmsM]
- Successfully formatted Seagate ST-225 as 20MB drive - Source: [FwrSnNjrmsM]
- Can copy files, install System 7, and run games - Source: [FwrSnNjrmsM]
- Read speed: ~167KB/sec - Source: [FwrSnNjrmsM]
- Write speed: ~47KB/sec - Source: [FwrSnNjrmsM]
- Total throughput: ~34KB/sec read+write - Source: [FwrSnNjrmsM]

##### What Doesn't Work
- Won't boot Mac from drive (starts then fails) - Source: [FwrSnNjrmsM]
- Settings lost on power cycle causes boot failures - Source: [FwrSnNjrmsM]
- Disk errors after reboot (wrong cylinder count) - Source: [FwrSnNjrmsM]
- Floppy drive emulation unreliable on Mac - Source: [FwrSnNjrmsM]
- Mac software (Silver Lining) can't properly address 360K floppy - Source: [FwrSnNjrmsM]
- Minimum partition size (500K) exceeds 360K floppy capacity - Source: [FwrSnNjrmsM]
- Multiple timing loop settings don't work reliably - Source: [FwrSnNjrmsM]

##### Configuration Notes for Mac
- Default "Fast Hardware Handshake" timing doesn't work - Source: [FwrSnNjrmsM]
- Use "Silver Lining Slow Handshake" timing - Source: [FwrSnNjrmsM]
- Must specify heads, cylinders, sectors manually - Source: [FwrSnNjrmsM]
- Seagate ST-225: 17 sectors (not default values) - Source: [FwrSnNjrmsM]
- Controller may receive power from SCSI termination power - Source: [FwrSnNjrmsM]
- May cause Mac to not boot if powered only by termination power - Source: [FwrSnNjrmsM]

#### Intended Use Cases
- Professional Unix workstations - Source: [FwrSnNjrmsM]
- Systems needing multiple drives on single SCSI cable - Source: [FwrSnNjrmsM]
- Converting cheap MFM drives to SCSI interface - Source: [FwrSnNjrmsM]
- External drive enclosures with MFM drives inside - Source: [FwrSnNjrmsM]
- 8" floppy integration on SCSI systems - Source: [FwrSnNjrmsM]

#### Software/Driver Status (as of video)
- No known PC/DOS drivers located - Source: [FwrSnNjrmsM]
- VCF forum discussions exist but no driver links found - Source: [FwrSnNjrmsM]
- Requires host software that can send SCSI configuration commands - Source: [FwrSnNjrmsM]
- Mac compatibility is limited without proper drivers - Source: [FwrSnNjrmsM]

#### Historical Context
- Pre-dates Mac Plus (1986) - first Mac with built-in SCSI - Source: [FwrSnNjrmsM]
- Likely used in professional/industrial settings - Source: [FwrSnNjrmsM]
- Allowed use of cheaper MFM drives on SCSI systems - Source: [FwrSnNjrmsM]
