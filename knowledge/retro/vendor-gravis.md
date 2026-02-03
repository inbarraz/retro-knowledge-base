# Gravis (Advanced Gravis)

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Gravis Ultrasound Max 1.8 | ISA Sound Card | [FnLKPVzK7bo] |
| Gravis Ultrasound (Classic) | ISA Sound Card | [FnLKPVzK7bo] |

## Platform-Specific Knowledge

### Gravis Ultrasound Max (Revision 1.8)

#### Overview
- Classic GUS with optional 16-bit recording daughterboard and CD-ROM interface on single board - Source: [FnLKPVzK7bo]
- 512KB sample RAM by default, upgradeable to 1MB - Source: [FnLKPVzK7bo]
- Serial number format: K11 xxxx - Source: [FnLKPVzK7bo]
- Designed by Advanced Gravis and Forte Technology (1994) - Source: [FnLKPVzK7bo]

#### Hardware Features
- Plays up to 32 simultaneous notes from any combination of 32 voices - Source: [FnLKPVzK7bo]
- Sample-based synthesis (not FM) - musicians can use custom samples - Source: [FnLKPVzK7bo]
- May have Crystal Audio chip for Sound Blaster/AdLib compatibility - Source: [FnLKPVzK7bo]
- SCSI terminator package visible (220/330) - Source: [FnLKPVzK7bo]
- Base port address configurable via jumpers (default 240) - Source: [FnLKPVzK7bo]

#### Sound Blaster Compatibility
- SBOS (Sound Board Operating System) provides software Sound Blaster/AdLib emulation - Source: [FnLKPVzK7bo]
- Emulates Sound Blaster (NOT Sound Blaster Pro - no stereo) - Source: [FnLKPVzK7bo]
- Hardware-based Sound Blaster compatibility via Crystal chip (on some versions) - Source: [FnLKPVzK7bo]
- Sound Blaster emulation was lackluster, limiting real-world usefulness - Source: [FnLKPVzK7bo]

#### MT-32/General MIDI Emulation
- Mega-M emulator provides General MIDI, Roland MT-32, Sound Canvas emulation - Source: [FnLKPVzK7bo]
- MT-32 emulation limited - doesn't support custom sound uploads from games - Source: [FnLKPVzK7bo]
- Sound quality claimed to be better than original Sound Blaster - Source: [FnLKPVzK7bo]

#### Historical Context
- Peak popularity around 486 era (1993-1995) - Source: [FnLKPVzK7bo]
- Demo scene heavily used GUS for sample-based music - Source: [FnLKPVzK7bo]
- By Pentium era, CPU could do software mixing - GUS became less necessary - Source: [FnLKPVzK7bo]
- Many users ran GUS + Sound Blaster simultaneously due to compatibility issues - Source: [FnLKPVzK7bo]
- Original red PCB version was first release - Source: [FnLKPVzK7bo]
- Interwave boards (later, more modern) have difficult driver situation - Source: [FnLKPVzK7bo]
- Classic GUS boards are easier to use than Interwave - Source: [FnLKPVzK7bo]
- Very expensive on secondary market today - Source: [FnLKPVzK7bo]

#### Common Failures

##### Nichicon VZ Capacitor Leakage
- VZ series Nichicon caps from 1990s leak and corrode board - Source: [FnLKPVzK7bo]
- Located near audio amplifier section (top left area of board) - Source: [FnLKPVzK7bo]
- Symptoms: Weird high-pitched oscillation, changes frequency when touching board - Source: [FnLKPVzK7bo]
- Visible as green corrosion around capacitors - Source: [FnLKPVzK7bo]
- 470µF 16V caps typical values needing replacement - Source: [FnLKPVzK7bo]

##### Repair Procedure
1. Clean corrosion with vinegar - Source: [FnLKPVzK7bo]
2. Wash board with soap and water after vinegar treatment - Source: [FnLKPVzK7bo]
3. Replace leaking caps with equivalent values - Source: [FnLKPVzK7bo]
4. Only replace caps in same series (VZ) - other series likely fine - Source: [FnLKPVzK7bo]
5. Board will look good as new after cleaning - Source: [FnLKPVzK7bo]

