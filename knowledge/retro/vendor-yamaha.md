# Yamaha

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| YMF719E-S Sound Card | ISA Sound Card | [vh9fVhSNzGg] |

## Platform-Specific Knowledge

### YMF719E-S ISA Sound Card

#### Overview
- Single-chip ISA sound card solution - Source: [vh9fVhSNzGg]
- Low-profile design - Source: [vh9fVhSNzGg]
- OPL3-compatible (FM synthesis) from Yamaha who created original AdLib chip - Source: [vh9fVhSNzGg]
- Perfect AdLib compatibility (Yamaha was original AdLib chip maker) - Source: [vh9fVhSNzGg]
- Sound Blaster compatible (8-bit only) - Source: [vh9fVhSNzGg]

#### Connections
- Audio output jack - Source: [vh9fVhSNzGg]
- Line input jack - Source: [vh9fVhSNzGg]
- Microphone input jack - Source: [vh9fVhSNzGg]
- MIDI/Game port (joystick connector) - Source: [vh9fVhSNzGg]
- Note: Audio output is FURTHEST from game port (opposite of Sound Blaster cards) - Source: [vh9fVhSNzGg]

#### Optional Wave Table
- Header for wave table module - Source: [vh9fVhSNzGg]
- Some cards have empty ROM socket for wave table synthesis chip - Source: [vh9fVhSNzGg]
- Wave table module may not fit due to low-profile card design - Source: [vh9fVhSNzGg]

#### DOS Configuration
- Works with UniSound driver - Source: [vh9fVhSNzGg]
- UniSound auto-detects Yamaha card and configures it - Source: [vh9fVhSNzGg]
- Typical settings: Port 220, IRQ 5, DMA 1, High DMA 3 - Source: [vh9fVhSNzGg]
- Set BLASTER environment variable for compatibility - Source: [vh9fVhSNzGg]
- UniSound sets up card but may not set BLASTER variable automatically - Source: [vh9fVhSNzGg]

#### Sound Blaster Compatibility
- Emulates Sound Blaster for 8-bit audio - Source: [vh9fVhSNzGg]
- NOT Sound Blaster 16 compatible (no 16-bit Sound Blaster mode) - Source: [vh9fVhSNzGg]
- DOS games using Doom/Duke Nukem 3D style 8-bit samples work fine - Source: [vh9fVhSNzGg]
- Games requiring 16-bit Sound Blaster won't get full fidelity - Source: [vh9fVhSNzGg]

#### Windows Sound System (WSS)
- Compatible with Windows Sound System - Source: [vh9fVhSNzGg]
- WSS mode provides 16-bit audio capability - Source: [vh9fVhSNzGg]
- WSS only works inside Windows (DOS box or Windows applications) - Source: [vh9fVhSNzGg]
- In pure DOS mode, limited to 8-bit Sound Blaster emulation - Source: [vh9fVhSNzGg]

#### Cost vs Sound Blaster
- Typically much cheaper than Sound Blaster cards - Source: [vh9fVhSNzGg]
- Good budget option for DOS gaming with AdLib/SB compatibility - Source: [vh9fVhSNzGg]
- If only needing AdLib + 8-bit Sound Blaster, this card is sufficient - Source: [vh9fVhSNzGg]

#### When to Choose Yamaha vs Sound Blaster
- Yamaha: Budget builds, AdLib-focused games, 8-bit games - Source: [vh9fVhSNzGg]
- Sound Blaster 16: Need 16-bit audio in DOS, broader compatibility - Source: [vh9fVhSNzGg]
- Most DOS games (Doom, Duke Nukem 3D, etc.) use 8-bit samples anyway - Source: [vh9fVhSNzGg]

## Historical Notes

### Yamaha and AdLib Heritage
- Yamaha designed the original OPL2/OPL3 FM synthesis chips used in AdLib cards - Source: [vh9fVhSNzGg]
- AdLib sound in games = Yamaha FM synthesis - Source: [vh9fVhSNzGg]
- Yamaha sound cards have perfect AdLib compatibility because they use genuine Yamaha chips - Source: [vh9fVhSNzGg]
