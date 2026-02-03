# Storage Devices and Media Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [Hard Drives](#hard-drives)
- [SCSI Drive Imaging](#scsi-drive-imaging)
- [8-Inch Floppy Disks](#8-inch-floppy-disks)
- [Floppy Disk Inspection and Handling](#floppy-disk-inspection-and-handling)
- [Floppy Drive Termination](#floppy-drive-termination)
- [PCMCIA SCSI Adapters](#pcmcia-scsi-adapters)

## Hard Drives

### SCSI Diagnostics
- Silver Lining: Mac utility for SCSI drive formatting, testing, partitioning - Source: [-9Ae-Lbz8AA]
- SCSI Probe: Control panel to identify SCSI devices by model number - Source: [-9Ae-Lbz8AA]
- Short test and seek test can identify failing drives - Source: [-9Ae-Lbz8AA]
- Clicking/scraping sounds indicate physical damage - Source: [-9Ae-Lbz8AA]

### SCSI Termination
- End device on SCSI chain needs termination resistors - Source: [-9Ae-Lbz8AA]
- Termination prevents signal reflections on cable - Source: [-9Ae-Lbz8AA]
- Short cable runs may work without termination but not recommended - Source: [-9Ae-Lbz8AA]
- Some drives have internal termination (check DIP switches) - Source: [-9Ae-Lbz8AA]
- DB25 terminator types less common than Centronics 50-pin - Source: [-9Ae-Lbz8AA]

### Vintage Hard Drive Failure Modes
- Seagate ST-251/ST-271/ST-277 series: 5.25" drives, most are dead now - Source: [-9Ae-Lbz8AA]
- "N" suffix indicates SCSI version (has intelligent controller) - Source: [-9Ae-Lbz8AA]
- Stepper motor drives are slow at seeking due to heavy assembly mass - Source: [-9Ae-Lbz8AA]
- Voice coil drives (later) much faster seeking - Source: [-9Ae-Lbz8AA]
- Read/write heads can get stuck on disc media after long storage - Source: [-9Ae-Lbz8AA]
- Powering up stuck drive can rip head off entirely - Source: [-9Ae-Lbz8AA]
- Missing/detached read/write head = drive is toast - Source: [-9Ae-Lbz8AA]
- Scratched media visible where head was stuck/dragging - Source: [-9Ae-Lbz8AA]

### Bad Sector Workaround
- Partition drive into multiple partitions - Source: [-9Ae-Lbz8AA]
- Place bad sectors in middle "don't use" partition - Source: [-9Ae-Lbz8AA]
- Can still use partitions before and after bad area - Source: [-9Ae-Lbz8AA]
- Old trick to extend life of dying drives - Source: [-9Ae-Lbz8AA]

### MFM Hard Drive Testing and Repair

#### ST-506/MFM Interface Overview
- MFM (Modified Frequency Modulation) drives use ST-506 interface - Source: [bgW5tpyJljM]
- Two cables: 34-pin for control/seeking, smaller connector for read/write data - Source: [bgW5tpyJljM]
- Drive acts like "dumb" device - controller handles intelligence - Source: [bgW5tpyJljM]
- Interface supports up to 4 drives - Source: [bgW5tpyJljM]

#### Cable Configuration
- 34-pin cable may have twist (like floppy cables) - Source: [bgW5tpyJljM]
- If drive doesn't respond, try swapping to non-twisted cable - Source: [bgW5tpyJljM]
- Easy to install cables backwards - verify orientation - Source: [bgW5tpyJljM]

#### Termination
- Drive termination controlled by DIP switches (e.g., switch 7 on Fujitsu) - Source: [bgW5tpyJljM]
- Termination OFF = termination ENABLED (counterintuitive) - Source: [bgW5tpyJljM]
- Termination affects WRITE signals from controller to drive - Source: [bgW5tpyJljM]
- READ signals terminated on controller, not drive - Source: [bgW5tpyJljM]
- Incorrect termination = can read but cannot write - Source: [bgW5tpyJljM]

#### BIOS Configuration
- Must set correct heads, cylinders, and sectors in BIOS - Source: [bgW5tpyJljM]
- Look up drive part number online for specifications - Source: [bgW5tpyJljM]
- Common sector values: 17 (typical), 32 (some drives) - Source: [bgW5tpyJljM]
- Setting smaller values than maximum will work but wastes capacity - Source: [bgW5tpyJljM]
- "Drive failure" at boot usually means wrong parameters or dead drive - Source: [bgW5tpyJljM]

#### ISA Bus Speed Compatibility
- MFM controllers designed for 8MHz ISA bus - Source: [bgW5tpyJljM]
- Controllers may fail to write at 20MHz ISA bus speed - Source: [bgW5tpyJljM]
- Set BIOS to "S Clock / 5" for proper 8MHz operation - Source: [bgW5tpyJljM]
- Reading may work at higher speeds, writing fails - Source: [bgW5tpyJljM]
- Symptom: "Controller fails to respond" during format - Source: [bgW5tpyJljM]

#### Low-Level Formatting
- Speed Store utility: Manual setup → Initialize → Standard Init - Source: [bgW5tpyJljM]
- Some BIOS have built-in low-level format utilities - Source: [bgW5tpyJljM]
- Interleave setting: 1:1 for fast controllers, 2:1 for slower ones - Source: [bgW5tpyJljM]
- Wrong interleave causes very slow transfer speeds (~30KB/s vs ~350KB/s) - Source: [bgW5tpyJljM]
- After low-level format, run media analysis to find bad sectors - Source: [bgW5tpyJljM]

#### SpinRite II for MFM Drives
- Can low-level format without erasing data - Source: [bgW5tpyJljM]
- Reads data, low-levels sector, writes data back - Source: [bgW5tpyJljM]
- Reads marginal sectors repeatedly until data recovered - Source: [bgW5tpyJljM]
- Can remap bad sectors - Source: [bgW5tpyJljM]
- Requires proper ISA bus speed to function - Source: [bgW5tpyJljM]

#### Track Zero Bad Error
- "Track zero bad disc unusable" - entire track 0 must be good for DOS - Source: [bgW5tpyJljM]
- Even single bad sector on track 0 (any head) makes drive unusable - Source: [bgW5tpyJljM]
- Rest of drive may be perfect but DOS cannot use it - Source: [bgW5tpyJljM]

#### Controller Compatibility
- 16-bit ISA MFM controllers generally interchangeable - Source: [bgW5tpyJljM]
- Western Digital WD1002-WAH, WD1003-WAH common examples - Source: [bgW5tpyJljM]
- Drive formatted with one controller readable by another - Source: [bgW5tpyJljM]
- Different controllers may need different interleave settings - Source: [bgW5tpyJljM]

#### 8-Bit vs 16-Bit Controller Compatibility
- Some older MFM drives ONLY work with 8-bit XT-class controllers - Source: [Rm7JubQdHIE]
- 8-bit controllers: WD1002-WA2, early Western Digital, early DTC - Source: [Rm7JubQdHIE]
- 16-bit controllers designed for 286/AT-class machines - Source: [Rm7JubQdHIE]
- Both interface types use identical ST-506 cable to drive - Source: [Rm7JubQdHIE]
- Differences are ISA bus width and controller firmware timing - Source: [Rm7JubQdHIE]
- Symptom of mismatch: drive spins but "drive not ready" error - Source: [Rm7JubQdHIE]
- Tandon TM-252 example of drive requiring 8-bit controller - Source: [Rm7JubQdHIE]
- Always try 8-bit controller if drive won't work with 16-bit - Source: [Rm7JubQdHIE]

#### Drive Types Tested
- Fujitsu M2227D (3.5" full height): 615 cylinders, 8 heads, 17 or 32 sectors - Source: [bgW5tpyJljM]
- Control Data 94205-51 (half height): 989 cylinders, 5 heads, 17 sectors - Source: [bgW5tpyJljM]
- Control Data 94155-86 (full height): 925 cylinders, 9 heads, 17 sectors - Source: [bgW5tpyJljM]
- Computer Memories CM 6640: Full height, stepper motor actuator outside sealed area - Source: [bgW5tpyJljM]

#### Stepper Motor vs Voice Coil
- Stepper motor drives: Head actuator often outside sealed chamber - Source: [bgW5tpyJljM]
- Voice coil drives: Quieter seeking, faster operation - Source: [bgW5tpyJljM]
- Stuck stepper motor: May be able to free by removing motor and manipulating - Source: [bgW5tpyJljM]
- Computer Memories CM 6640: Lock solenoid prevents stepper from moving - Source: [bgW5tpyJljM]

#### Old MFM Drive Reliability
- Design life was typically 5-7 years - Source: [bgW5tpyJljM]
- 40-year-old drives may still work if stored properly - Source: [bgW5tpyJljM]
- Drives not used for long time may lose data - low-level reformat refreshes - Source: [bgW5tpyJljM]
- Half-height Control Data drives particularly reliable - Source: [bgW5tpyJljM]

#### MFM Drive Revival Techniques

##### Stiction Recovery
- Spindle bearings seize during long storage (stiction) - Source: [CpQ2j2J6wL0]
- Gentle physical tap/manipulation may free stuck spindle - Source: [CpQ2j2J6wL0]
- Opening drive NOT required for stiction - percussive maintenance works - Source: [CpQ2j2J6wL0]
- Once spinning, drive should spin up easier on subsequent power cycles - Source: [CpQ2j2J6wL0]

##### Stepper Motor Lubrication
- Stepper motor bearings can become gummed up over time - Source: [CpQ2j2J6wL0]
- Symptom: Drive gives flash/blink error codes, head can't complete initialization - Source: [CpQ2j2J6wL0]
- Stepper should turn freely when power is off; stiffness indicates problem - Source: [CpQ2j2J6wL0]
- Apply bearing oil into stepper motor shaft - Source: [CpQ2j2J6wL0]
- Manually rotate stepper through sticky spots while powered off - Source: [CpQ2j2J6wL0]
- SAFETY: Only manipulate heads while disc is spinning or just stopped - Source: [CpQ2j2J6wL0]
- May require 50+ power cycles while manipulating stepper - Source: [CpQ2j2J6wL0]
- WARNING: Lubricated bearings are temporary fix only - Source: [CpQ2j2J6wL0]
- Drive will fail again, especially after storage - only use for data recovery - Source: [CpQ2j2J6wL0]
- Warm drive works more reliably - let run for 20-30 minutes - Source: [CpQ2j2J6wL0]

##### Stepper Motor Bearing Oil Technique
- For drives where stepper motor cannot complete seek sequence - Source: [dErXDjMJ2dA]
- Symptom: Drive spins up, tries to move head, then shuts off - Source: [dErXDjMJ2dA]
- Cause: Stepper motor bearing has dry spots/seized positions - Source: [dErXDjMJ2dA]
- Apply bearing oil to stepper motor shaft - Source: [dErXDjMJ2dA]
- Remove stepper wheel if possible to access shaft directly - Source: [dErXDjMJ2dA]
- Manually rotate stepper through sticky spots while oiling - Source: [dErXDjMJ2dA]
- Power cycle repeatedly while exercising stepper - Source: [dErXDjMJ2dA]
- Once working, run SpinRite or similar to exercise entire mechanism - Source: [dErXDjMJ2dA]
- NOT a permanent fix - only for data recovery - Source: [dErXDjMJ2dA]
- Copy data off immediately, do not trust drive long-term - Source: [dErXDjMJ2dA]
- Proper repair requires replacing stepper motor or bearings - Source: [dErXDjMJ2dA]

#### Hard Card Specific Issues

##### Plus Hardcard Failures
- Rubber bump stops inside drives turn to goo (same as cassette belts) - Source: [cXbDSudlSTQ]
- Goo gets on heads and prevents assembly from moving - Source: [cXbDSudlSTQ]
- Most Plus hard cards found today don't work - Source: [cXbDSudlSTQ]
- No schematics available, drives are custom (not swappable) - Source: [cXbDSudlSTQ]
- Controller failures can cause data degradation during use - Source: [cXbDSudlSTQ]

##### Hard Card ROM Address Conflicts
- Hard cards use ROM BIOS, typically at C800 - Source: [cXbDSudlSTQ]
- Conflicts with XT-IDE and other cards at same address - Source: [cXbDSudlSTQ]
- Configure other cards for D000 or different address - Source: [cXbDSudlSTQ]
- Some hard cards have DIP switches for ROM address selection - Source: [cXbDSudlSTQ]

##### MFM Controller Compatibility
- Low-level format written by one controller brand may not work with another - Source: [cXbDSudlSTQ]
- Opti controller format NOT compatible with Western Digital - Source: [cXbDSudlSTQ]
- Hard drive error (1701) when swapping controllers = need re-low-level - Source: [cXbDSudlSTQ]
- Must low-level format when moving MFM drive between controller brands - Source: [cXbDSudlSTQ]
- 16-bit MFM controllers within same brand are generally interchangeable - Source: [cXbDSudlSTQ]

##### Controller Board Swap Diagnostics
- MFM drive controllers are "dumb" - contain read/write amps and motor control only - Source: [CpQ2j2J6wL0]
- Controllers interchangeable between same model drives (e.g., ST-225 to ST-225) - Source: [CpQ2j2J6wL0]
- Swap controller to diagnose: if problem follows controller, controller is bad - Source: [CpQ2j2J6wL0]
- If problem stays with drive after swap, mechanical/head assembly issue - Source: [CpQ2j2J6wL0]
- Three screws typically hold controller PCB to drive chassis - Source: [CpQ2j2J6wL0]
- Disconnect: thin ribbon cable (head data), spindle motor, stepper motor cables - Source: [CpQ2j2J6wL0]
- Save working controllers as spares for future repairs - Source: [CpQ2j2J6wL0]

##### Head Assembly Corrosion
- Glue on head ribbon cable becomes corrosive over decades - Source: [CpQ2j2J6wL0]
- Visible as brown crustiness on delicate head wires - Source: [CpQ2j2J6wL0]
- Corroded wires break, causing total drive failure - Source: [CpQ2j2J6wL0]
- Symptoms: Drive spins, seeks/clicks, but won't assert ready signal - Source: [CpQ2j2J6wL0]
- Must open drive to diagnose - inspect head ribbon area under magnification - Source: [CpQ2j2J6wL0]
- Usually not repairable - drive is toast - Source: [CpQ2j2J6wL0]

##### Magnetic Signal Fade Recovery
- Magnetic signal on platters may fade during long storage - Source: [CpQ2j2J6wL0]
- Symptoms: Drive spins but can't read existing data - Source: [CpQ2j2J6wL0]
- Low-level format refreshes magnetic patterns - Source: [CpQ2j2J6wL0]
- Data will be lost, but drive becomes usable again - Source: [CpQ2j2J6wL0]

#### Interleave Optimization (SpinRite II)

##### Interleave Importance
- Wrong interleave causes severe performance penalty (1/10th speed or worse) - Source: [CpQ2j2J6wL0]
- Optimal interleave depends on computer speed, not just drive - Source: [CpQ2j2J6wL0]
- Fast machines (486) typically need 1:1 interleave - Source: [CpQ2j2J6wL0]
- Slower machines need 2:1 or higher - Source: [CpQ2j2J6wL0]

##### SpinRite II Features
- Can determine optimal interleave for your specific computer - Source: [CpQ2j2J6wL0]
- Can change interleave without erasing data - Source: [CpQ2j2J6wL0]
- Shows maximum data rate at each interleave setting - Source: [CpQ2j2J6wL0]
- Gibson Research product, considered best utility for MFM optimization - Source: [CpQ2j2J6wL0]

#### MFM Interface Fundamentals
- All MFM drives have similar transfer speeds (~300 KB/sec) regardless of manufacturer - Source: [CpQ2j2J6wL0]
- Interface runs at 5-6.25 megabits/second - this limits speed - Source: [CpQ2j2J6wL0]
- Speed differences between drives are in seek time only - Source: [CpQ2j2J6wL0]
- Voice coil drives much faster seeking than stepper motor drives - Source: [CpQ2j2J6wL0]
- Voice coil also much quieter during operation - Source: [CpQ2j2J6wL0]

#### MFM Drive Ready Signal
- "Drive ready" signal tells controller drive is operational - Source: [CpQ2j2J6wL0]
- If not asserted: computer waits indefinitely or reports "drive failure" - Source: [CpQ2j2J6wL0]
- Mr BIOS specifically reports "waiting for fixed disk to spin up" - Source: [CpQ2j2J6wL0]
- Other BIOS may just hang with no message - Source: [CpQ2j2J6wL0]

#### Miniscribe Blink Error Codes
- Error codes displayed as Morse code via activity LED - Source: [CpQ2j2J6wL0]
- Zero = half second of flashing, One = continuous on - Source: [CpQ2j2J6wL0]
- Half second between bits, full second between code repeats - Source: [CpQ2j2J6wL0]
- Code D (1101) = Seek error during burn-in or recal - Source: [CpQ2j2J6wL0]
- Look up codes in Miniscribe technical manual - Source: [CpQ2j2J6wL0]

#### Software Found on Old Drives
- Thompson Toolkit: Unix-like shell for DOS - Source: [bgW5tpyJljM]
- LapLink: Serial/parallel file transfer between PCs - Source: [bgW5tpyJljM]
- On-Track Disk Manager: Partition management utility - Source: [bgW5tpyJljM]
- X-Tree Gold: DOS file manager - Source: [bgW5tpyJljM]

#### MFM-to-SCSI Converters (OMTI 5200)
- Allows using cheap MFM hard drives on SCSI systems - Source: [FwrSnNjrmsM]
- Z8 microprocessor-based (essentially a complete Z80 computer) - Source: [FwrSnNjrmsM]
- Supports 2 hard drives + 2 floppy drives on single SCSI ID via LUNs - Source: [FwrSnNjrmsM]
- Heads/cylinders configurable via SCSI commands - Source: [FwrSnNjrmsM]
- Settings NOT saved - resets on power loss - Source: [FwrSnNjrmsM]
- Built-in SCSI terminator - Source: [FwrSnNjrmsM]
- Mac compatibility: Works with Silver Lining (slow handshake mode) - Source: [FwrSnNjrmsM]
- ~47KB/sec write, ~167KB/sec read through converter - Source: [FwrSnNjrmsM]
- Manual: bitsavers.org/pdf/sms/3001206_OMTI_5000_Series_Reference_Aug85.pdf - Source: [FwrSnNjrmsM]

### IDE Laptop Drives (44-pin)
- Used in Amiga 600/1200, early laptops - Source: [-9Ae-Lbz8AA]
- New old stock Seagate 100GB 44-pin IDE drives still available on eBay - Source: [-9Ae-Lbz8AA]
- Quiet, good bearings, reliable - around $15 - Source: [-9Ae-Lbz8AA]
- Good replacement for vintage machines needing 44-pin IDE - Source: [-9Ae-Lbz8AA]

## SCSI Drive Imaging

### BlueSCSI V2 Initiator Mode
- Turns BlueSCSI into SCSI host to dump drive contents - Source: [7EVAWWsaBUg]
- Automatically images attached SCSI devices to SD card - Source: [7EVAWWsaBUg]
- ~3 MB/s transfer speed possible - Source: [7EVAWWsaBUg]
- Works with removable media (Zip, SyQuest) - ejects disc when done - Source: [7EVAWWsaBUg]
- GitHub: github.com/BlueSCSI/BlueSCSI-v2 - Source: [7EVAWWsaBUg]

### Initiator Mode Setup
1. Edit bluescsi.ini: add `InitiatorMode = 1` - Source: [7EVAWWsaBUg]
2. Move jumper from TARGET to INITIATOR position - Source: [7EVAWWsaBUg]
3. Install jumper on INITIATOR header - Source: [7EVAWWsaBUg]
4. Remove BACKFEED jumper if using USB power - Source: [7EVAWWsaBUg]

### Critical: Same Power Supply Requirement
- BlueSCSI and target drive MUST be on same power supply - Source: [7EVAWWsaBUg]
- Separate supplies cause RP2040 to fail initialization - Source: [7EVAWWsaBUg]
- Use floppy splitter cable to power both from same source - Source: [7EVAWWsaBUg]

### Termination
- Both ends of SCSI bus must be terminated - Source: [7EVAWWsaBUg]
- Target drive needs termination resistors installed - Source: [7EVAWWsaBUg]
- Or use cable terminator on empty connector - Source: [7EVAWWsaBUg]

### Known Issues (as of Nov 2023 firmware)
- Some drives respond to ID7 AND their configured ID - creates duplicate images - Source: [7EVAWWsaBUg]
- Bad sectors can cause imaging to abort - Source: [7EVAWWsaBUg]
- Some drives cause firmware crash on initialization - Source: [7EVAWWsaBUg]
- Wi-Fi Pico version has non-functional activity LED - Source: [7EVAWWsaBUg]
- No serial port access for real-time progress monitoring - Source: [7EVAWWsaBUg]

### Image File Output
- Creates HDx0.img files (x = SCSI ID) - Source: [7EVAWWsaBUg]
- Increments filename if file exists (HD00, HD01, etc.) - Source: [7EVAWWsaBUg]
- For >4GB drives, format SD card as exFAT - Source: [7EVAWWsaBUg]
- Log file shows progress and errors - Source: [7EVAWWsaBUg]

### Alternative: ThinkPad with PCMCIA SCSI
- Use old laptop with PCMCIA SCSI adapter (e.g., Adaptec) - Source: [7EVAWWsaBUg]
- Windows XP or Linux can read/image drives directly - Source: [7EVAWWsaBUg]
- Good for validating drives work before BlueSCSI imaging - Source: [7EVAWWsaBUg]

## 8-Inch Floppy Disks

### Media Handling
- Very robust and reliable media format - Source: [0ZKsQsZhDvw]
- Double-sided disks have index hole in different position than single-sided - Source: [0ZKsQsZhDvw]
- Double-sided media rarer and more valuable - Source: [0ZKsQsZhDvw]
- Disks are very flexible and tend to return to shape even if bent - Source: [0ZKsQsZhDvw]
- IBM System/36 used carousel caddies for automatic disk loading - Source: [0ZKsQsZhDvw]

### Formatting
- FormatQM: Bulk formatting utility for testing multiple disks quickly - Source: [0ZKsQsZhDvw]
- Good disks make different tone than bad disks - Source: [0ZKsQsZhDvw]
- Available at vetusware.com - Source: [0ZKsQsZhDvw]

### High-Density 8-Inch Disks
- FD26 HD high-density 8" disks exist but are unusual - Source: [eFatlDatjZM]
- Index hole is in DIFFERENT position than standard single or double-sided disks - Source: [eFatlDatjZM]
- Single-sided, double-sided, and HD all have different index hole positions - Source: [eFatlDatjZM]
- 96 TPI (tracks per inch) vs standard density - Source: [eFatlDatjZM]
- Double track specification - Source: [eFatlDatjZM]
- Cannot be used in standard 8" drives due to index hole position - Source: [eFatlDatjZM]
- Media formulation likely similar to 5.25" high-density (different coercivity) - Source: [eFatlDatjZM]
- No known drives in collectors' hands currently - Source: [eFatlDatjZM]
- Important for media preservation - data on these disks may be unreadable - Source: [eFatlDatjZM]

## Floppy Disk Inspection and Handling

### Visual Inspection Before Use
- Always inspect disks visually before inserting into drive - Source: [eIVtVmNP_VI]
- Open jacket shutter and rotate disk by hand - Source: [eIVtVmNP_VI]
- Surface should be shiny, smooth, consistent all around - Source: [eIVtVmNP_VI]
- Reject any disks with visible mold, cloudiness, or irregularities - Source: [eIVtVmNP_VI]

### Mold and Contamination
- Moldy disks can transfer contamination to read/write heads - Source: [eIVtVmNP_VI]
- Contaminated heads prevent reading ANY disk until cleaned - Source: [eIVtVmNP_VI]
- Manual head cleaning may be required (cleaning disk not enough) - Source: [eIVtVmNP_VI]
- Single-sided disks often more susceptible than double-sided - Source: [eIVtVmNP_VI]
- Disks stored together often all affected if mold present - Source: [eIVtVmNP_VI]
- Brand quality varies: Memorex, Elephant, Bit Bank often more resistant - Source: [eIVtVmNP_VI]

### Stuck Disks
- Some old disks get stuck inside jacket (won't rotate) - Source: [eIVtVmNP_VI]
- Caused by spilled liquids or degraded jacket liner - Source: [eIVtVmNP_VI]
- Disk is dead if stuck - cannot be used - Source: [eIVtVmNP_VI]

### FormatQM Utility
- Version 2.02 for bulk formatting and testing - Source: [eIVtVmNP_VI]
- Uses direct hardware access for quick disk swaps - Source: [eIVtVmNP_VI]
- Auto-detects when new disk inserted - Source: [eIVtVmNP_VI]
- Different tones for good vs bad disks - Source: [eIVtVmNP_VI]
- Set "allow flawed diskette" to NO to reject any bad sectors - Source: [eIVtVmNP_VI]
- Always format 360K disks on 360K drives (double density on DD) - Source: [eIVtVmNP_VI]
- Download: vetusabandonware.com/download/FormatQM%20v2.02%202.02/?id=17085 - Source: [eIVtVmNP_VI]

### Storage Recommendations
- Temperature: 50-125°F (10-52°C) per Memorex specs - Source: [eIVtVmNP_VI]
- Low humidity preferred - Source: [eIVtVmNP_VI]
- Room temperature (20-21°C) optimal for longevity - Source: [eIVtVmNP_VI]

## 5.25" Floppy Drive Testing and Configuration

### Drive Select Jumpers and Terminology

#### Drive Select Strapping
- DS0/DS1/DS2/DS3 or I/IS/II strapping systems used - Source: [xtHwYQyhkAc]
- "I" corresponds to drive select 0, "IS" to select 1, "II" to select 2 - Source: [xtHwYQyhkAc]
- PC cable twist allows all drives to be jumpered as DS1/IS - Source: [xtHwYQyhkAc]
- Some drives use different jumper labeling systems - check documentation - Source: [xtHwYQyhkAc]

#### Speed Selection (Dual Speed Drives)
- High-density 5.25" drives can spin at 360 RPM (HD) or 300 RPM (DD) - Source: [xtHwYQyhkAc]
- 300 RPM mode for reading/writing 360K double-density disks - Source: [xtHwYQyhkAc]
- 360 RPM mode for 1.2MB high-density disks - Source: [xtHwYQyhkAc]
- Speed typically controlled via DENSITY SELECT signal from controller - Source: [xtHwYQyhkAc]
- Some drives have manual speed selection jumper override - Source: [xtHwYQyhkAc]

#### Track Density
- 96 TPI (tracks per inch): High-density drives - Source: [xtHwYQyhkAc]
- 48 TPI: Double-density drives (360K) - Source: [xtHwYQyhkAc]
- HD drives can write 360K disks but may cause compatibility issues - Source: [xtHwYQyhkAc]
- Narrow HD track written on 48 TPI disk may not read in native DD drive - Source: [xtHwYQyhkAc]

### ImageDisk (IMD) Testing Software
- Utility for thorough floppy drive and media testing - Source: [xtHwYQyhkAc]
- Tests both read AND write capability - Source: [xtHwYQyhkAc]
- Reports actual disk format detected vs expected - Source: [xtHwYQyhkAc]
- Good for verifying drives work properly before use - Source: [xtHwYQyhkAc]
- Download from Dunfield's site (classiccmp.org/dunfield) - Source: [xtHwYQyhkAc]

### 5.25" High-Density Drive Models

#### TEAC FD-55GFR
- Common high-density 1.2MB PC drive - Source: [xtHwYQyhkAc]
- Very reliable when working - Source: [xtHwYQyhkAc]
- Dual speed: 360 RPM (HD) and 300 RPM (DD) - Source: [xtHwYQyhkAc]
- Many found working even after decades - Source: [xtHwYQyhkAc]

#### Chinon Drives
- Generally reliable Japanese-made drives - Source: [xtHwYQyhkAc]
- Some models have unusual jumper configurations - Source: [xtHwYQyhkAc]

#### Newtronics Drives
- Budget/generic drives common in clones - Source: [xtHwYQyhkAc]
- Variable quality - some work fine, others problematic - Source: [xtHwYQyhkAc]

#### Panasonic/Matsushita Drives
- JU-475 series common in IBM machines - Source: [xtHwYQyhkAc]
- Generally very reliable - Source: [xtHwYQyhkAc]

#### Epson Drives
- Good quality Japanese drives - Source: [xtHwYQyhkAc]
- Some models used in Apple II systems - Source: [xtHwYQyhkAc]

#### Mitsubishi Drives
- MF504B and similar models - Source: [xtHwYQyhkAc]
- Quality varies by vintage - Source: [xtHwYQyhkAc]

### 3.5" High-Density Drives

#### TEAC FD-235HF
- Standard 1.44MB PC floppy drive - Source: [xtHwYQyhkAc]
- Very common and reliable - Source: [xtHwYQyhkAc]
- Good replacement source for any PC needing 3.5" drive - Source: [xtHwYQyhkAc]

### Testing Procedure
1. Verify drive physically spins disk when activated - Source: [xtHwYQyhkAc]
2. Check head movement (should seek smoothly) - Source: [xtHwYQyhkAc]
3. Test reading known-good disk of appropriate format - Source: [xtHwYQyhkAc]
4. Test writing and verify by reading back - Source: [xtHwYQyhkAc]
5. For HD drives, test both 1.2MB and 360K modes - Source: [xtHwYQyhkAc]
6. Use ImageDisk or similar diagnostic for thorough testing - Source: [xtHwYQyhkAc]

### Common Floppy Drive Failures
- Dirty heads: Clean with IPA and lint-free swab - Source: [xtHwYQyhkAc]
- Worn drive belt: 3.5" drives especially (spindle belt) - Source: [xtHwYQyhkAc]
- Stepper motor sticking: May respond to lubrication - Source: [xtHwYQyhkAc]
- Failed head amplifier IC: Usually not repairable - Source: [xtHwYQyhkAc]
- Broken eject mechanism: 3.5" drives, sometimes fixable - Source: [xtHwYQyhkAc]

## Floppy Drive Termination

### Termination Theory

#### Why Termination is Needed
- Floppy drives use open collector (or open drain) output drivers - Source: [RMM16oeTB8A]
- Open collector can only pull signal LOW, cannot drive HIGH - Source: [RMM16oeTB8A]
- Pull-up resistors needed to bring signal HIGH when not actively driven - Source: [RMM16oeTB8A]
- Without termination, signals "float" at undefined levels - Source: [RMM16oeTB8A]
- Termination provides both defined idle state AND proper signal impedance - Source: [RMM16oeTB8A]

#### Standard Termination Values
- SA-800 (8-inch): 150 ohm pull-up to 5V per signal line - Source: [RMM16oeTB8A]
- SA-400 (5.25-inch): Same 150 ohm specification inherited from SA-800 - Source: [RMM16oeTB8A]
- 3.5-inch PC drives: Often use 300 ohm (different from original spec) - Source: [RMM16oeTB8A]
- PC floppy interface: 300 ohm at controller AND 300 ohm at drive = ~150 ohm equivalent - Source: [RMM16oeTB8A]

### Signal Direction Matters

#### Controller-to-Drive Signals (Write Signals)
- Drive select, motor on, step, direction, write gate, write data - Source: [RMM16oeTB8A]
- Open collector drivers on CONTROLLER - Source: [RMM16oeTB8A]
- Must be terminated at the END of cable (last drive) - Source: [RMM16oeTB8A]
- Signal travels from controller to drive - Source: [RMM16oeTB8A]

#### Drive-to-Controller Signals (Read Signals)
- Index, track 0, write protect, read data, ready, two-sided - Source: [RMM16oeTB8A]
- Open collector drivers on DRIVE - Source: [RMM16oeTB8A]
- Must be terminated at CONTROLLER end - Source: [RMM16oeTB8A]
- Signal travels from drive back to controller - Source: [RMM16oeTB8A]

### Platform-Specific Termination

#### IBM PC/XT/AT Floppy Interface
- Controller has built-in termination for read signals - Source: [RMM16oeTB8A]
- Modern 3.5" drives often have built-in termination for write signals - Source: [RMM16oeTB8A]
- 300 ohm at each end = 150 ohm equivalent parallel resistance - Source: [RMM16oeTB8A]
- This is why PC drives "just work" without terminator packs - Source: [RMM16oeTB8A]

#### TRS-80 Model 2 Floppy Interface
- External floppy expansion box has termination challenges - Source: [RMM16oeTB8A]
- Controller inside computer, drives in external enclosure - Source: [RMM16oeTB8A]
- Write signals: Terminated at last drive in chain (normal) - Source: [RMM16oeTB8A]
- Read signals: Termination in external box, not at controller - Source: [RMM16oeTB8A]
- Long cable run from external box back to computer creates issues - Source: [RMM16oeTB8A]
- Signal may be weak or noisy due to unterminated controller end - Source: [RMM16oeTB8A]

#### Generic SA-400/SA-800 Drives
- Terminator pack (resistor network) plugs into socket on drive PCB - Source: [RMM16oeTB8A]
- Only install terminator on LAST drive in chain - Source: [RMM16oeTB8A]
- Middle drives should have terminator removed - Source: [RMM16oeTB8A]
- Terminator packs are DIP or SIP resistor networks - Source: [RMM16oeTB8A]

### Troubleshooting Termination Issues

#### Symptoms of Missing Termination
- Drive select doesn't work reliably - Source: [RMM16oeTB8A]
- Read errors or data corruption - Source: [RMM16oeTB8A]
- Intermittent operation - Source: [RMM16oeTB8A]
- Works with short cables but fails with long cables - Source: [RMM16oeTB8A]

#### Symptoms of Over-Termination
- Excessive current draw - Source: [RMM16oeTB8A]
- Signal levels too low (terminated at multiple points) - Source: [RMM16oeTB8A]
- Both ends plus middle drives all terminated = bad - Source: [RMM16oeTB8A]

### 34-Pin Floppy Interface Pinout
- Even pins are ground - Source: [RMM16oeTB8A]
- Odd pins carry signals - Source: [RMM16oeTB8A]
- Pin 1: High density (not on original SA-400) - Source: [RMM16oeTB8A]
- PC cable twist at pins 10-16 swaps drive select lines - Source: [RMM16oeTB8A]
- This allows both drives to be jumpered as DS1 - Source: [RMM16oeTB8A]

## PCMCIA SCSI Adapters

### Adaptec Slim SCSI
- PCMCIA/PC Card SCSI adapter for laptops - Source: [i08yBdvJ4kA]
- "Fast SCSI" version tops out around 2 MB/s - Source: [i08yBdvJ4kA]
- Requires proprietary high-density cable (20+ conductors) - Source: [i08yBdvJ4kA]
- Cable converts to standard 50-pin SCSI connector - Source: [i08yBdvJ4kA]

### Use Cases
- Accessing old Mac drives with HFS filesystem - Source: [i08yBdvJ4kA]
- Working with SGI machines - Source: [i08yBdvJ4kA]
- Testing SCSI drives without desktop hardware - Source: [i08yBdvJ4kA]
- Plug and play in Linux (Debian mounts HFS partitions automatically) - Source: [i08yBdvJ4kA]

### Compatible Laptops
- Any laptop with PCMCIA/PC Card slot - Source: [i08yBdvJ4kA]
- ThinkPad X series, T series, Toughbooks work well - Source: [i08yBdvJ4kA]
- Linux provides good driver support for Adaptec adapters - Source: [i08yBdvJ4kA]

## Floptical Drives

### Overview
- Floptical = floppy + optical, hybrid technology from late 1980s - Source: [uXUCgOprlu0]
- Uses optical servo for precise head alignment - Source: [uXUCgOprlu0]
- Can store ~21MB formatted on special floptical media - Source: [uXUCgOprlu0]
- iOmega/Insight manufactured floptical drives - Source: [uXUCgOprlu0]
- Precursor to LS-120 SuperDisk technology - Source: [uXUCgOprlu0]

### Interface
- SCSI interface, NOT standard floppy interface - Source: [uXUCgOprlu0]
- Dedicated ISA controller card often included - Source: [uXUCgOprlu0]
- Controller card has ROM BIOS for boot support - Source: [uXUCgOprlu0]
- Shows up as SCSI floppy device, not hard drive - Source: [uXUCgOprlu0]
- Requires special drivers for DOS/Mac/Amiga - Source: [uXUCgOprlu0]

### Standard Floppy Compatibility
- Can read/write standard 720K and 1.44MB floppy disks - Source: [uXUCgOprlu0]
- Has second set of heads for standard floppy operation - Source: [uXUCgOprlu0]
- Makes it useful even without floptical media - Source: [uXUCgOprlu0]

### Media
- Floptical disks look similar to standard 3.5" floppies - Source: [uXUCgOprlu0]
- Have optical grooves for servo alignment (invisible to eye) - Source: [uXUCgOprlu0]
- Very rare and hard to find today - Source: [uXUCgOprlu0]
- SGI workstations used floptical drives - Source: [uXUCgOprlu0]
- Was considered for Amiga 3000 but never bundled - Source: [uXUCgOprlu0]

### Modern Support
- Windows NT, 2000 have native format support - Source: [uXUCgOprlu0]
- Windows XP and later dropped floptical support - Source: [uXUCgOprlu0]
- Mac OS can boot from floptical - Source: [uXUCgOprlu0]

### SCSI Drive Termination
- Drives need termination resistors at end of chain - Source: [i08yBdvJ4kA]
- Some drives have TE (Terminator Enable) jumper for built-in termination - Source: [i08yBdvJ4kA]
- Ribbon cable with terminating resistors can be used instead - Source: [i08yBdvJ4kA]