##### CD-ROM Header Issue
- Plastic shroud on CD-ROM header often ripped off by careless removal - Source: [FnLKPVzK7bo]
- Pins remain intact, just missing plastic alignment piece - Source: [FnLKPVzK7bo]
- Cosmetic issue, doesn't affect function - Source: [FnLKPVzK7bo]

#### DOS Configuration

##### Environment Variables
- ULTRASOUND: Base IO, IRQ, DMA settings (e.g., `ULTRASOUND=240,1,5,5`) - Source: [FnLKPVzK7bo]
- ULTRA16: Required for Max version to enable detection - Source: [FnLKPVzK7bo]
- Must set ULTRA16 variable (see manual for exact format) - Source: [FnLKPVzK7bo]

##### Initialization
- ULTRINIT program required to initialize card before use - Source: [FnLKPVzK7bo]
- Without ULTRINIT, system may freeze when accessing card - Source: [FnLKPVzK7bo]
- Ultrasound software version 4.11 commonly used - Source: [FnLKPVzK7bo]

#### Audio Quality vs Modern Recreation
- Original GUS picks up noise from ISA bus (common for vintage cards) - Source: [FnLKPVzK7bo]
- PicoGUS uses external high-quality DAC, eliminates bus noise - Source: [FnLKPVzK7bo]
- PicoGUS has cleaner audio output than vintage hardware - Source: [FnLKPVzK7bo]

### PicoGUS (Modern Recreation)

#### Overview
- Raspberry Pi Pico-based GUS emulator - Source: [FnLKPVzK7bo]
- Open source project by Ian Scott (polpo) - Source: [FnLKPVzK7bo]
- ~$60-70 assembled from Tindie - Source: [FnLKPVzK7bo]
- Open source - can build your own from schematics - Source: [FnLKPVzK7bo]
- Uses high-quality DAC for 3.5mm stereo audio output - Source: [FnLKPVzK7bo]

#### Features
- Emulates GUS perfectly for most software - Source: [FnLKPVzK7bo]
- Software-defined: Can also emulate Tandy sound, Creative CMS, AdLib - Source: [FnLKPVzK7bo]
- Original Sound Blaster emulation coming - Source: [FnLKPVzK7bo]
- SID emulation possible (in development) - Source: [FnLKPVzK7bo]
- Has MIDI output - Source: [FnLKPVzK7bo]
- USB OTG support - can use Xbox 360 controller as PC joystick - Source: [FnLKPVzK7bo]
- LED flashes to indicate card activity - Source: [FnLKPVzK7bo]

#### Configuration
- Same ULTRASOUND environment variable as real GUS - Source: [FnLKPVzK7bo]
- Default base IO: 240 - Source: [FnLKPVzK7bo]
- Uses PGUSINIT instead of ULTRINIT - Source: [FnLKPVzK7bo]

#### Compatibility Testing
- Can help identify compatibility issues between GUS and other cards - Source: [FnLKPVzK7bo]
- Known issue: Second Reality demo crashes with XT-IDE 8-bit version - Source: [FnLKPVzK7bo]
- Same issue affects real GUS - not a PicoGUS bug - Source: [FnLKPVzK7bo]

#### Links
- Tindie: tindie.com/products/polpo/picogus-sound-card-emulator-for-isa-retro-pcs/ - Source: [FnLKPVzK7bo]
- GitHub: github.com/polpo/picogus - Source: [FnLKPVzK7bo]

## Tools & Equipment

### Testing Software
- Pinball Fantasies: Uses GUS for sample-based Amiga-style music - Source: [FnLKPVzK7bo]
- Cubic Player: Module file player with GUS support - Source: [FnLKPVzK7bo]
- Second Reality demo: Famous 1993 demo (copyrighted music) - Source: [FnLKPVzK7bo]
