# Cirrus Logic

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| GD-541 VGA Card | Video Card | [Yew71A7IaIQ] |

## Platform-Specific Knowledge

### GD-541 VGA Card

#### Overview
- Lower-end Cirrus Logic VGA chip - Source: [Yew71A7IaIQ]
- 2D hardware acceleration for Windows drawing operations - Source: [Yew71A7IaIQ]
- Hardware blitter for faster rectangle fills and drawing - Source: [Yew71A7IaIQ]
- 16-bit ISA card - Source: [Yew71A7IaIQ]
- Date code 1993 on chip - Source: [Yew71A7IaIQ]

#### Memory Configuration
- 256KB video RAM (fixed, not expandable on tested card) - Source: [Yew71A7IaIQ]
- Uses 44256 (256Kx4) DRAM chips - Source: [Yew71A7IaIQ]

#### 8-bit ISA Compatibility
- Card can work in 8-bit ISA slots - Source: [Yew71A7IaIQ]
- Marked "8 bit compatible" - 16-bit extension can hang off edge - Source: [Yew71A7IaIQ]
- Allows use in IBM PC/XT systems - Source: [Yew71A7IaIQ]

#### Performance Benchmarks (vidp speed at 10MHz ISA)
- 40x25 text: ~3.9KB/ms - Source: [Yew71A7IaIQ]
- 80x25 text: ~2.0KB/ms - Source: [Yew71A7IaIQ]
- 320x200x256: ~2.7KB/ms - Source: [Yew71A7IaIQ]
- Similar performance to Oak OTI-067 in raw throughput - Source: [Yew71A7IaIQ]
- 2D acceleration benefits Windows, not DOS benchmarks - Source: [Yew71A7IaIQ]

#### Video Output Characteristics
- Normal VGA analog signal levels - Source: [Yew71A7IaIQ]
- Compatible with capture devices without brightness adjustment - Source: [Yew71A7IaIQ]
- Text rendering appears slightly dimmer than Oak OTI-067 - Source: [Yew71A7IaIQ]

#### ISA Bus Speed Compatibility
- Works reliably at 10MHz ISA bus speed - Source: [Yew71A7IaIQ]
- Performance improves with faster ISA bus (if supported by motherboard) - Source: [Yew71A7IaIQ]
- Default 8MHz ISA works fine - Source: [Yew71A7IaIQ]

#### CGA/EGA Compatibility
- Emulates CGA and EGA modes in VGA - Source: [Yew71A7IaIQ]
- CGA emulation works correctly (unlike some Oak cards) - Source: [Yew71A7IaIQ]
- Packy Robot and other CGA games work properly - Source: [Yew71A7IaIQ]
- Jim Leonard CGA Compatibility Suite passes - Source: [Yew71A7IaIQ]
