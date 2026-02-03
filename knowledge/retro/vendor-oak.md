# Oak Technologies

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| OTI-067 VGA/EGA/CGA Card | Video Card | [Yew71A7IaIQ] |

## Platform-Specific Knowledge

### OTI-067 VGA/EGA/CGA Multi-Mode Video Card

#### Overview
- Dual output card: VGA analog (HD15) and TTL digital (DE-9) - Source: [Yew71A7IaIQ]
- Supports VGA, EGA, CGA, MDA, and Hercules modes - Source: [Yew71A7IaIQ]
- 16-bit ISA card that also works in 8-bit slots - Source: [Yew71A7IaIQ]
- Oak Technologies OTI-067 main chip - Source: [Yew71A7IaIQ]
- BIOS date code 1988 on chip sticker - Source: [Yew71A7IaIQ]

#### Memory Configuration
- Base configuration: 256KB video RAM - Source: [Yew71A7IaIQ]
- Expandable to 512KB with additional 44256 DRAM chips - Source: [Yew71A7IaIQ]
- Uses 4256K (256Kx4) DRAM chips - two chips = 256KB - Source: [Yew71A7IaIQ]
- No jumpers needed for RAM detection (auto-detect) - Source: [Yew71A7IaIQ]

#### DIP Switch Settings (6-position)
- Switches 1-4 control monitor type selection - Source: [Yew71A7IaIQ]
- Switches 5-6 listed as "reserved" in manual but may need correct position - Source: [Yew71A7IaIQ]
- Switch settings based on DFI VG-7000 compatible manual - Source: [Yew71A7IaIQ]

#### Monitor Type Switch Settings (SW1-4)
| Monitor Type | SW1 | SW2 | SW3 | SW4 |
|--------------|-----|-----|-----|-----|
| CGA Color | On | On | On | On |
| MDA Pure (no emulation) | On | On | On | Off |
| EGA Pure (no emulation) | On | Off | On | Off |
| VGA Color | Off | On | Off | On |
| VGA Monochrome | On | Off | Off | On |
| 8514 Monitor | Off | Off | On | On |
| NEC Multi-Sync Monitors | Various | | | |

- Off = Open, On = Closed - Source: [Yew71A7IaIQ]
- VGA Color mode limits resolution to 640x480 max - Source: [Yew71A7IaIQ]
- System will hang if high-res mode attempted with VGA Color setting - Source: [Yew71A7IaIQ]

#### Jumpers
- JP2/JP3: Interlace/Non-interlace mode selection - Source: [Yew71A7IaIQ]
- Only active in modes 55/56/57 (high-res interlaced) - Source: [Yew71A7IaIQ]
- JP1/JP2: IRQ2 enable/disable - Source: [Yew71A7IaIQ]
- IRQ2 typically disabled (not used by most software) - Source: [Yew71A7IaIQ]
- One jumper may control 8-bit vs 16-bit mode - Source: [Yew71A7IaIQ]

#### Performance Benchmarks (vidp speed utility)
- VGA mode at 10MHz ISA bus speed: - Source: [Yew71A7IaIQ]
  - 40x25 text: ~3.8KB/ms
  - 80x25 text: ~2.0KB/ms
  - 320x200x256: ~2.7KB/ms
- EGA mode shows similar or faster performance - Source: [Yew71A7IaIQ]
- CGA mode performs faster than EGA in some tests - Source: [Yew71A7IaIQ]
- Significantly faster than actual IBM EGA card in EGA modes - Source: [Yew71A7IaIQ]

#### 8-bit Slot Compatibility
- Works in 8-bit ISA slots without jumper changes - Source: [Yew71A7IaIQ]
- Performance approximately halved in 8-bit mode - Source: [Yew71A7IaIQ]
- 16-bit extension hangs off end of 8-bit slot - Source: [Yew71A7IaIQ]

#### TTL Digital Output (VGA Timing)
- Outputs VGA timing (640x480/720x400 at 70Hz) over TTL - Source: [Yew71A7IaIQ]
- Works with multisync TTL monitors that support VGA timings - Source: [Yew71A7IaIQ]
- RGB2HDMI can capture this mode with OTI VGA profile - Source: [Yew71A7IaIQ]
- 320x200 mode outputs as 640x400 (scan doubled) - Source: [Yew71A7IaIQ]
- Limited to 16 TTL colors (no VGA palette support) - Source: [Yew71A7IaIQ]

#### Known Issues
- CGA graphics modes may not work (card-specific fault) - Source: [Yew71A7IaIQ]
- Text modes and EGA modes work but CGA graphics freeze - Source: [Yew71A7IaIQ]
- CGA row reprogramming (demo effects) does work - Source: [Yew71A7IaIQ]
- Likely OTI-067 chip failure if CGA emulation broken - Source: [Yew71A7IaIQ]
- Crystal oscillator physical damage doesn't cause CGA-only failure - Source: [Yew71A7IaIQ]

#### RGB Brightness
- Card outputs hotter analog RGB signals than typical VGA cards - Source: [Yew71A7IaIQ]
- May cause blown-out/clipped whites on capture devices - Source: [Yew71A7IaIQ]
- Reduce brightness in capture device settings to compensate - Source: [Yew71A7IaIQ]
- Not an issue with analog CRT monitors (adjust brightness knob) - Source: [Yew71A7IaIQ]

#### Comparison to Later Cards
- No 2D acceleration (unlike Cirrus Logic GD-541) - Source: [Yew71A7IaIQ]
- Slower than dedicated VGA cards but faster in legacy modes - Source: [Yew71A7IaIQ]
- Good "jack of all trades" for systems with various monitors - Source: [Yew71A7IaIQ]
