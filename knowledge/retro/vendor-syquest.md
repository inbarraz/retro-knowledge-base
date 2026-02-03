# SyQuest

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| SQ5110 (88MB) | Removable Storage | [bW5_9WfiVSw] |

## Platform-Specific Knowledge

### SyQuest 88MB Drives

#### Overview
- 88MB removable hard drive cartridge system - Source: [bW5_9WfiVSw]
- Cartridge contains actual hard drive platter - Source: [bW5_9WfiVSw]
- SCSI interface - Source: [bW5_9WfiVSw]

#### LED Status Indicators
- Solid green LED: Drive ready, cartridge accessible - Source: [bW5_9WfiVSw]
- Flashing green LED: Drive cannot read cartridge (error condition) - Source: [bW5_9WfiVSw]
- Orange LED stuck on: Possible driver issue, not drive fault - Source: [bW5_9WfiVSw]

#### Cartridge Recovery Technique
- Flashing green LED does NOT always mean cartridge is dead - Source: [bW5_9WfiVSw]
- Recovery: Use Silver Lining utility on Mac, run "Short Test" - Source: [bW5_9WfiVSw]
- Short test spins down cartridge, spins up, performs read/write tests - Source: [bW5_9WfiVSw]
- Even if test reports errors, cartridge may mount afterward - Source: [bW5_9WfiVSw]
- Recovered 4 out of 4 "bad" cartridges with this method - Source: [bW5_9WfiVSw]

#### Drive Compatibility Issues
- Bad drive can cause cartridges to show flashing LED even in good drives - Source: [bW5_9WfiVSw]
- Appears to mark something on disc that flags it as bad - Source: [bW5_9WfiVSw]
- Short test in working drive can "reset" this condition - Source: [bW5_9WfiVSw]
- PLI branded 88MB "C" variant may differ from standard 88MB - Source: [bW5_9WfiVSw]

#### Formatted Capacity
- 88MB cartridge formats to approximately 83MB usable - Source: [bW5_9WfiVSw]

#### Service Documentation
- 44MB drives better documented than 88MB versions - Source: [bW5_9WfiVSw]
- 88MB service information harder to find - Source: [bW5_9WfiVSw]

### Silver Lining Utility (Mac)

#### Testing Options
- Short Test: Quick verification, can recover "bad" cartridges - Source: [bW5_9WfiVSw]
- Full Test: Complete surface scan - Source: [bW5_9WfiVSw]
- Format: Low-level format option - Source: [bW5_9WfiVSw]

#### Common Error Messages
- "Unable to reliably access the disk" - may still be recoverable - Source: [bW5_9WfiVSw]
- Read errors during test don't mean cartridge is unrecoverable - Source: [bW5_9WfiVSw]

#### Compatibility Notes
- Silver Lining drivers may conflict with Mac Classic operation - Source: [bW5_9WfiVSw]
- Can cause system freezes with orange LED stuck on - Source: [bW5_9WfiVSw]
- May need SyQuest-specific formatting utility - Source: [bW5_9WfiVSw]

## Troubleshooting Guide

### Flashing Green LED on 88MB Cartridge
1. Try cartridge in different known-good drive - Source: [bW5_9WfiVSw]
2. If flashing persists, use Silver Lining utility - Source: [bW5_9WfiVSw]
3. Run Short Test even if drive reports access errors - Source: [bW5_9WfiVSw]
4. After test completes (even with errors), try mounting again - Source: [bW5_9WfiVSw]
5. Cartridge may now mount normally with solid green LED - Source: [bW5_9WfiVSw]

### Cross-Contamination Warning
- Using cartridge in bad drive may cause it to fail in good drives - Source: [bW5_9WfiVSw]
- Damage appears recoverable with Short Test method - Source: [bW5_9WfiVSw]
- Not permanent, but requires intervention - Source: [bW5_9WfiVSw]
