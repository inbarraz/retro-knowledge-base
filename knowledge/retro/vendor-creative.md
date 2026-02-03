# Creative Labs

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Sound Blaster AWE64 (CT4520) | Sound Card | [51yfmDql8Z4] |
| Sound Blaster 32 | Sound Card | [51yfmDql8Z4] |

## Platform-Specific Knowledge

### Sound Blaster AWE64 / AWE32 / Sound Blaster 32

#### EMU8000 Wavetable Synthesis
- EMU8000 chip provides hardware wavetable synthesis - Source: [51yfmDql8Z4]
- EMU was a synthesizer company (now part of Creative) - Source: [51yfmDql8Z4]
- Can address up to 28MB of RAM directly - Source: [51yfmDql8Z4]
- Stock cards have 512K to 4MB RAM installed - Source: [51yfmDql8Z4]
- 1MB sound font ROM built into card - Source: [51yfmDql8Z4]

#### Wavetable vs Software Mixing
- 386SX too slow for software mixing of multi-channel audio - Source: [51yfmDql8Z4]
- With wavetable synthesis, 386SX can play 32-40 channel MOD files easily - Source: [51yfmDql8Z4]
- Without wavetable, 386SX struggles with even 4-channel files - Source: [51yfmDql8Z4]
- Pentium class CPU can do software mixing, making wavetable unnecessary - Source: [51yfmDql8Z4]
- Software mixing became the norm once Pentium CPUs were common - Source: [51yfmDql8Z4]

#### Programming Difficulty
- EMU8000 API is obtuse and difficult to program - Source: [51yfmDql8Z4]
- Gravis Ultrasound was easier to program, hence more demo scene support - Source: [51yfmDql8Z4]
- In Windows, driver handles complexity - games just use sound fonts - Source: [51yfmDql8Z4]

### RAM Expansion Options

#### Bits und Bolts RAM Boards
- Open source hardware RAM expansion for Sound Blaster cards - Source: [51yfmDql8Z4]
- Website: bitsundbolts.com - Source: [51yfmDql8Z4]
- YouTube: @bitsundbolts - Source: [51yfmDql8Z4]

#### Available Models
- Rapsity 28MB Edition: Uses lower density RAM chips - Source: [51yfmDql8Z4]
- MIDI Forge Sonata Rev 2: 28MB, uses 3.3V chips with voltage regulators - Source: [51yfmDql8Z4]
- Minuette: 8MB version (sufficient for DOS use) - Source: [51yfmDql8Z4]

#### RAM Chip Sources
- Can harvest RAM chips from old SIMMs - Source: [51yfmDql8Z4]
- PAL chip handles RAM addressing logic - Source: [51yfmDql8Z4]
- Sense pins configured via resistors to tell card how to map memory - Source: [51yfmDql8Z4]

#### Practical RAM Needs
- 8MB more than enough for DOS applications - Source: [51yfmDql8Z4]
- 28MB useful for Windows sound fonts (SF2 files up to 15-27MB exist) - Source: [51yfmDql8Z4]
- Cubic Player can use wavetable to play large MOD/XM/IT files - Source: [51yfmDql8Z4]

### DOS Configuration

#### UniSound Driver
- Alternative to Creative's DOS drivers - Source: [51yfmDql8Z4]
- URL: vogons.org/viewtopic.php?t=72553 - Source: [51yfmDql8Z4]
- All configuration in AUTOEXEC.BAT (no CONFIG.SYS changes needed) - Source: [51yfmDql8Z4]
- Easier for swapping sound cards frequently - Source: [51yfmDql8Z4]

#### I/O Ports
- Wavetable port: 620 hex (talks directly to EMU chip) - Source: [51yfmDql8Z4]
- MIDI port: 330 hex (external MIDI connector) - Source: [51yfmDql8Z4]
- General MIDI emulation uses original MIDI port (e.g., 320) - Source: [51yfmDql8Z4]

#### Sound Fonts in DOS
- DOS uses SBK files (Sound Bank 1.0 format) - Source: [51yfmDql8Z4]
- Windows uses SF2 files (Sound Font 2.0, more common, larger) - Source: [51yfmDql8Z4]
- SF2 to SBK conversion exists but converted files may not work correctly - Source: [51yfmDql8Z4]
- synth_gm.sbk file controls which sound font is loaded for GM emulation - Source: [51yfmDql8Z4]

#### Known Issues
- Some sound fonts have hanging note bugs in DOS - Source: [51yfmDql8Z4]
- May be DSP version issue or sound font conversion issue - Source: [51yfmDql8Z4]
- Same files work perfectly through MT-32 or Sound Canvas - Source: [51yfmDql8Z4]

### Testing Tools

#### Cubic Player (DOS)
- MOD/XM/IT file player with wavetable synthesis support - Source: [51yfmDql8Z4]
- Detects "Wave Blaster or Sound Blaster 32" for EMU8000 cards - Source: [51yfmDql8Z4]
- Shows available sample memory (e.g., M512, M8192, M28672) - Source: [51yfmDql8Z4]
- Edit INI file: Comment out "devw Sounder32" to disable wavetable - Source: [51yfmDql8Z4]
- Different mixers: Q (quality), F (FPU), fast integer - Source: [51yfmDql8Z4]

#### DIAGNOSE Utility
- Creative utility shows DRAM size on card - Source: [51yfmDql8Z4]
- Can test RAM - Source: [51yfmDql8Z4]
- Older versions may not work with newer cards (e.g., 1996 util vs AWE64) - Source: [51yfmDql8Z4]

#### DOS MIDI
- Simple MIDI file player for DOS - Source: [51yfmDql8Z4]
- Can use internal wavetable (port 620) or external MIDI (port 330) - Source: [51yfmDql8Z4]

### Thermal Notes
- Part of AWE64 card gets very hot during operation - Source: [51yfmDql8Z4]
- PCB may be slightly discolored in hot area - Source: [51yfmDql8Z4]
- Heat felt through back of board - Source: [51yfmDql8Z4]

## Related Hardware

### MIDI Forge Wavetable Module
- Wavetable expander using Raspberry Pi Zero - Source: [51yfmDql8Z4]
- Plugs into wavetable header on Sound Blaster 16 - Source: [51yfmDql8Z4]
- Emulates Roland MT-32 and other wavetable devices - Source: [51yfmDql8Z4]
- Uses I2C DAC (96kHz, 24-bit) for high quality output - Source: [51yfmDql8Z4]
- Includes small OLED screen and buttons - Source: [51yfmDql8Z4]
- Audio routed back through sound card - Source: [51yfmDql8Z4]

### Pico GUS
- Emulates Gravis Ultrasound perfectly - Source: [51yfmDql8Z4]
- 8MB PS-RAM for samples - Source: [51yfmDql8Z4]
- True MPU-401 compatibility (can use real MT-32/Sound Canvas) - Source: [51yfmDql8Z4]
- Same high-quality DAC module as MIDI Forge - Source: [51yfmDql8Z4]
- Open source hardware and software - Source: [51yfmDql8Z4]
- Less expensive than finding real MPU-401 cards - Source: [51yfmDql8Z4]
